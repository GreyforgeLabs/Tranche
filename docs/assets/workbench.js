/* Tranche workbench. Pure query helpers also run under node:test. */
(function (root) {
  'use strict';
  const normalize = value => String(value ?? '').normalize('NFKD').replace(/[\u0300-\u036f]/g, '').toLowerCase();
  const words = value => normalize(value).match(/[\p{L}\p{N}_-]+/gu) || [];
  // Optimal string alignment distance: insertion, deletion, substitution, transposition.
  function distance(a, b) {
    const matrix = Array.from({length: a.length + 1}, (_, i) => [i]);
    for (let j = 0; j <= b.length; j++) matrix[0][j] = j;
    for (let i = 1; i <= a.length; i++) {
      for (let j = 1; j <= b.length; j++) {
        matrix[i][j] = Math.min(matrix[i - 1][j] + 1, matrix[i][j - 1] + 1,
          matrix[i - 1][j - 1] + (a[i - 1] === b[j - 1] ? 0 : 1));
        if (i > 1 && j > 1 && a[i - 1] === b[j - 2] && a[i - 2] === b[j - 1]) {
          matrix[i][j] = Math.min(matrix[i][j], matrix[i - 2][j - 2] + 1);
        }
      }
    }
    return matrix[a.length][b.length];
  }
  function index(pr) {
    return {text: normalize(`${pr.title} ${pr.author} ${pr.number} ${pr.body}`),
      tokens: words(`${pr.title} ${pr.author} ${pr.body}`)};
  }
  function matches(pr, query, searchIndex, wordCache) {
    const terms = normalize(query).trim().split(/\s+/).filter(Boolean);
    if (!terms.length) return true;
    const haystack = searchIndex || index(pr);
    return terms.every(term => {
      if (/^#?\d+$/.test(term)) return String(pr.number) === term.replace(/^#/, '');
      if (term.startsWith('@')) return normalize(pr.author) === term.slice(1);
      if (haystack.text.includes(term)) return true;
      const tolerance = term.length >= 8 ? 2 : term.length >= 4 ? 1 : 0;
      return tolerance > 0 && haystack.tokens.some(word => {
        if (Math.abs(word.length - term.length) > tolerance) return false;
        const key = `${term}\0${word}`;
        if (wordCache?.has(key)) return wordCache.get(key);
        const matched = distance(term, word) <= tolerance;
        wordCache?.set(key, matched);
        return matched;
      });
    });
  }
  // Issue #3: security is the top-priority meta-category; its queue leads the nav.
  const queues = {security: 'security_priority', all: null, candidates: 'candidate', senior: 'senior', followup: 'followup', related: 'related'};
  const PAGE_SIZE = 30;
  function select(rows, state = {}, indexes) {
    const field = queues[state.queue || 'all'];
    const wordCache = new Map(); // Repeated corpus vocabulary pays edit distance only once.
    const filtered = rows.filter(pr => (!field || pr[field]) &&
      (!state.category || state.category === 'all' || pr.category === state.category) &&
      matches(pr, state.q || '', indexes?.get(pr.number), wordCache));
    filtered.sort((a, b) => {
      // Issue #3: top priority first — the security meta-category outranks every chosen order.
      if (a.security_priority !== b.security_priority) return a.security_priority ? -1 : 1;
      if (state.sort === 'security') {
        // Inside each group: descending security probability, unknown last.
        const av = typeof a.security === 'number' && Number.isFinite(a.security) ? a.security : -1;
        const bv = typeof b.security === 'number' && Number.isFinite(b.security) ? b.security : -1;
        return (bv - av) || a.number - b.number;
      }
      const riskSort = state.sort === 'risk';
      const av = riskSort ? a.risk : Date.parse(a.created);
      const bv = riskSort ? b.risk : Date.parse(b.created);
      const ak = typeof av === 'number' && Number.isFinite(av);
      const bk = typeof bv === 'number' && Number.isFinite(bv);
      if (ak !== bk) return ak ? -1 : 1;
      if (!ak) return a.number - b.number;
      return (state.sort === 'oldest' ? av - bv : bv - av) || a.number - b.number;
    });
    const pages = Math.max(1, Math.ceil(filtered.length / PAGE_SIZE));
    const page = Math.max(1, Math.min(pages, Number.isSafeInteger(state.page) ? state.page : 1));
    return {items: filtered.slice((page - 1) * PAGE_SIZE, page * PAGE_SIZE), total: filtered.length, page, pages};
  }
  function positiveInteger(value) {
    return /^[1-9]\d*$/.test(String(value)) && Number.isSafeInteger(Number(value)) ? Number(value) : null;
  }
  function parseState(search, categories = ['all']) {
    const params = new URLSearchParams(search);
    const queue = params.get('queue');
    const category = params.get('category');
    const sort = params.get('sort');
    return {q: params.get('q') || '', queue: Object.hasOwn(queues, queue) ? queue : 'all',
      category: categories.includes(category) ? category : 'all',
      sort: ['newest', 'oldest', 'risk', 'security'].includes(sort) ? sort : 'newest',
      page: positiveInteger(params.get('page')) || 1, pr: positiveInteger(params.get('pr'))};
  }
  function serializeState(state) {
    const params = new URLSearchParams();
    if (state.q) params.set('q', state.q);
    if (state.queue && state.queue !== 'all') params.set('queue', state.queue);
    if (state.category && state.category !== 'all') params.set('category', state.category);
    if (state.sort && state.sort !== 'newest') params.set('sort', state.sort);
    if (state.page > 1) params.set('page', state.page);
    if (positiveInteger(state.pr)) params.set('pr', state.pr);
    return params.size ? `?${params}` : '';
  }
  const api = {matches, index, select, parseState, serializeState};
  if (typeof module !== 'undefined' && module.exports) module.exports = api;
  root.TrancheWorkbench = api;
  if (typeof document !== 'undefined') boot();

  function boot() {
    const dataElement = document.getElementById('workbench-data');
    if (!dataElement) return;
    const data = JSON.parse(dataElement.textContent);
    const rows = data.prs;
    const byNumber = new Map(rows.map(pr => [pr.number, pr]));
    const indexes = new Map(rows.map(pr => [pr.number, index(pr)]));
    const categories = ['all', ...Object.keys(data.categories)];
    const $ = id => document.getElementById(id);
    const dialog = $('pr-dialog');
    let state = parseState(location.search, categories);
    let listKey = '';
    let returnFocus = null;
    let timer;
    const formatCount = n => n.toLocaleString('en-US');
    const metric = (value, ceiling, probability = false) => typeof value === 'number' && Number.isFinite(value)
      ? `${value.toFixed(probability ? 2 : 1)}${ceiling ? ` / ${ceiling}` : ''}` : 'Unknown';
    function node(tag, text, className) {
      const element = document.createElement(tag);
      if (text !== undefined) element.textContent = text;
      if (className) element.className = className;
      return element;
    }
    function button(text, action, className) {
      const element = node('button', text, className);
      element.type = 'button';
      element.addEventListener('click', action);
      return element;
    }
    function categoryLabel(cat) { return data.categories[cat] || 'Unknown'; }
    function githubLink(number) {
      const link = node('a', 'Open pull request on GitHub ↗', 'github-link');
      // Never trust captured URLs, query strings or model text as link targets.
      if (positiveInteger(number)) link.href = `https://github.com/omacom/omarchy/pull/${number}`;
      link.target = '_blank'; link.rel = 'noopener noreferrer';
      return link;
    }
    function inspect(number) {
      if (!byNumber.has(number)) return;
      if (!dialog.open) returnFocus = document.activeElement;
      update({pr: number});
    }
    function memberButton(number) {
      const pr = byNumber.get(number);
      if (!pr) return node('span', `#${number} · outside captured corpus`);
      return button(`#${number} · ${pr.title}`, () => inspect(number), 'related-member');
    }
    function pairLine(pair, label) {
      const item = node('li', undefined, 'pair-diagnostic');
      const a = Array.isArray(pair) ? pair[0] : pair.a;
      const b = Array.isArray(pair) ? pair[1] : pair.b;
      item.append(memberButton(a), node('span', ' ↔ '), memberButton(b));
      const verdict = String(pair.verdict || 'unknown').replaceAll('_', ' ');
      const detail = Array.isArray(pair) ? 'Not compared' : `${pair.classification || 'unknown'} · ${verdict} · P(same): ${metric(pair.p_same, null, true)}`;
      item.append(node('p', `${label}: ${detail}`, 'small'));
      return item;
    }
    function relationships(pr, content) {
      content.append(node('h3', 'Related PRs'));
      const section = node('div', undefined, 'relationships');
      let found = false;
      const groups = [
        ...data.groups.confirmed_groups.map(members => ({members, consistent: true})),
        ...data.groups.review_groups,
      ];
      for (const group of groups.filter(g => g.members.includes(pr.number))) {
        found = true;
        section.append(node('h4', group.consistent ? 'Model-consistent candidate group' : 'Group needing relationship review'));
        const members = node('div', undefined, 'related-members');
        group.members.forEach(n => members.append(memberButton(n)));
        section.append(members);
        const diagnostics = node('ul', undefined, 'diagnostics');
        for (const [key, label] of [['conflicting_pairs', 'Conflict'], ['uncertain_pairs', 'Uncertain relationship'], ['missing_pairs', 'Missing pair']]) {
          (group[key] || []).forEach(pair => diagnostics.append(pairLine(pair, label)));
        }
        section.append(diagnostics);
        if (group.unbound_evidence) section.append(node('p', 'Unbound legacy evidence — revisions cannot be checked.', 'small'));
      }
      const pairs = data.groups.uncertain_pairs.filter(pair => pair.a === pr.number || pair.b === pr.number);
      if (pairs.length) {
        found = true;
        section.append(node('h4', 'Pairs needing a human comparison'));
        const list = node('ul', undefined, 'diagnostics');
        pairs.forEach(pair => list.append(pairLine(pair, 'Relationship')));
        section.append(list);
      }
      section.append(node('p', found ? 'Model-suggested relationships, not verified duplicates. No survivor selected; compare code and fix coverage.' : 'No suggested relationships in this capture.', 'small'));
      content.append(section);
    }
    function renderDetail(pr) {
      $('detail-number').textContent = `PULL REQUEST #${pr.number}`;
      const content = $('detail-content');
      content.replaceChildren();
      const title = node('h2', pr.title); title.id = 'detail-title';
      content.append(title, githubLink(pr.number));
      const properties = node('dl', undefined, 'properties');
      const fields = [
        ['Author', `@${pr.author}`], ['Category', categoryLabel(pr.category)],
        ['Status', pr.draft ? 'Draft' : 'Not draft'], ['Created', pr.created || 'Unknown'],
        ['Model evidence', pr.freshness === 'current' ? 'Bound judgment · title and description only' : pr.freshness === 'unbound' ? 'Unbound legacy judgment · revisions not checked' : 'Unjudged or stale'],
        ['Model risk', metric(pr.risk, 4)], ['Security probability', metric(pr.security, null, true)],
        ['Finished form', metric(pr.finished, 3)], ['Review effort', metric(pr.effort, 3)],
        ['Fix probability', metric(pr.is_fix, null, true)], ['Diffstat', pr.diffstat || 'Unknown'],
      ];
      for (const [label, value] of fields) {
        const field = node('div'); field.append(node('dt', label), node('dd', value)); properties.append(field);
      }
      content.append(properties, node('h3', 'Description snippet'));
      content.append(node('p', pr.body || 'No description supplied.', 'body-snippet'));
      if (pr.body_truncated) content.append(node('p', 'Captured snippet is shortened. Read the full description on GitHub.', 'small'));
      relationships(pr, content);
    }
    function render() {
      const result = select(rows, state, indexes);
      state.page = result.page;
      if (state.pr && !byNumber.has(state.pr)) state.pr = null;
      $('search').value = state.q;
      $('sort').value = state.sort;
      $('category').value = state.category;
      document.querySelectorAll('[data-queue]').forEach(b => b.setAttribute('aria-pressed', String(b.dataset.queue === state.queue)));
      document.querySelectorAll('[data-category]').forEach(b => b.setAttribute('aria-pressed', String(b.dataset.category === state.category)));
      const start = result.total ? (result.page - 1) * PAGE_SIZE + 1 : 0;
      const end = Math.min(result.page * PAGE_SIZE, result.total);
      $('result-count').textContent = `${formatCount(result.total)} results · ${formatCount(start)}–${formatCount(end)} of ${formatCount(result.total)} · ${formatCount(rows.length)} captured PRs`;
      $('empty').hidden = result.total !== 0;
      $('prev').disabled = result.page <= 1;
      $('next').disabled = result.page >= result.pages;
      $('page-label').textContent = `Page ${result.page} of ${result.pages}`;
      const nextKey = JSON.stringify([state.q, state.queue, state.category, state.sort, state.page]);
      if (nextKey !== listKey) {
        listKey = nextKey;
        const fragment = document.createDocumentFragment();
        for (const pr of result.items) {
          const item = node('li', undefined, 'pr-row');
          const opener = button('', () => inspect(pr.number), 'pr-open');
          opener.dataset.number = pr.number;
          opener.setAttribute('aria-label', `Inspect PR #${pr.number}: ${pr.title}`);
          const heading = node('span', undefined, 'pr-heading');
          heading.append(node('span', `#${pr.number}`, 'pr-number'), node('span', pr.title, 'pr-title'));
          const meta = node('span', undefined, 'pr-meta');
          meta.append(node('span', `@${pr.author}`, 'pr-author'), node('span', categoryLabel(pr.category)),
            node('span', pr.created ? pr.created.slice(0, 10) : 'Date unknown'));
          if (pr.draft) meta.append(node('span', 'Draft', 'tag draft'));
          if (pr.security_priority) meta.append(node('span', 'Security first', 'tag security'));
          if (pr.related) meta.append(node('span', 'Related', 'tag'));
          if (pr.freshness !== 'current') meta.append(node('span', pr.freshness === 'unbound' ? 'Unbound evidence' : 'Unjudged / stale', 'tag'));
          const info = node('span', undefined, 'pr-info'); info.append(heading, meta);
          const risk = node('span', metric(pr.risk, 4), `risk ${pr.risk == null ? 'unknown' : pr.risk >= 3 ? 'high' : 'known'}`);
          risk.setAttribute('aria-label', `Model risk ${metric(pr.risk, 4)}`);
          opener.append(info, risk);
          item.append(opener); fragment.append(item);
        }
        $('results').replaceChildren(fragment);
      }
      if (state.pr) {
        if (dialog.dataset.number !== String(state.pr)) {
          renderDetail(byNumber.get(state.pr)); dialog.dataset.number = state.pr;
          if (dialog.open) {dialog.scrollTop = 0; $('close-detail').focus();}
        }
        if (!dialog.open) {returnFocus = document.activeElement; dialog.showModal();}
      } else if (dialog.open) {
        dialog.close(); dialog.dataset.number = '';
        const fallback = document.querySelector(`.pr-open[data-number="${returnFocus?.dataset?.number || ''}"]`);
        (returnFocus?.isConnected ? returnFocus : fallback || $('search')).focus();
      }
    }
    function writeURL(replace = false) {
      const url = location.pathname + serializeState(state) + location.hash;
      if (url !== location.pathname + location.search + location.hash) history[replace ? 'replaceState' : 'pushState'](null, '', url);
    }
    function update(change, replace = false) {
      clearTimeout(timer);
      state = {...state, ...change}; render(); writeURL(replace);
    }
    function reset() { update({q: '', queue: 'all', category: 'all', sort: 'newest', page: 1, pr: null}); }
    for (const category of categories) {
      const count = category === 'all' ? rows.length : rows.filter(pr => pr.category === category).length;
      const b = button('', () => update({category, page: 1, pr: null}), 'category-button');
      b.dataset.category = category;
      b.append(node('span', category === 'all' ? 'All categories' : categoryLabel(category)), node('span', formatCount(count), 'category-count'));
      $('category-buttons').append(b);
    }
    document.querySelectorAll('[data-queue]').forEach(b => {
      const field = queues[b.dataset.queue];
      b.querySelector('span').textContent = formatCount(field ? rows.filter(pr => pr[field]).length : rows.length);
      b.addEventListener('click', () => update({queue: b.dataset.queue, page: 1, pr: null}));
    });
    $('search').addEventListener('input', () => {
      clearTimeout(timer);
      timer = setTimeout(() => update({q: $('search').value, page: 1, pr: null}), 50);
    });
    $('sort').addEventListener('change', () => update({sort: $('sort').value, page: 1, pr: null}));
    $('category').addEventListener('change', () => update({category: $('category').value, page: 1, pr: null}));
    $('prev').addEventListener('click', () => update({page: state.page - 1, pr: null}));
    $('next').addEventListener('click', () => update({page: state.page + 1, pr: null}));
    $('reset').addEventListener('click', reset); $('empty-reset').addEventListener('click', reset);
    $('close-detail').addEventListener('click', () => update({pr: null}));
    dialog.addEventListener('cancel', event => {event.preventDefault(); update({pr: null});});
    window.addEventListener('popstate', () => {clearTimeout(timer); state = parseState(location.search, categories); render(); writeURL(true);});
    document.addEventListener('keydown', event => {
      const editing = /INPUT|TEXTAREA|SELECT/.test(event.target.tagName) || event.target.isContentEditable;
      if (!dialog.open && ((event.key === '/' && !editing && !event.ctrlKey && !event.metaKey) || ((event.ctrlKey || event.metaKey) && event.key.toLowerCase() === 'k'))) {
        event.preventDefault(); $('search').focus(); $('search').select();
      }
    });
    render(); writeURL(true);
  }
})(typeof globalThis !== 'undefined' ? globalThis : this);
