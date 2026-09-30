'use strict';
const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const source = path.join(__dirname, '../docs/assets/workbench.js');
const api = fs.existsSync(source) ? require(source) : {};
const {execFileSync} = require('node:child_process');
const os = require('node:os');

// Dependency-free, offline DOM integration on the same Chromium as browser QA.
let chromium;
try { chromium = execFileSync('which', ['chromium'], {encoding: 'utf8'}).trim(); } catch {}
test('browser workbench renders safe text, inspects PRs, restores focus and URL state', {skip: !chromium}, () => {
  const directory = fs.mkdtempSync(path.join(os.tmpdir(), 'tranche-browser-'));
  try {
    const pagePath = path.join(directory, 'probe.html');
    const page = fs.readFileSync(path.join(__dirname, '../docs/index.html'), 'utf8');
    const data = {prs: [{number: 1234, title: 'Fix <img src=x onerror="window.pwned=1"> suspend', body: '</script><b>bluetooth</b>', author: 'river', category: 'docs', created: '2026-01-01', risk: null, security: 0.8, security_priority: true, finished: null, draft: false, freshness: 'unjudged or stale', related: true, candidate: false, senior: false, followup: false}], categories: {docs: 'Docs', unknown: 'Unknown'}, groups: {confirmed_groups: [], review_groups: [], uncertain_pairs: [{a: 1234, b: 4321, verdict: 'unrelated', p_same: 0.9, classification: 'contradictory'}]}};
    data.prs.push({number:4321, title:'Add screensaver timer', body:'', author:'stone', category:'docs', created:'2025-01-01', risk:0, security:0, security_priority:false, finished:0, draft:true, freshness:'current', related:true});
    data.groups.review_groups.push({members:[1234,4321], conflicting_pairs:[{a:1234,b:4321,verdict:'unrelated',p_same:0.1,classification:'different'}], uncertain_pairs:[], missing_pairs:[[1234,9999]], unbound_evidence:true});
    const payload = JSON.stringify(data).replace(/</g, '\\u003c');
    const probe = `<script>window.addEventListener('DOMContentLoaded', async () => {
      const report = document.createElement('pre'); report.id = 'probe-result'; document.body.append(report);
      const check = (v, message) => {if (!v) throw new Error(message)};
      const wait = () => new Promise(r => setTimeout(r, 80));
      try {
        check(getComputedStyle(document.body).backgroundColor === 'rgb(22, 22, 30)', 'Tokyo Night stylesheet loaded');
        check(getComputedStyle(document.querySelector('.pr-open')).borderRadius === '0px', 'square interface');
        check(document.documentElement.scrollWidth <= innerWidth, 'no horizontal page overflow');
        check(document.querySelector('.wordmark img').currentSrc.endsWith('tranche-title.png'), 'desktop reduced-motion asset');
        document.body.dispatchEvent(new KeyboardEvent('keydown', {key:'/', bubbles:true, cancelable:true}));
        check(document.activeElement.id === 'search', 'slash shortcut');
        document.querySelector('#sort').focus();
        document.body.dispatchEvent(new KeyboardEvent('keydown', {key:'k', ctrlKey:true, bubbles:true, cancelable:true}));
        check(document.activeElement.id === 'search', 'Ctrl K shortcut');
        check(document.querySelectorAll('.pr-row').length === 2, 'all captured PRs rendered');
        check(!window.pwned && !document.querySelector('#results img'), 'title stays inert');
        check(document.querySelector('[data-queue="security"]').textContent.includes('Security first'), 'security queue leads the nav');
        check([...document.querySelectorAll('[data-queue]')][0].dataset.queue === 'security', 'security is the first queue button');
        check(document.querySelector('[data-queue="batched"]')?.textContent.includes('Batched'), 'batched queue exists');
        check(document.querySelector('#sort option[value=security]')?.textContent.includes('Security'), 'security sort option');
        const row = document.querySelector('.pr-open'); row.focus(); row.click();
        check(document.querySelector('dialog').open, 'native dialog opens');
        check(document.querySelector('#detail-title').textContent === ${JSON.stringify(data.prs[0].title)}, 'full title');
        check(document.querySelector('#detail-content').textContent.includes('Unknown'), 'unknown not zero');
        check(document.querySelector('.pr-meta .tag.security')?.textContent === 'Security first', 'security priority tag');
        check(!document.querySelector('#detail-content b'), 'body stays text');
        check(document.querySelector('#detail-content a').href === 'https://github.com/omacom/omarchy/pull/1234', 'safe github link');
        check(location.search.includes('pr=1234'), 'selection deep link');
        document.querySelector('#close-detail').click();
        check(!document.querySelector('dialog').open && document.activeElement === row, 'focus restored');
        const search = document.querySelector('#search'); search.value = 'suspned'; search.dispatchEvent(new Event('input')); await wait();
        check(document.querySelectorAll('.pr-row').length === 1, 'typo search in UI');
        search.value = 'nothingmatches'; search.dispatchEvent(new Event('input')); await wait();
        check(!document.querySelector('#empty').hidden, 'no results');
        document.querySelector('#empty-reset').click();
        check(document.querySelectorAll('.pr-row').length === 2 && !location.search, 'reset');
        document.querySelector('[data-queue="senior"]').click();
        check(!document.querySelector('#empty').hidden && location.search.includes('queue=senior'), 'queue URL');
        history.back(); await wait();
        check(document.querySelectorAll('.pr-row').length === 2 && search.value === '', 'back restores');
        history.forward(); await wait();
        check(!document.querySelector('#empty').hidden, 'forward restores');
        history.replaceState(null, '', location.pathname + '?pr=1234'); window.dispatchEvent(new PopStateEvent('popstate'));
        check(document.querySelector('dialog').open, 'deep link opens inspector');
        check(document.querySelector('.relationships').textContent.includes('Missing pair: Not compared'), 'readable missing-pair diagnostic');
        check(document.querySelector('.relationships').textContent.includes('Conflict: different'), 'readable conflict diagnostic');
        const related = [...document.querySelectorAll('.related-member')].find(b => b.textContent.startsWith('#4321'));
        related.focus(); related.click();
        check(document.querySelector('#detail-title').textContent === 'Add screensaver timer', 'related PR navigation');
        check(document.activeElement === document.querySelector('#close-detail'), 'inspector focus survives related navigation');
        const ev = new Event('cancel', {cancelable:true}); document.querySelector('dialog').dispatchEvent(ev);
        check(!document.querySelector('dialog').open, 'escape cancel closes');
        check(!document.querySelector('#detail-content img'), 'no injected markup');
        const clone = document.documentElement.cloneNode(true);
        clone.querySelectorAll('script, #probe-result').forEach(el => el.remove());
        const frame = document.createElement('iframe'); frame.style.width = '390px'; frame.style.border = '0';
        frame.srcdoc = '<!doctype html>' + clone.outerHTML; document.body.append(frame);
        await new Promise(resolve => frame.addEventListener('load', resolve, {once:true}));
        const mobile = frame.contentDocument;
        check(mobile.documentElement.scrollWidth <= 390, '390px has no overflow');
        check(mobile.querySelector('.wordmark img').currentSrc.endsWith('omarchy-title.png'), 'mobile reduced-motion asset');
        check(frame.contentWindow.getComputedStyle(mobile.querySelector('.tranche-motion')).animationName === 'none', 'reduced motion disables name animation');
        check(mobile.querySelector('.product-note')?.getClientRects().length > 0, 'honest product note visible on mobile');
        frame.remove();
        report.textContent = 'BROWSER_PASS';
      } catch (error) {report.textContent = 'BROWSER_FAIL: ' + error.message}
    });</script>`;
    const modified = page.replace('<head>', `<head><base href="file://${path.resolve(__dirname, '../docs')}/">`)
      .replace(/<script id="workbench-data" type="application\/json">[\s\S]*?<\/script>/, () => `<script id="workbench-data" type="application/json">${payload}</script>`)
      .replace('</body>', probe + '</body>');
    fs.writeFileSync(pagePath, modified);
    const output = execFileSync(chromium, ['--headless', '--no-sandbox', '--disable-gpu', '--force-prefers-reduced-motion', '--allow-file-access-from-files', `--user-data-dir=${directory}/profile`, '--virtual-time-budget=5000', '--dump-dom', `file://${pagePath}`], {encoding: 'utf8', timeout: 20000, maxBuffer: 4 * 1024 * 1024, stdio: ['ignore', 'pipe', 'ignore']});
    const result = output.match(/<pre id="probe-result">([^<]*)<\/pre>/)?.[1];
    assert.equal(result, 'BROWSER_PASS');
  } finally {fs.rmSync(directory, {recursive: true, force: true});}
});

test('search matches real typos, title, number, author, and description terms', () => {
  assert.equal(typeof api.matches, 'function', 'fuzzy search is implemented');
  const pr = {number: 1234, title: 'Fix suspend initialization', author: 'river', body: 'Restore bluetooth pairing after resume'};
  for (const query of ['suspned', 'suspnd', 'bluetooh', '#1234', '@river', 'suspend pairing', '1234 river']) {
    assert.equal(api.matches(pr, query), true, query);
  }
  for (const query of ['nonexistent', '#123', '@rivet', 'suspend nonexistent']) {
    assert.equal(api.matches(pr, query), false, query);
  }
  assert.equal(api.matches(pr, ''), true);
});

test('queues and categories filter independently; page totals include all results', () => {
  assert.equal(typeof api.select, 'function', 'queue selection is implemented');
  const rows = Array.from({length: 61}, (_, i) => ({number: i + 1, title: 'Suspend fix', body: '', author: 'river', category: i % 2 ? 'docs' : 'hardware-drivers', candidate: i < 10, senior: i === 60, followup: i === 20, related: i > 55, security_priority: i < 3}));
  assert.equal(api.select(rows, {queue: 'all', page: 2}).total, 61);
  assert.equal(api.select(rows, {queue: 'all', page: 2}).items.length, 30);
  assert.equal(api.select(rows, {queue: 'all', page: 3}).items.length, 1);
  assert.equal(api.select(rows, {queue: 'all', page: 999}).page, 3);
  assert.equal(api.select(rows, {queue: 'candidates', category: 'docs'}).total, 5);
  assert.equal(api.select(rows, {queue: 'senior'}).total, 1);
  assert.equal(api.select(rows, {queue: 'followup'}).total, 1);
  assert.equal(api.select(rows, {queue: 'related'}).total, 5);
  assert.equal(api.select(rows, {queue: 'security'}).total, 3, 'security meta-category queue');
  const empty = api.select(rows, {q: 'nothinghere', page: 9});
  assert.equal(empty.total, 0);
  assert.equal(empty.page, 1);
  assert.deepEqual(empty.items, []);
});

test('batched queue selects only PRs carrying pre-release batches', () => {
  const rows = [{number: 1, batches: [{id: 'docs-B1'}]}, {number: 2, batches: []}, {number: 3}];
  assert.equal(api.select(rows, {queue: 'batched'}).total, 1);
  assert.equal(api.select(rows, {queue: 'batched'}).items[0].number, 1);
  assert.equal(api.select(rows, {queue: 'all'}).total, 3);
});

test('security meta-category outranks every chosen sort; security sort orders by probability', () => {
  const rows = [
    {number: 1, created: '2026-01-01', risk: 0, security: 0.2, security_priority: false},
    {number: 2, created: '2026-01-04', risk: 4, security: 0.9, security_priority: true},
    {number: 3, created: '2026-01-03', risk: 1, security: 0.5, security_priority: true},
    {number: 4, created: '2026-01-02', risk: 2, security: null, security_priority: false},
  ];
  const ids = sort => api.select(rows, {sort}).items.map(pr => pr.number);
  assert.deepEqual(ids('newest'), [2, 3, 4, 1], 'priority leads, then newest first');
  assert.deepEqual(ids('oldest'), [3, 2, 1, 4], 'priority leads, then oldest first');
  assert.deepEqual(ids('risk'), [2, 3, 4, 1], 'priority leads, then risk high first');
  assert.deepEqual(ids('security'), [2, 3, 1, 4], 'probability order inside each group');
  const rowsWithUnknown = [...rows, {number: 5, created: '2026-01-05', risk: 0, security: null, security_priority: false}];
  const securityOrder = api.select(rowsWithUnknown, {sort: 'security'}).items.map(pr => pr.number);
  assert.deepEqual(securityOrder, [2, 3, 1, 4, 5], 'unknown security probability last');
});

test('date and model risk sorts are deterministic with unknown values last', () => {
  const rows = [{number: 1, created: '2026-01-01', risk: null}, {number: 2, created: '2026-01-02', risk: 0}, {number: 3, created: '2026-01-03', risk: 4}, {number: 4, created: '', risk: null}];
  const ids = sort => api.select(rows, {sort}).items.map(pr => pr.number);
  assert.deepEqual(ids('newest'), [3, 2, 1, 4]);
  assert.deepEqual(ids('oldest'), [1, 2, 3, 4]);
  assert.deepEqual(ids('risk'), [3, 2, 1, 4]);
  assert.deepEqual(rows.map(pr => pr.number), [1, 2, 3, 4], 'source is not mutated');
});

test('URL state round trips search, queue, category, sort, page and selected PR', () => {
  assert.equal(typeof api.parseState, 'function', 'deep links are implemented');
  const categories = ['all', 'docs', 'unknown'];
  const state = {q: 'suspend @river #1234', queue: 'senior', category: 'docs', sort: 'risk', page: 3, pr: 1234};
  assert.deepEqual(api.parseState(api.serializeState(state), categories), state);
  assert.deepEqual(api.parseState('?q=%3Cscript%3E&queue=no&category=bad&sort=no&page=-5&pr=javascript:1', categories), {q: '<script>', queue: 'all', category: 'all', sort: 'newest', page: 1, pr: null});
  for (const value of ['2.5', '1e2', 'Infinity', '9007199254740993', '0', '-1', 'NaN']) {
    assert.equal(api.parseState(`?page=${value}&pr=${value}`, categories).page, 1);
    assert.equal(api.parseState(`?page=${value}&pr=${value}`, categories).pr, null);
  }
  assert.equal(api.serializeState(api.parseState('', categories)), '');
});
