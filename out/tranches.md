# Tranche — historical Omarchy PR report

> Historical, unbound model-only output. The rows and scores below are retained from the original run, not reevaluated. Descriptions were judged; patches, tests, security and supersedence were not verified. Treat historical readiness and survivor labels as discovery leads, not merge or closure approvals.

Corpus: 2832 open PRs, 2832 judged. Duplicate groups: 101 (225 PRs). Ready-to-roll candidates: 802. Needs author follow-up: 113. Escalate: 324.

Method: one batched Jev call per PR (category / risk / is_fix / dupe_signal / finished_form / review_effort / security_flag); duplicate candidates found by title similarity within a category, confirmed by a Jev pair judgment; groups via union-find.

## Tranche: desktop-config — 306 PRs recommended as a merge-ready roll-up

| PR | title | author | finished | effort | fix |
|---|---|---|---|---|---|
| #10182 | Tag Waterfox as a Firefox-based browser | nzkritik | 3.0 | 0.2 | 0.92 |
| #7736 | Match LocalSend's current Wayland app ID | OldJobobo | 3.0 | 1.2 | 0.97 |
| #13255 | Fix menu JSONC trailing-comma stripping corrupting string values | buger | 3.0 | 1.1 | 0.98 |
| #9629 | Hide notifications during screensaver | ClGratton | 3.0 | 1.5 | 0.92 |
| #9280 | Dereference relative symlinks when staging user themes | fresh3nough | 3.0 | 1.3 | 0.98 |
| #7756 | Stop building a theme signature nothing reads | Adolanium | 3.0 | 1.1 | 0.64 |
| #13564 | Move the parked overlay to the focused monitor before it is shown | manuaudio | 2.9 | 1.1 | 0.98 |
| #7173 | Localize clock bar weekday/month names | dr-moreira | 2.9 | 0.9 | 0.93 |
| #12512 | Exclude covered windows from the capture picker | sanjyay | 2.9 | 1.0 | 0.97 |
| #10274 | Keep panel sliders from losing the pointer grab inside a ScrollView | AntoineGagnon1 | 2.9 | 1.1 | 0.98 |
| #8681 | Hide Ghostty scrollbar in screensaver | nameproof | 2.9 | 0.7 | 0.88 |
| #10743 | Fix Super+V in Codex's integrated terminal | Skeptomenos | 2.9 | 1.4 | 0.96 |
| #7806 | Drop key auto-repeat in the lock screen password field | berndb | 2.9 | 1.2 | 0.98 |
| #13511 | Fix menu JSONC top-level array rendering phantom rows | buger | 2.9 | 0.7 | 0.98 |
| #12763 | Recover off-screen JetBrains Toolbox windows | nikooo777 | 2.9 | 1.0 | 0.95 |
| #12676 | Parse keys whose type is spelled out in the keybindings menu | seletz | 2.9 | 1.2 | 0.96 |
| #11887 | Preserve bar space while the shell restarts | jkarmel | 2.9 | 2.7 | 0.74 |
| #13133 | Sync vscode theme test with the real-file extension | anandude | 2.9 | 1.0 | 0.93 |
| #7273 | Match the volume OSD icon to the output switcher | xymbol | 2.9 | 1.8 | 0.76 |
| #12385 | Report failed theme removal before announcing success | yashranaway | 2.9 | 1.1 | 0.98 |
| #10577 | Enable resolve_binds_by_sym for high XF86 keycodes | fresh3nough | 2.9 | 0.8 | 0.79 |
| #10383 | Open tray menus on left-click when a menu is exposed | fresh3nough | 2.9 | 1.1 | 0.96 |
| #7088 | Fix polkit password dots rendering as tiny specks | ax1g | 2.9 | 0.2 | 0.97 |
| #13065 | Update the VS Code theme CLI checks for the copied theme file | en3r0 | 2.9 | 1.1 | 0.90 |
| #12042 | Render every modifier Hyprland can bind in the keybindings menu | jimjimovich | 2.9 | 1.0 | 0.93 |
| #8560 | Restore lock screen password focus lost on suspend | robouk | 2.9 | 1.0 | 0.97 |
| #13713 | theme-set-claude/pi: clean up staged tmp file when settings update fails | kvnloo | 2.9 | 1.2 | 0.97 |
| #10704 | Prevent Super+C/V/X send_key_state from retriggering the bind | gw7523 | 2.9 | 1.1 | 0.97 |
| #10494 | Allow Hyprland binding switches in Lua diagnostics | jfturcot | 2.9 | 0.8 | 0.72 |
| #7495 | Keep the monitor layout when changing scale | Piemme99 | 2.9 | 1.2 | 0.97 |
| #6896 | Apply the system keyboard layout to the SDDM greeter | g-desoutter | 2.9 | 1.6 | 0.95 |
| #11858 | Clear and swallow the lock-screen wake key so it is not typed as a password char | h14h | 2.9 | 1.1 | 0.96 |
| #10468 | Name keycode bindings after the layout the keyboard is using | seletz | 2.9 | 1.9 | 0.89 |
| #13709 | fix(hyprland): reload guard skips instances whose getoption has no bool | kvnloo | 2.9 | 1.0 | 0.98 |
| #13503 | Keep Foot's font size when changing the font | ashuttl | 2.9 | 1.0 | 0.98 |
| #13722 | menu keybindings: --config requires a value, reject unknown flags | kvnloo | 2.8 | 1.3 | 0.95 |
| #11639 | Fix calendar date clipping | MBemera | 2.8 | 1.2 | 0.96 |
| #10129 | Restore the presentation terminal after a shell restart | falser101 | 2.8 | 1.4 | 0.96 |
| #9976 | Load personal Hyprland overrides through require_optional.safe | fresh3nough | 2.8 | 1.5 | 0.96 |
| #7404 | Accept theme-set display names in theme remove | 686f6c61 | 2.8 | 1.0 | 0.97 |
| #13755 | Propagate display-power dispatch failures | mrcobas | 2.8 | 1.0 | 0.95 |
| #12307 | Prefer a known internal touchpad when an external trackpad is connected | shmlkv | 2.8 | 1.8 | 0.89 |
| #11863 | Skip dwindle togglesplit on scrolling workspaces | Per0-1 | 2.8 | 1.1 | 0.94 |
| #13552 | Route fcitx5 D-Bus activation through omarchy-fcitx5.service | Ray0907 | 2.8 | 1.4 | 0.95 |
| #12814 | Keep panel focus during panel switches | dt-lindberg | 2.8 | 0.9 | 0.96 |
| #11882 | Fix stale menu-image thumbnails after in-place overwrite (#11806) | thescurry | 2.8 | 1.1 | 0.98 |
| #7713 | Include dual-width fonts in font picker | OldJobobo | 2.8 | 1.3 | 0.89 |
| #7592 | Refocus the lock password field after resume | RovshanMuradov | 2.8 | 1.1 | 0.97 |
| #7419 | Let Chromium size and position PiP windows (Fixes #7391) | shrijit37 | 2.8 | 1.0 | 0.97 |
| #10277 | Enable bar widgets for active hybrid plugins | arisgysel-design | 2.8 | 1.5 | 0.96 |
| #7011 | Keep bar clicks out of login shells | SL0wZEr | 2.8 | 1.8 | 0.74 |
| #6871 | Keep the menu populated across git swaps of its definition file | dhh | 2.8 | 1.1 | 0.95 |
| #13581 | Keep Google Meet browser border when switching tabs | ryantm | 2.8 | 1.1 | 0.92 |
| #12712 | Fix infinite iteration in keybinding scanner API stubs | wulujia | 2.8 | 1.1 | 0.98 |
| #7717 | Widen the column for full width on scrolling workspaces | donperi | 2.8 | 1.1 | 0.92 |
| #7563 | Clear a stuck bar-move ghost when the gesture is interrupted | calledtoconstruct | 2.8 | 1.2 | 0.98 |
| #9760 | List hybrid plugins as enabled when they live in plugins[] | ujo4eva | 2.8 | 1.1 | 0.94 |
| #10571 | Raise themed readable-text mixes to WCAG AA contrast | fresh3nough | 2.8 | 1.4 | 0.86 |
| #7465 | Fix Obsidian focus pattern for its current app id | johnnynia | 2.8 | 0.4 | 0.98 |
| #7036 | Fix enabling and disabling a display doing nothing | sterre-g | 2.8 | 1.0 | 0.98 |
| #8695 | Cap screensaver frame rate at the panel refresh rate | nbeerbower | 2.8 | 1.3 | 0.65 |
| #5881 | Account for keyboard layout variant for keybinding helper | blegat | 2.8 | 1.5 | 0.90 |
| #13495 | clock: make panel SystemClock precision follow the bar's seconds detection | aasmpro | 2.8 | 1.1 | 0.90 |
| #9978 | Load personal hypr.envs after package Hyprland defaults | fresh3nough | 2.8 | 1.8 | 0.97 |
| #9972 | Skip readonly moduleName/settings writes in bar injectProps | fresh3nough | 2.8 | 1.0 | 0.97 |
| #8980 | fix(shell): keep notification dismiss button visible | fgrehm | 2.8 | 1.2 | 0.93 |
| #11034 | Clamp notification cards to the width their container has | SimonSchubert | 2.7 | 1.2 | 0.95 |
| #10565 | Drop shift:both_capslock_cancel from default kb_options | fresh3nough | 2.7 | 1.6 | 0.73 |
| #10564 | Skip opening an empty scratchpad on Super+S | fresh3nough | 2.7 | 1.2 | 0.96 |
| #9984 | Render bar tooltips as StyledText for rich plugin markup | fresh3nough | 2.7 | 0.8 | 0.96 |
| #9408 | Follow the icon theme inheritance chain when building the app icon index | VykosMolt | 2.7 | 2.3 | 0.88 |
| #11080 | Fix PluginBarApi hover-reveal writes so cloned panels can close | SomeoneWithOptions | 2.7 | 1.8 | 0.97 |
| #8411 | Fix out-of-range group window shortcuts | wxasacoder | 2.7 | 1.3 | 0.98 |
| #7240 | Fix invisible VS Code list hover state | yacobmole | 2.7 | 0.4 | 0.96 |
| #9000 | Fix clipped left border on Display scale 1x pill | mubshrx | 2.7 | 1.0 | 0.97 |
| #7560 | Fix weather panel hero overlapping location at triple-digit temps | guilhermetk | 2.7 | 0.9 | 0.97 |
| #6958 | Preserve terminal font size when changing font family | sbalbalosa | 2.7 | 1.3 | 0.97 |
| #8069 | Add fallback logic to resolve current user in SDDM greeter | ErikMelton | 2.7 | 1.6 | 0.97 |
| #12862 | Re-tile Meet meeting windows caught by the PiP rule | anandude | 2.7 | 1.5 | 0.96 |
| #12538 | Treat idle timeout 0 as disabled, not immediate | paulogeyer | 2.7 | 1.0 | 0.98 |
| #9362 | Coerce bar set values to the widget manifest type | fresh3nough | 2.7 | 1.7 | 0.97 |
| #8258 | Fix Brave Origin refresh collision | llirik0 | 2.7 | 1.2 | 0.97 |
| #6467 | fix(panel-slider): color-match muted knob to dimmed fill line | itscallssh | 2.7 | 1.4 | 0.93 |
| #13132 | Keep tmux from stamping backgrounds on self-reloading terminals | anandude | 2.7 | 1.5 | 0.93 |
| #12541 | Apply brightness to mirrored external displays | paulogeyer | 2.7 | 1.2 | 0.94 |
| #10989 | fix: keep 1.25x tooltip and scale-pill borders from dropping edges | kvnloo | 2.7 | 1.9 | 0.97 |
| #10931 | Preserve bar widgets when the layout changes | kristofferR | 2.7 | 2.8 | 0.84 |
| #8942 | Anchor the clock and weather popups under their widgets | scottjones | 2.7 | 1.0 | 0.92 |
| #13475 | Dismiss open panels and grant focus grace period on screensaver launch | AnPod | 2.6 | 1.7 | 0.97 |
| #10693 | Ignore missing group window indexes | aastrand | 2.6 | 1.0 | 0.95 |
| #7413 | Keep background refreshes from scrolling an open select menu | melonamin | 2.6 | 1.6 | 0.97 |
| #13851 | Fix clock widget rendering weekday/month names in English regardless of locale | SloBloLabs | 2.6 | 0.9 | 0.98 |
| #12517 | Position picture-in-picture from its final size, like webcam overlay | ludagoo | 2.6 | 1.1 | 0.94 |
| #11238 | Fit the weather panel to narrow popups | SimonSchubert | 2.6 | 1.2 | 0.95 |
| #8393 | Say when an installed theme's files are refused | scottjones | 2.6 | 1.4 | 0.67 |
| #7723 | Keep last good shell config when user shell.json fails to parse | felixzsh | 2.6 | 1.5 | 0.83 |
| #11475 | Detach nightlight startup from captured command output | yashranaway | 2.6 | 1.0 | 0.98 |
| #7269 | Run the shell on the Vulkan backend on primary NVIDIA GPUs | PavelAlennikov | 2.6 | 1.6 | 0.92 |
| #6642 | Keep the lock blank from turning the display off (DPMS link-drop crash) | akashgagda | 2.6 | 1.2 | 0.78 |
| #9479 | Keep launched apps on the workspace they started from | ClumZeez | 2.6 | 1.8 | 0.83 |
| #13593 | Scale the bar spacer with the spacing scale and text size | Susensio | 2.6 | 0.9 | 0.76 |
| #6904 | Dismiss an open shell panel with Super+W | csfh | 2.6 | 1.9 | 0.90 |
| #9985 | Resolve notification image-path through iconSource | fresh3nough | 2.6 | 0.9 | 0.97 |
| #8768 | Give btop a float big enough for its 80x24 minimum | nbeerbower | 2.6 | 0.9 | 0.95 |
| #8625 | Keep kitty font zoom when switching themes | AccursedGalaxy | 2.6 | 1.5 | 0.84 |
| #7488 | Detect Apple Silicon trackpads in omarchy-hw-touchpad | Skeptomenos | 2.6 | 0.5 | 0.93 |
| #9049 | Give TUI windows a terminal-sized touchpad scroll rule | PyRo1121 | 2.6 | 1.4 | 0.92 |
| #11970 | Wire serviceFor for installed third-party bar plugins (#11949) | thescurry | 2.6 | 1.1 | 0.98 |
| #7497 | Stop monitor scaling from persisting a scale the reload will undo | davydotcom | 2.6 | 1.6 | 0.96 |
| #10077 | Release the panel cursor when the pointer leaves a row | ludagoo | 2.6 | 2.3 | 0.89 |
| #9570 | Rearm idle monitor after timeout changes | rookepoole | 2.6 | 1.5 | 0.96 |
| #11496 | Size the weather bar icon like the other bar icons | SemihMutlu07 | 2.6 | 1.0 | 0.77 |
| #9535 | Show browser shortcuts only when their extensions are enabled | qybaihe | 2.6 | 1.8 | 0.67 |
| #13684 | Re-probe night light after each minute so the bar follows hyprsunset's schedule | Susensio | 2.5 | 1.3 | 0.96 |
| #11244 | Clamp the lock screen's password field to the screen width | SimonSchubert | 2.5 | 1.0 | 0.95 |
| #9614 | omarchy #9544 launch-or-focus agent titles (fork PR) | kvnloo | 2.5 | 1.3 | 0.96 |
| #9245 | Fix context menus for Wine tray items | clementrog | 2.5 | 1.8 | 0.97 |
| #8350 | Paste clipboard history with Ctrl+V outside terminals | fregys | 2.5 | 1.5 | 0.90 |
| #13718 | theme-set-pi: stop stomping the user's chosen theme on re-provision | kvnloo | 2.5 | 1.3 | 0.94 |
| #13190 | Always show notification dismiss control | guillesrl | 2.5 | 1.1 | 0.65 |
| #11223 | Refuse a theme with no palette instead of applying it | vovarbv | 2.5 | 1.2 | 0.96 |
| #7283 | Use layout-independent universal clipboard shortcuts | janhesters | 2.5 | 1.7 | 0.95 |
| #11578 | Derive publicBarConfig() from shellConfig to fix one-step-late plugin APIs | AnPod | 2.5 | 1.1 | 0.97 |
| #12189 | Only reload local plugins when loadable sources change | DonnieFi | 2.5 | 1.9 | 0.91 |
| #9211 | Wake the lock screen on resume and keep wake keys out of the password | phedoreanu | 2.5 | 1.9 | 0.92 |
| #9882 | Tag Chromium --app web apps as chromium-based browsers | fresh3nough | 2.5 | 1.0 | 0.96 |
| #13103 | Refocus the origin window before pasting a picked clipboard entry | surim0n | 2.5 | 2.0 | 0.97 |
| #11441 | Include windows from all visible displays in screenshot picker | Tunahanyrd | 2.5 | 2.2 | 0.88 |
| #8876 | Stop keybinding scans from looping on mocked APIs | yashranaway | 2.5 | 1.9 | 0.97 |
| #8259 | Keep notification contents out of process arguments | llirik0 | 2.5 | 2.9 | 0.74 |
| #7536 | Treat Ctrl+[ as panel escape | NorthernReach | 2.5 | 1.1 | 0.83 |
| #11239 | Close open bar panels while the screensaver is up | ninepointlabs | 2.5 | 1.6 | 0.95 |
| #9296 | Recover screen-recording indicator after stuck probes | fresh3nough | 2.5 | 1.5 | 0.98 |
| #9279 | Tag Vivaldi's window class case-insensitively in browser.lua | reverb256 | 2.5 | 0.7 | 0.98 |
| #8802 | Show every Hyprland workspace in the bar, not only 1-10 | kizzd | 2.5 | 1.5 | 0.76 |
| #9742 | Float Omawrite's file dialogs | wulujia | 2.5 | 0.5 | 0.96 |
| #7910 | window-pop: don't tile an already-floating window | tahadx | 2.5 | 1.2 | 0.98 |
| #6693 | Preserve borders on Google Meet browser windows | timohubois | 2.5 | 1.1 | 0.95 |
| #13379 | Stop fetching system stats the power panel no longer shows | benwillems | 2.5 | 1.6 | 0.94 |
| #13259 | Force DPMS enable on system wake when status is stale | Bartok9 | 2.5 | 1.2 | 0.87 |
| #11447 | Ship fcitx5 wayland.conf so layouts are not pushed to the compositor | twinkybot | 2.5 | 0.5 | 0.95 |
| #10958 | Fix bar reordering for duplicate widgets | roonakyadav | 2.4 | 2.1 | 0.98 |
| #10628 | Gate active-window title to the focused monitor | fresh3nough | 2.4 | 1.7 | 0.94 |
| #9281 | Fit the presentation terminal to its logo instead of a fixed 875x600 | londospark | 2.4 | 1.7 | 0.86 |
| #13409 | Wait for the shell (for its notification service) before launching autostart app | mihailo-obradovic | 2.4 | 1.1 | 0.95 |
| #9649 | Deduplicate monitor outputs with matching EDIDs | pallavk | 2.4 | 2.5 | 0.92 |
| #7296 | feat: wrap the overflowing text in the menu | Sameer292 | 2.4 | 0.8 | 0.90 |
| #11269 | Fix DaVinci Resolve Download Manager focus lock | AksharP5 | 2.4 | 0.4 | 0.97 |
| #10984 | Pin gcr-prompter so Unlock Keyring stays on the current workspace | Literato2 | 2.4 | 0.9 | 0.87 |
| #10470 | Fix SDDM password field sometimes not getting focus on load | woodenplastic | 2.4 | 1.0 | 0.98 |
| #13787 | Fix square aspect toggle on scrolling workspaces | mkenter | 2.4 | 1.4 | 0.98 |
| #9967 | Resolve a live Hyprland signature before restarting the shell | fresh3nough | 2.4 | 1.8 | 0.97 |
| #9133 | Resolve keycodes with the active keyboard layout | yashranaway | 2.4 | 1.8 | 0.95 |
| #9015 | Make scrolling columns resizable at workspace edge | hancengiz | 2.4 | 1.5 | 0.87 |
| #7954 | Remember menu selection when navigating back | mauhaa | 2.4 | 1.7 | 0.67 |
| #8437 | Hide Obsidian's window buttons in the Omarchy theme | ecomodeller | 2.4 | 0.9 | 0.69 |
| #7738 | Notifications: clicking a toast focuses the exact sending window when focus_on_a | nixfred | 2.4 | 1.1 | 0.96 |
| #12991 | fix(clipboard): paste into the window that opened the manager (#12987) | kvnloo | 2.4 | 1.6 | 0.98 |
| #12961 | fix(hypr): layout-toggle named workspaces by name selector | kvnloo | 2.4 | 1.2 | 0.97 |
| #9889 | Load workspace layout saves from the layouts directory | fresh3nough | 2.4 | 1.8 | 0.97 |
| #7833 | Remove the toast when a sender closes its own notification | lucletoffe | 2.4 | 1.1 | 0.97 |
| #13776 | Step the bar below the screensaver while one is up | manuaudio | 2.4 | 1.2 | 0.97 |
| #12579 | Keep the Omarchy screensaver from firing during VLC playback | evandrojr | 2.4 | 1.0 | 0.91 |
| #13580 | Tint Cloudflare connected tray icon for light themes | ryantm | 2.4 | 0.9 | 0.73 |
| #13541 | Catch the bar clock up after a suspend | stevederico | 2.4 | 1.2 | 0.97 |
| #13497 | Fix: white/vantablack request a Yaru grey variant no package ships | baron-hines | 2.4 | 0.8 | 0.97 |
| #10210 | Fix theme switcher listing a theme twice when a user override has no preview | johnsideserf | 2.4 | 0.9 | 0.98 |
| #7905 | Dictation indicator toggles dictation on left click | tahadx | 2.4 | 1.2 | 0.93 |
| #11414 | Fix monitor scaling widget coupling multiple monitors' scale | bfagundez | 2.4 | 1.6 | 0.98 |
| #10578 | Silence fcitx5 startup layout tip notifications | fresh3nough | 2.4 | 1.7 | 0.96 |
| #7471 | Wake the blanked lock screen from the keyboard | notTanveer | 2.4 | 1.1 | 0.96 |
| #13104 | Keep the last valid shell.json when the user file is truncated | surim0n | 2.4 | 1.8 | 0.97 |
| #7794 | Step running foot windows to the new text size | scottjones | 2.4 | 1.9 | 0.78 |
| #13092 | Write the monospace rule to a conf.d drop-in, not fonts.conf | surim0n | 2.3 | 1.1 | 0.96 |
| #10570 | Sync GDK_SCALE into app launch environments on scale change | fresh3nough | 2.3 | 1.2 | 0.96 |
| #9986 | Theme Hyprland decoration glow with border colors | fresh3nough | 2.3 | 1.0 | 0.95 |
| #8307 | Stop re-sampling the wallpaper for the transparent bar on unrelated state writes | ryanyogan | 2.3 | 1.6 | 0.95 |
| #12606 | Inhibit idle and screensaver when browsers or video web apps are fullscreen | murdawkmedia | 2.3 | 1.2 | 0.78 |
| #12360 | Toggle a touchpad's mouse-emulation sibling with it | z23 | 2.3 | 1.7 | 0.95 |
| #13473 | Reserve only revealed tray drawer width when collapsed | AnPod | 2.3 | 1.1 | 0.96 |
| #13784 | Make the screensaver fullscreen when a layer surface holds keyboard focus | seantimm | 2.3 | 1.0 | 0.95 |
| #12377 | Fix emoji/clipboard paste into browsers with Ctrl+V | AndrijaSkontra | 2.3 | 1.8 | 0.92 |
| #13313 | Reject shell metacharacters in USB input-device names | Chessing234 | 2.3 | 1.1 | 0.93 |
| #10106 | Float LibreOffice file dialogs | Mina-Sayed | 2.3 | 0.9 | 0.86 |
| #10002 | Add drop-zone candidates for empty bar sections | fresh3nough | 2.3 | 1.1 | 0.95 |
| #11946 | Fix calendar hero overflowing on narrow panels (MacBook M1 Pro) | marcindyguda | 2.3 | 1.7 | 0.98 |
| #9667 | fix: idle-inhibit Steam games matching steam_app_* | kvnloo | 2.3 | 1.1 | 0.96 |
| #8907 | foot: render light themes into [colors-light] so foot reports the right color-th | rubas | 2.3 | 1.0 | 0.96 |
| #8341 | Fix Bitwarden extension popout rendering | TyRichards | 2.3 | 1.6 | 0.97 |
| #13100 | notifications: honor expireTimeout for critical alerts | surim0n | 2.3 | 1.1 | 0.97 |
| #12756 | Disable fcitx5 QuickPhrase's Super+grave trigger | quanru | 2.3 | 2.0 | 0.90 |
| #9203 | Stop restoring a stale keyboard backlight on idle-cycle cancel | phedoreanu | 2.3 | 1.2 | 0.96 |
| #7241 | Inset BorderSurface strokes a device pixel to survive clip edges | gsamokovarov | 2.3 | 1.0 | 0.94 |
| #13579 | Wait for the first plugin scan before building the stock bar | manuaudio | 2.2 | 1.4 | 0.97 |
| #13097 | Label the weather panel with the location that supplied the weather | surim0n | 2.2 | 1.2 | 0.96 |
| #10260 | Gate screensaver launches on window class and pidof -x | fresh3nough | 2.2 | 1.1 | 0.97 |
| #11838 | Fix calendar and weather popup text colours | tcballard | 2.2 | 1.2 | 0.97 |
| #10190 | Fix workspace indicator after monitor move | dzanaga | 2.2 | 0.9 | 0.97 |
| #6918 | Keep Wi-Fi indicator online when AP object is missing | patrickrodrigues-aa | 2.2 | 1.6 | 0.96 |
| #12257 | fix(bar/tray): collapse the tray drawer's reserved space | nas3ts | 2.2 | 1.9 | 0.93 |
| #9590 | Clear stale graphical-session before uwsm so SDDM autologin is not a blank scree | pib-nbsmedia | 2.2 | 1.8 | 0.96 |
| #8741 | Prevent network address values from overlapping labels | avk458 | 2.2 | 0.8 | 0.93 |
| #8086 | Re-arm idle monitor when timeouts change in shell.json (#8038) | askadityapandey | 2.2 | 1.7 | 0.97 |
| #12975 | Dismiss screensaver on pointer activity after launch settle | kvnloo | 2.2 | 2.0 | 0.96 |
| #12258 | Keep the screensaver up until it has been focused once | z23 | 2.2 | 1.2 | 0.97 |
| #8825 | Add --no-gtk option to display text size command | pazthor | 2.2 | 1.8 | 0.74 |
| #7716 | Gate calculator keybindings with preinstalls | OldJobobo | 2.2 | 1.0 | 0.96 |
| #12118 | Make scrolling Alt-Tab follow visual order | DaDecky | 2.2 | 2.0 | 0.71 |
| #10630 | Fix stale Wi-Fi connection state in network bar | chivopic | 2.2 | 1.1 | 0.98 |
| #8059 | Keep Hyprland helpers global | catlee | 2.2 | 1.0 | 0.95 |
| #7451 | menu: scale wheel events 3x for faster touchpad scrolling on long lists | tahadx | 2.2 | 1.1 | 0.75 |
| #7290 | Keep tray icons rendering when an icon switches symbolic state | chiengyn | 2.2 | 1.0 | 0.97 |
| #12654 | Prevent screensaver during fullscreen browser video | Caya231 | 2.2 | 1.6 | 0.75 |
| #12501 | Use output-relative slurp coordinates for region share | paulogeyer | 2.2 | 1.1 | 0.90 |
| #12431 | Fix: menu `No matches for "abc.."` message overflow | kaunkrishna | 2.2 | 0.5 | 0.92 |
| #9135 | Let on-screen keyboards reach the menu | yashranaway | 2.2 | 1.4 | 0.96 |
| #12963 | fix(media): stop marquee while playback is paused | kvnloo | 2.2 | 1.4 | 0.98 |
| #12962 | fix(lock): give session lock 1500ms to stabilize outputs | kvnloo | 2.2 | 0.1 | 0.97 |
| #12183 | Keep weather widget visible when wttr.in TLS fails (#11999) | thescurry | 2.2 | 1.2 | 0.96 |
| #11035 | Toggle keybindings with Super+K | KrishRVH | 2.2 | 0.9 | 0.76 |
| #10361 | Raise browser windows that open behind the presentation float | gradlman | 2.2 | 1.8 | 0.96 |
| #13332 | Fall back to hyprsunset gamma on displays without DDC/CI | C50NK4 | 2.1 | 1.7 | 0.65 |
| #8922 | Keep the image selector fast when vips cannot read an image | bjarneo | 2.1 | 1.7 | 0.91 |
| #12016 | Open a hidden workspace on the bar that was clicked | mikebenner | 2.1 | 1.2 | 0.93 |
| #10574 | Wake SDDM greeter displays on input and lid events | fresh3nough | 2.1 | 1.5 | 0.97 |
| #9565 | Keep fcitx5 aligned with Hyprland keyboard layouts | rookepoole | 2.1 | 2.4 | 0.65 |
| #13679 | Dismiss tray menu on activate and hide tooltip over it | AnPod | 2.1 | 1.4 | 0.82 |
| #13647 | Clear fullscreen stolen when screensaver loses focus | AnPod | 2.1 | 1.0 | 0.96 |
| #13483 | Fix tooltip border clipping at fractional scales | iccodes | 2.1 | 1.0 | 0.97 |
| #8773 | Fix premature lock reblank on slow displays | ClGratton | 2.1 | 2.0 | 0.96 |
| #7029 | Show the new track on the media OSD instead of the player name | Orkunnnn | 2.1 | 1.6 | 0.93 |
| #6533 | Make keyboard backlight steps consistent in both directions | merdiofriviaisherebitch | 2.1 | 2.0 | 0.96 |
| #12931 | Load high contrast VS Code themes as hc-black/hc-light | Bryan-Legend | 2.1 | 1.0 | 0.84 |
| #11981 | Fix fullscreen Steam game window rules | flrsn | 2.1 | 1.9 | 0.95 |
| #8732 | Keep hyprsunset running after a restart | lamchun1110 | 2.1 | 1.9 | 0.96 |
| #13460 | Guard panel close against throwing plugin implementations | AnPod | 2.1 | 1.6 | 0.98 |
| #7020 | Float Java AWT XWayland popups instead of tiling them | v-t-r-gg | 2.1 | 1.0 | 0.87 |
| #12362 | Pin the keybindings row order to one collation | linyiru | 2.1 | 1.1 | 0.84 |
| #10270 | Reduce notification overlay surface area | nicknack5050 | 2.1 | 2.4 | 0.67 |
| #9509 | Refresh the bar clock on wake so it does not sit stale after suspend | reverb256 | 2.1 | 1.1 | 0.97 |
| #8815 | Distinguish plugged in but not charging in the bar battery icon | VardanMelkonyan | 2.1 | 1.0 | 0.74 |
| #12338 | Make the menu search line a real text input | linyiru | 2.1 | 1.6 | 0.96 |
| #11610 | Debounce AppLibrary appsChanged() against spurious DesktopEntries churn | shingoku2 | 2.1 | 1.7 | 0.97 |
| #10414 | Disable broken Inhibit portal so video holds off the screensaver | DegenApeDev | 2.1 | 1.3 | 0.95 |
| #9345 | Fix slider knob stopping short of the track end | ejuro | 2.1 | 1.0 | 0.94 |
| #9186 | Reapply clamshell disable after idle wake | pauloklaus | 2.1 | 1.1 | 0.97 |
| #7245 | fix(shell): position bar widget panels relative to anchor widget | ax1g | 2.1 | 1.5 | 0.97 |
| #13126 | Keep the reveal mask rendering so background transitions animate | ScytheAkira | 2.1 | 0.9 | 0.98 |
| #10130 | Re-arm the lock screen's blank timer from any input while locked | Pillumz | 2.1 | 1.4 | 0.94 |
| #7637 | Fix positional hotkeys for multi-surface bar widgets | konradk | 2.1 | 1.1 | 0.97 |
| #13636 | Size bar tray drawer from reveal extent while collapsed | AnPod | 2.0 | 1.4 | 0.96 |
| #12666 | shell: clamp notification toast width to viewport; battery warning auto-expires | 0xdfi | 2.0 | 1.9 | 0.95 |
| #6569 | fix(notifications): animate toast entry/exit and wake engine only on expiry | shrijit37 | 2.0 | 2.1 | 0.60 |
| #11736 | Guard qmk_hid calls with a timeout so a hung device can't stall theme switch | presidentecarter | 2.0 | 0.9 | 0.96 |
| #10343 | Don't treat pointer motion right after an output change as lock-screen activity | johnkattenhorn | 2.0 | 1.8 | 0.96 |
| #9520 | Wait for apps to flush state before powering off or rebooting | reverb256 | 2.0 | 2.0 | 0.95 |
| #11015 | Fix the bar startup stall and the shell restart race | silversword411 | 2.0 | 2.8 | 0.96 |
| #8982 | Fix/monitor scale persistence named output | 69Harold69 | 2.0 | 1.2 | 0.96 |
| #13658 | Refresh bar clock when sleep monitor restarts after resume | AnPod | 2.0 | 0.9 | 0.97 |
| #12997 | Mark the workspace each display is showing, not the focused one | fazzledev | 2.0 | 1.2 | 0.97 |
| #11162 | Flash the lock screen fingerprint icon when a read is rejected | PapeThePope | 2.0 | 1.6 | 0.72 |
| #7898 | Quote input device names before embedding them in Lua | dhh | 2.0 | 1.3 | 0.95 |
| #13725 | Fix Display panel display toggle using rejected hyprctl keyword | houz42 | 2.0 | 1.0 | 0.98 |
| #13227 | Reset keyboard layout before suspend lock | WokoFlipper | 2.0 | 0.8 | 0.98 |
| #11756 | Dim the workspace marker on unfocused monitors | jacobs852 | 2.0 | 1.0 | 0.69 |
| #10631 | Compute menu row height once per rebuild, not per append | fresh3nough | 2.0 | 1.5 | 0.93 |
| #9757 | Let on-screen keyboards reach bar panels | ekollof | 2.0 | 0.9 | 0.97 |
| #13638 | Force-clear zombie windows that ignore cooperative close | AnPod | 2.0 | 1.1 | 0.96 |
| #10146 | fix(notifications): group identical notifications the way mako did | rdjperron | 2.0 | 2.6 | 0.96 |
| #8885 | Batch window pop dispatches | yashranaway | 2.0 | 1.9 | 0.91 |
| #7146 | Disable the panel by overlay alone in clamshell recovery | mkelk | 2.0 | 2.4 | 0.93 |
| #13642 | Refresh Apps menu rows on every enter and late shell inject | AnPod | 1.9 | 1.3 | 0.95 |
| #10629 | Stop force-tiling chromium windows so tab tear-out can move | fresh3nough | 1.9 | 0.8 | 0.92 |
| #7660 | fix(keybindings): print Lua-compatible combos | ketpatil77 | 1.9 | 0.9 | 0.89 |
| #13142 | Preserve monitor position and per-output scale when scaling | f1n3d | 1.9 | 2.0 | 0.94 |
| #12857 | Don't reload a 0x0 monitor that already has video modes | suhitanantula | 1.9 | 1.2 | 0.95 |
| #8808 | Monitor scaling: honour desc: and multi-line hl.monitor rules for the internal p | iceteps | 1.9 | 1.9 | 0.95 |
| #8517 | Size popped-out windows for the active monitor | catlee | 1.9 | 1.5 | 0.63 |
| #13086 | Avoid readonly writes in command bar modules | thecdrz | 1.9 | 1.2 | 0.95 |
| #11195 | Prevent nightlight toggle race conditions and temperature oscillation (#11122) | harshithnadig | 1.9 | 1.8 | 0.97 |
| #9041 | Bind KP_Enter alongside RETURN | PyRo1121 | 1.9 | 1.5 | 0.94 |
| #6496 | Disable the laptop display while mirroring is on | DataDave-Dev | 1.9 | 1.2 | 0.97 |
| #13818 | Ignore static pointer position changes on lock screen wake (#13812) | szaidi-code | 1.9 | 1.3 | 0.97 |
| #10549 | Use Display P3 on Dell XPS OLED internal panels | j-c-m | 1.9 | 1.1 | 0.71 |
| #12093 | Paint wall-clock time as soon as the clock widget loads | paulogeyer | 1.9 | 0.8 | 0.96 |
| #12819 | Add lazy thumbnails and gate layer effects to nearby slides in background switch | sanjyay | 1.9 | 1.7 | 0.95 |
| #8135 | Open the power panel without a battery for profile controls | thecdrz | 1.9 | 1.2 | 0.94 |
| #13738 | Fall back to device connection state and live status in network bar widget | Pabl0125 | 1.9 | 1.5 | 0.96 |
| #10019 | Bound colour alias resolution in shell.toml | DanDreadless | 1.9 | 1.4 | 0.96 |
| #11136 | idle: clamp Timer intervals to avoid 32-bit overflow | leftydevkit | 1.9 | 1.2 | 0.98 |
| #10575 | Fall back to foot for Ghostty screensaver on fractional scale | fresh3nough | 1.9 | 1.2 | 0.93 |
| #13657 | Pass Super clipboard chords through to Emacs | AnPod | 1.9 | 1.1 | 0.93 |
| #10547 | Add --force to omarchy-restart-shell | codemonkey76 | 1.9 | 1.1 | 0.70 |
| #8229 | Stop the keybindings cache key flipping on menu keyboard focus | HoneyTyagii | 1.9 | 1.0 | 0.98 |
| #9508 | Simplify DaVinci Resolve window rules | sharms | 1.9 | 2.0 | 0.66 |
| #9129 | Ignore vendor hotkey keyboard devices | yashranaway | 1.9 | 1.1 | 0.96 |
| #7307 | Fit screensaver art to the monitor scale | vitalibondar | 1.9 | 1.7 | 0.88 |
| #11199 | Support QVariantList in manifestHasKind for cloned menu plugins (#11190) | harshithnadig | 1.8 | 1.8 | 0.97 |
| #8055 | Select share regions in output relative coordinates | koenhendriks | 1.8 | 1.3 | 0.96 |
| #8048 | Dismiss screensaver on pointer motion | kazeshini178 | 1.8 | 1.8 | 0.89 |
| #5514 | Fix screenshot cancel cleaning stale hyprpicker | afurm | 1.8 | 0.9 | 0.98 |
| #13662 | Prefer route-based status for the network bar icon | AnPod | 1.8 | 1.2 | 0.92 |
| #12357 | Give omacalc a centered floating size | z23 | 1.8 | 0.8 | 0.89 |
| #12091 | Do not use muted as a VS Code button fill | paulogeyer | 1.8 | 1.2 | 0.86 |
| #10490 | Scope 1Password floating geometry to main window | Drecullith | 1.8 | 1.8 | 0.89 |
| #9523 | Refocus lock screen when session secures | mlmrx | 1.8 | 1.6 | 0.95 |

## Tranche: fix-misc — 156 PRs recommended as a merge-ready roll-up

| PR | title | author | finished | effort | fix |
|---|---|---|---|---|---|
| #9344 | Keep speed tests loaded during process cleanup | ptqa | 3.0 | 1.6 | 0.96 |
| #12479 | Drop destroyed PipeWire nodes from the audio panel fallback cache | Abnersouza7 | 3.0 | 1.1 | 0.98 |
| #8076 | Stop the hybrid GPU test from failing without Omarchy installed | munzzyy | 3.0 | 0.8 | 0.97 |
| #11847 | Don't fail the locate test on non-UTF-8 files under bin/ | cristim | 2.9 | 0.8 | 0.98 |
| #9398 | Discover LUKS drives via lsblk, not blkid | fresh3nough | 2.9 | 1.0 | 0.98 |
| #7578 | Clamp idle timeouts to the int32 millisecond timer ceiling | MBemera | 2.9 | 1.1 | 0.96 |
| #13512 | Fix menu JSONC inline comment tails emptying the whole menu | buger | 2.9 | 1.2 | 0.98 |
| #11235 | Stop speedtest workers when their parent is killed | maandrij | 2.9 | 1.1 | 0.98 |
| #11177 | Show wind in m/s for Russian locales | MicahelE | 2.9 | 1.9 | 0.78 |
| #7598 | Fix orphaned network speed test workers | MBemera | 2.9 | 2.1 | 0.96 |
| #10457 | Treat app word prefixes as label prefixes in menu search | benwillems | 2.9 | 1.1 | 0.95 |
| #13127 | Walk the calendar grid from noon across midnight DST switches | anandude | 2.9 | 1.7 | 0.98 |
| #8787 | Fix lopsided cursor highlight on network panel header actions | mayaanhafeez | 2.9 | 1.0 | 0.96 |
| #13557 | Run the ShellIpc registration check without a shell | manuaudio | 2.9 | 0.9 | 0.96 |
| #9819 | Drive the launch OSD in-process so a lost close cannot strand it | Yiin | 2.9 | 1.7 | 0.95 |
| #8128 | Fix empty array shell IPC transport | llirik0 | 2.9 | 1.0 | 0.97 |
| #12386 | Report ASCII export write failures | yashranaway | 2.9 | 1.4 | 0.97 |
| #11679 | Keep living scripts off their historic siblings in Chromium fallback | anant1811 | 2.9 | 1.4 | 0.89 |
| #8165 | Give every silent test assertion a failure message | TinySkillet | 2.9 | 1.9 | 0.92 |
| #10291 | Keep the Plymouth unlock entry field on-screen for large logos | org-tekeli-borisp | 2.8 | 1.1 | 0.97 |
| #7819 | Stand down the tailscale poll watchdog once its polls exit | wico216 | 2.8 | 1.8 | 0.97 |
| #12196 | Stop speed test workers outliving a killed parent | Marjinoz | 2.8 | 1.6 | 0.98 |
| #11520 | fix(capture): single-flight screen recording stop and skip empty (#11508) | ansonboby | 2.8 | 1.4 | 0.98 |
| #11421 | Fix stale city suggestions in weather location search | richardslatter | 2.8 | 2.0 | 0.98 |
| #9042 | Run the screensaver exit handler exactly once | PyRo1121 | 2.8 | 1.1 | 0.98 |
| #7405 | Fail shell and CLI tests when ripgrep is missing | 686f6c61 | 2.8 | 1.2 | 0.96 |
| #13769 | Stop mise wrappers recursing when mise's activation variables are missing | andrew-boyd | 2.8 | 1.1 | 0.97 |
| #13742 | Test passwordless sudo revoke hook packaging | haiderakt | 2.8 | 0.6 | 0.65 |
| #12020 | Ignore bytecode and temp files in local plugin watcher | ram-devv1 | 2.8 | 1.2 | 0.97 |
| #13714 | menu-input/menu-select: reject unknown flags | kvnloo | 2.8 | 1.2 | 0.94 |
| #13751 | Walk the calendar grid at noon so a midnight DST start can't repeat a day | dhiasalhiQ | 2.8 | 1.1 | 0.97 |
| #13730 | Preserve notification images from localhost file URLs | Inference1 | 2.8 | 1.1 | 0.96 |
| #13529 | Show physical uplink in network panel with TUN proxies | LIghtJUNction | 2.8 | 1.8 | 0.95 |
| #11054 | Fix orphaned speed test traffic when the overlay is dismissed mid-run | Melcus | 2.8 | 1.7 | 0.98 |
| #13498 | Fix: omarchy plugin clone can generate a colliding plugin id | baron-hines | 2.8 | 1.2 | 0.98 |
| #13239 | Bound speedtest transfers so hung endpoints cannot strand workers | Raj-Jagadeesh-A-P | 2.8 | 1.9 | 0.97 |
| #12867 | Elide the head of the reminder typing line | anandude | 2.8 | 0.9 | 0.97 |
| #11965 | fix: use the current login shell for desktop app launches | ralphsmith80 | 2.8 | 1.5 | 0.97 |
| #11287 | Explain snapshot failures caused by regular directories | hussainanjar | 2.8 | 1.5 | 0.73 |
| #10416 | Fix cloned service lookups | imzihuailin | 2.7 | 1.6 | 0.98 |
| #7406 | Say when acceptance screenshots fail to capture | 686f6c61 | 2.7 | 1.2 | 0.96 |
| #12866 | Start speedtest measurement window on first sample | anandude | 2.7 | 1.9 | 0.98 |
| #12828 | test: avoid false failures in desktop OCR checks | jdx | 2.7 | 1.2 | 0.92 |
| #10576 | Bust plugin component URLs on hot-reload | fresh3nough | 2.7 | 1.9 | 0.98 |
| #12809 | Use popup text color for network panel popup content | sanjyay | 2.7 | 1.6 | 0.97 |
| #11014 | Recover shell restarts when the replacement launch is rejected | anovoselnik | 2.7 | 1.4 | 0.95 |
| #12457 | Escape font names before rewriting terminal and fontconfig files | cYoren | 2.7 | 1.8 | 0.97 |
| #7216 | Stub OSD calls in power tests | DatAIrchitect | 2.7 | 1.0 | 0.86 |
| #13509 | Check a clone's source before reporting it restored | yeomanse | 2.6 | 1.0 | 0.97 |
| #10634 | Coalesce concurrent shell restarts | chivopic | 2.6 | 1.3 | 0.97 |
| #13113 | Round weather coordinates to ~1 km before storing and sending | surim0n | 2.6 | 1.9 | 0.78 |
| #7653 | Keep menu empty-state text inside the card | benwillems | 2.6 | 1.6 | 0.95 |
| #13561 | Run the browser launcher test against the checkout's helpers | manuaudio | 2.6 | 0.8 | 0.94 |
| #10686 | Reuse the sleep-lock failure notification | llirik0 | 2.6 | 1.9 | 0.95 |
| #12234 | fix(nvim): relink treesitter queries orphaned by retired lazyvim package | WhiteHades | 2.6 | 1.3 | 0.98 |
| #10557 | fix: assert default-no confirmation in Hermes removal test | texasich | 2.6 | 0.8 | 0.87 |
| #9488 | Prevent clipboard capture hangs | maxcroy1 | 2.6 | 1.8 | 0.97 |
| #11730 | Rank an app above the menu actions that manage it | ivorycrayon | 2.6 | 1.1 | 0.93 |
| #13114 | Skip read-only injectProps writes for the custom command module | surim0n | 2.5 | 1.1 | 0.96 |
| #12832 | Escape notification body markup instead of only stripping image tags | taufderl | 2.5 | 1.1 | 0.92 |
| #10679 | Let reminders elapse during suspend | llirik0 | 2.5 | 1.2 | 0.97 |
| #9973 | Wrap polkit justification text instead of middle-eliding it | fresh3nough | 2.5 | 1.2 | 0.95 |
| #7491 | Show the hourglass while dictation is transcribing | Kristijan-K | 2.5 | 1.0 | 0.97 |
| #12970 | Defer tray submenu stack swaps past the click call stack | kvnloo | 2.5 | 1.4 | 0.97 |
| #9693 | Pick the matching Noto CJK variant for language-tagged text | ZacharyZhang-NY | 2.5 | 1.9 | 0.95 |
| #10680 | Stop the crash watcher from reporting its own probe | llirik0 | 2.5 | 1.1 | 0.98 |
| #7289 | capture: exclude media-controller nodes from the webcam list | danteRub | 2.5 | 1.0 | 0.97 |
| #7231 | Dispatch shell commands without a login shell | achevalier-dev | 2.5 | 1.5 | 0.76 |
| #13360 | Encode transcode clipboard file URIs | HerrStolzier | 2.5 | 1.0 | 0.96 |
| #7551 | Measure speedtest on the interface the transfer uses | Literato2 | 2.5 | 1.6 | 0.96 |
| #13221 | Load shell configuration before starting plugin discovery | sam-bee | 2.5 | 1.9 | 0.96 |
| #6471 | Hide sharee nodes from the Tailscale machines list | jmckible | 2.5 | 1.0 | 0.73 |
| #10785 | Keep menu-plugin app-library when manifests cross the panel Instantiator | ekollof | 2.5 | 1.4 | 0.97 |
| #12981 | Move plugin manifest scan into an external script | surim0n | 2.5 | 2.1 | 0.94 |
| #13141 | Wait for a slow-exiting shell before restarting it | Nejcc | 2.4 | 1.2 | 0.97 |
| #11134 | Reject disabling unknown plugin IDs in PluginRegistry | sanjyay | 2.4 | 1.4 | 0.96 |
| #12967 | Prefer weather report nearest_area over separate %l city label | kvnloo | 2.4 | 1.5 | 0.95 |
| #12021 | Escalate webcam overlay cleanup to SIGKILL and sweep on stop | ram-devv1 | 2.4 | 1.3 | 0.96 |
| #8633 | Stop network speed tests when their launcher dies | lamchun1110 | 2.4 | 2.0 | 0.96 |
| #6892 | Fix emoji paste in Firefox | VBNorebert | 2.4 | 0.8 | 0.97 |
| #13151 | Keep the Windows VM running through a guest restart | JamesStuder | 2.4 | 2.0 | 0.93 |
| #12996 | fix(shell): keep scoped APIs on cloned menu plugins (#12944) | kvnloo | 2.4 | 1.5 | 0.98 |
| #12943 | Build the clock month grid at noon so DST gaps do not repeat a day | Bartok9 | 2.4 | 1.1 | 0.96 |
| #12098 | Remember highlighted menu item after returning from submenus | Teslicek | 2.4 | 1.2 | 0.95 |
| #11285 | Give cloned menus their application library | sfk8815-create | 2.4 | 1.0 | 0.97 |
| #13681 | Parse menu JSONC with string-aware comments and object roots | AnPod | 2.4 | 1.9 | 0.94 |
| #10070 | Remove dead Qt.clearComponentCache guard from plugin reload | fresh3nough | 2.4 | 0.8 | 0.92 |
| #7188 | Honor OMARCHY_SCREENRECORD_USE_PORTAL when recording fullscreen | Literato2 | 2.4 | 1.0 | 0.95 |
| #8978 | fix(shell): report failed desktop entry launches | fgrehm | 2.4 | 1.7 | 0.92 |
| #8766 | Fix local plugin reloads | catlee | 2.3 | 2.0 | 0.96 |
| #11385 | Kill the local plugin watcher with the shell via pdeathsig | chadmandoo | 2.3 | 1.3 | 0.97 |
| #13242 | Invalidate image row cache when a file is edited in place | Raj-Jagadeesh-A-P | 2.3 | 1.1 | 0.98 |
| #13176 | Retry delay inhibit after logind OperationInProgress on resume | Bartok9 | 2.3 | 1.6 | 0.96 |
| #12966 | Do not restart launchTimeout on retriggered launches | kvnloo | 2.3 | 1.0 | 0.98 |
| #12776 | Restart media marquee once width bindings settle | D4RK0N3dev | 2.3 | 1.6 | 0.98 |
| #10715 | Stop package removal when the installed-package query fails | yashranaway | 2.3 | 1.3 | 0.97 |
| #7826 | Finish superseded menu-select requests so their waiters exit | wico216 | 2.3 | 1.8 | 0.98 |
| #12544 | Back off fingerprint lock retries on hard device errors | thabopal | 2.3 | 1.1 | 0.97 |
| #7754 | Avoid full plugin reload when discovering new plugins | sanjyay | 2.3 | 2.6 | 0.74 |
| #13340 | Encode plugin scan records as JSONL | AFOliveira | 2.3 | 2.3 | 0.76 |
| #7402 | Make stateful regression tests self-contained | mdenesfe | 2.3 | 1.7 | 0.94 |
| #13096 | Build the calendar grid cursor at noon, not midnight | surim0n | 2.3 | 1.0 | 0.97 |
| #9807 | Fix uwsm-app deadlock that stops all app launches | seanpk | 2.3 | 1.6 | 0.98 |
| #12669 | Follow symlink starting points in omarchy-menu-file | Bartok9 | 2.2 | 2.1 | 0.95 |
| #9128 | Detect browser families without launching them | yashranaway | 2.2 | 1.5 | 0.95 |
| #12985 | Fix clock calendar grid shifting a day after a spring-forward DST transition | gtf-inet | 2.2 | 0.9 | 0.98 |
| #11079 | Keep plugin shell facades alive and intact for live consumers | joniler | 2.2 | 1.6 | 0.94 |
| #9013 | fix: address high-confidence shellcheck findings | fgrehm | 2.2 | 1.8 | 0.91 |
| #12983 | Add signal fallback to omarchy-restart-shell for IPC-wedged shells | surim0n | 2.2 | 1.9 | 0.96 |
| #12471 | Fix recording indicator stuck 'active' after a force-killed stop | ReneXiong | 2.2 | 1.4 | 0.98 |
| #8692 | Resolve mise wrapper binaries before execution | imadtg | 2.2 | 1.7 | 0.97 |
| #8570 | Focus existing windows after no-op app launches | npenza | 2.2 | 1.4 | 0.90 |
| #8269 | Skip cross-repository checks without sibling repos | gouveags | 2.2 | 1.7 | 0.92 |
| #11569 | Skip Electron utility subprocess crashes in crash-watch | Bartok9 | 2.2 | 1.1 | 0.95 |
| #9551 | Detect fingerprint enrollment by the enrolled entries, not the word "finger" | kahlin | 2.2 | 1.1 | 0.96 |
| #9161 | Discover and normalize web app icons | DerpyCrabs | 2.2 | 1.9 | 0.79 |
| #11925 | fix(shell): keep __sourceDir on third-party plugin manifests | joewinke | 2.1 | 1.0 | 0.98 |
| #10705 | Coalesce plugin reloads and exclude .git from inotify | gw7523 | 2.1 | 1.6 | 0.92 |
| #9903 | Show useful app details in menu search | MansTomb | 2.1 | 1.1 | 0.65 |
| #12969 | Match fontconfig monospace override on first family only | kvnloo | 2.1 | 1.1 | 0.91 |
| #12697 | Preserve configured cursors for screenshots on transformed displays | DiegoYegros | 2.1 | 1.8 | 0.83 |
| #7189 | Report screen recordings that fail to start | Literato2 | 2.1 | 0.9 | 0.94 |
| #13819 | Bound fingerprint retry attempts with exponential backoff (#13748) | szaidi-code | 2.1 | 1.9 | 0.97 |
| #13547 | omarchy-refresh-config shouldn't override symlinked file content | omarchybot | 2.1 | 1.7 | 0.96 |
| #11302 | Fix network status and latency on IPv6-only links | emanueleadelini | 2.1 | 2.3 | 0.94 |
| #9641 | Use universal paste for Voxtype output | komagata | 2.1 | 2.2 | 0.72 |
| #12575 | Stub omarchy-osd in the system power test | davidboulay | 2.1 | 0.9 | 0.93 |
| #11092 | Pin recording audio sample rate at 48 kHz | sandmor | 2.1 | 0.5 | 0.97 |
| #8734 | Share Voxtype status across bar surfaces | lamchun1110 | 2.1 | 2.8 | 0.72 |
| #7332 | Scroll the Tailscale machine list independently of the panel | andrepadez | 2.1 | 1.3 | 0.72 |
| #8896 | Debounce unforced lock wake calls immediately following display blanking | Sword-Saint69 | 2.0 | 1.3 | 0.97 |
| #13018 | Fix #12665: omarchy-menu-file returns 0 files when ~/Pictures/~/Videos are symli | yashbijlani | 2.0 | 1.2 | 0.98 |
| #13063 | fix: report panel plugin load failures instead of throwing | BernhardRode | 2.0 | 0.9 | 0.98 |
| #12261 | Recover polkit agent registration when a stale listener blocks pkexec | Chessing234 | 2.0 | 1.9 | 0.95 |
| #11606 | Stop a web app's generated .desktop id from leaking into app search | brenoperucchi | 2.0 | 1.6 | 0.95 |
| #7309 | fix: always use sed -i --follow-symlinks to preserve symlinks | calebdw | 2.0 | 1.9 | 0.94 |
| #13194 | Let bar-entry plugin shells resolve their entry's own service | TMartinPPC | 2.0 | 2.2 | 0.95 |
| #7447 | sleep-monitor: resolve dbus-monitor by absolute path to avoid PATH shadowing | tahadx | 2.0 | 0.9 | 0.97 |
| #13782 | Retry a sleep inhibitor rejected while logind is still transitioning | Bartok9 | 2.0 | 1.1 | 0.96 |
| #12406 | Replace eval with quote-aware word split in omarchy-launch-or-focus | dhh | 2.0 | 2.1 | 0.90 |
| #12964 | Honor critical notification expireTimeout when sender requests one | kvnloo | 1.9 | 1.1 | 0.96 |
| #12559 | Give screen recording stop more than five seconds to mux | Bartok9 | 1.9 | 1.2 | 0.93 |
| #10632 | Size ConfirmDialog buttons to their labels | fresh3nough | 1.9 | 1.4 | 0.95 |
| #8792 | Fix webcam MJPEG negotiation for screen recordings | ottosilva | 1.9 | 1.4 | 0.96 |
| #13012 | Restore menu selection when navigating back | onurersel | 1.9 | 1.7 | 0.90 |
| #12795 | Name the catppuccin flavour LazyVim loads instead of the plugin entrypoint | ayandexyz | 1.9 | 0.3 | 0.95 |
| #8573 | Fix Emoji Picker for all apps with both keyboard and mouse | axelfontaine | 1.9 | 2.3 | 0.97 |
| #13095 | Keep the launch OSD timeout from being restarted indefinitely | surim0n | 1.9 | 1.6 | 0.94 |
| #10510 | Tailscale panel: label exit nodes with their MagicDNS name | ssandys | 1.9 | 1.1 | 0.81 |
| #12892 | Remove dead CommonJS module.exports guards from shell JS modules | Only1allan | 1.8 | 2.2 | 0.88 |
| #10253 | Bound network speed test runtime | arisgysel-design | 1.8 | 1.5 | 0.94 |
| #6739 | Keep Windows running when RDP fails | yashranaway | 1.8 | 1.1 | 0.94 |
| #12361 | Check the weather hook's exit status, not its message | linyiru | 1.8 | 1.0 | 0.87 |
| #11338 | Withdraw the toast when the server closes its notification | xmagma-x | 1.8 | 1.5 | 0.98 |
| #7144 | Window VM start then stop, add retry mechanism for RDP connection | phamdung196 | 1.8 | 1.3 | 0.92 |
| #8277 | Auto-detect weather units from the configured location's country | Jhon-opt | 1.8 | 2.0 | 0.89 |

## Tranche: hardware-drivers — 111 PRs recommended as a merge-ready roll-up

| PR | title | author | finished | effort | fix |
|---|---|---|---|---|---|
| #7745 | Keep Spotify volume across track changes | sdye1337 | 3.0 | 1.3 | 0.97 |
| #9482 | Count GPUs without waking the one that is asleep | VykosMolt | 2.9 | 1.8 | 0.92 |
| #13744 | Detect NEXT Biometrics readers as fingerprint hardware | lovecamera68-ai | 2.9 | 0.6 | 0.95 |
| #11836 | Skip screen digitizers when detecting the touchpad | Per0-1 | 2.9 | 1.1 | 0.94 |
| #8205 | Read actual gmux display brightness | piotrsynowiec | 2.9 | 1.2 | 0.94 |
| #13711 | Require the pattern argument in omarchy-hw-match | kvnloo | 2.9 | 1.0 | 0.97 |
| #10458 | Enable speakers on Late 2015 21.5-inch iMacs | inspiretelapps | 2.9 | 1.8 | 0.80 |
| #10844 | Close Bluetooth panel after connecting | sergedoub | 2.9 | 1.0 | 0.87 |
| #9883 | Keep low-battery latch across AC online flaps | fresh3nough | 2.9 | 1.1 | 0.98 |
| #12387 | Detect the Chipsailing CS9711 USB reader | yashranaway | 2.8 | 1.1 | 0.94 |
| #9400 | Keep discovery from moving a Bluetooth row out from under the pointer | VykosMolt | 2.8 | 1.7 | 0.96 |
| #7308 | Keep jack names on multi-port audio devices | sunblot | 2.8 | 1.1 | 0.92 |
| #12634 | Wake displays before restoring keyboard and clamshell state | RenanBezerraGuima | 2.8 | 1.5 | 0.79 |
| #8317 | Show UPower device batteries in Bluetooth panel | erbmicha | 2.8 | 2.0 | 0.70 |
| #6548 | Fix audio device labels and guard seamless output switching | HANCORE-linux | 2.8 | 1.9 | 0.94 |
| #13373 | Keep UVC webcams at a fixed frame rate | phil-bowens | 2.8 | 1.1 | 0.82 |
| #11516 | Ignore USB Touch Bar DRM when detecting external displays | hanscnelson | 2.8 | 1.2 | 0.96 |
| #8329 | Detect ROG machines reporting sys_vendor as "ASUS" | ianleon | 2.8 | 0.9 | 0.97 |
| #13111 | Fall back to UPower when the sysfs battery rate is implausible | surim0n | 2.8 | 1.2 | 0.97 |
| #12785 | fix: correct Khadas Mind Graphics Speaker volume mapping | hyf4053 | 2.8 | 1.0 | 0.98 |
| #11228 | Document Dell XPS 13 silent speaker recovery | Jdelg718 | 2.8 | 1.4 | 0.63 |
| #10003 | Keep bluetooth panel visible after user powers it off | fresh3nough | 2.8 | 1.4 | 0.95 |
| #7459 | Initialize the analog playback path for any ASUS ROG Realtek codec | nitine | 2.8 | 1.9 | 0.94 |
| #11675 | Keep Activity from waking a runtime-suspended NVIDIA GPU | anant1811 | 2.8 | 1.7 | 0.94 |
| #11592 | Fix legacy Intel VA-API driver detection | aladh | 2.8 | 1.4 | 0.97 |
| #11076 | Disable broken eDP Panel Replay on Dell XPS Panther Lake | joniler | 2.8 | 0.9 | 0.90 |
| #7880 | Don't treat Bluetooth Trusted as a completed pairing | reinierbutot | 2.8 | 1.7 | 0.97 |
| #12863 | Retry Bluetooth pairing once on failure | nixfred | 2.7 | 1.0 | 0.95 |
| #12300 | Fix fronted sink detection for community speaker tunings | shmlkv | 2.7 | 1.7 | 0.97 |
| #9612 | omarchy #9586 sysfs battery thresholds | kvnloo | 2.7 | 1.5 | 0.88 |
| #11917 | Keep the Micron 2400 NVMe SSD out of its APST power states | Sraleik | 2.7 | 0.6 | 0.90 |
| #10455 | Wait out an in-flight sleep operation before inhibiting | codemonkey76 | 2.7 | 1.2 | 0.94 |
| #12175 | Move only application streams when switching the audio input | HazAT | 2.7 | 1.0 | 0.96 |
| #10125 | Avoid Baffin GPU hangs during screen recording | andrewrbrady | 2.7 | 1.6 | 0.97 |
| #13396 | Resolve the audio output sink through EasyEffects 8 | stefanoverna | 2.6 | 1.8 | 0.96 |
| #11835 | fix: toggle every touchscreen digitizer | Per0-1 | 2.6 | 1.9 | 0.98 |
| #10076 | Prefer kernel charge registers for battery percentage | ludagoo | 2.6 | 2.2 | 0.77 |
| #9716 | Disable WebKitGTK DMA-BUF renderer on NVIDIA | vltic | 2.6 | 0.9 | 0.87 |
| #7779 | Hide Hibernate when the kernel will not accept the request | omarchybot | 2.6 | 1.2 | 0.95 |
| #8426 | Fix missing HDMI/DP audio on Intel Kabylake HDMI + Conexant systems | OmarGonD | 2.6 | 0.9 | 0.96 |
| #11260 | Pause Bluetooth discovery during pairing | itsMattGuenther | 2.6 | 1.9 | 0.95 |
| #7186 | Report combined dual-battery status in the power panel | unleashed-nick | 2.6 | 2.4 | 0.91 |
| #12504 | Skip force-igpu Vfio dance when no NVIDIA GPU is present | paulogeyer | 2.5 | 1.0 | 0.96 |
| #12585 | Keep the Bluetooth widget on the bar while the radio is off | selfcrypto | 2.5 | 1.7 | 0.97 |
| #11937 | Restart Bluetooth agent when BlueZ is replaced | n0mahd | 2.5 | 2.1 | 0.94 |
| #9553 | Fix per-app stream sliders ignoring pointer input | shaynhornik | 2.5 | 1.0 | 0.98 |
| #13600 | Reset elan_i2c trackpads and fail clearly when none match | AnPod | 2.5 | 1.4 | 0.96 |
| #8947 | Set GDK_GL=gles on NVIDIA so GTK3 video playback works | danielgccr | 2.5 | 0.7 | 0.97 |
| #10191 | Prefer the live device name when labeling Bluetooth devices | njos-444-navelin | 2.5 | 1.0 | 0.94 |
| #7336 | Re-detect Apple display when cached hiddev node stops responding | 0xApotheosis | 2.5 | 1.3 | 0.97 |
| #13189 | Force software video decode in Chromium on NVIDIA GPUs with GSP firmware | jampick | 2.5 | 1.2 | 0.95 |
| #13016 | Derive power panel charge direction from settled battery state | jaderfeijo | 2.5 | 1.7 | 0.97 |
| #8712 | Skip powerprofilesctl when daemon is down | Elshayib | 2.4 | 1.9 | 0.96 |
| #11785 | Serialize repeating volume adjustments | Yiteng-CHEN | 2.4 | 1.8 | 0.92 |
| #9755 | Refresh monitor brightness state every second | iccodes | 2.4 | 0.8 | 0.93 |
| #9638 | Switch Bluetooth headsets to HFP when selecting their input | fresh3nough | 2.4 | 1.6 | 0.95 |
| #7948 | Stop the DMI chassis fallback in omarchy-hw-laptop reading an empty string | chubuntuarc | 2.3 | 1.0 | 0.97 |
| #9524 | Detect Broadcom ControlVault 3 fingerprint readers | qybaihe | 2.3 | 1.2 | 0.79 |
| #12769 | Handle low-resolution brightness deltas safely | sonique6784 | 2.3 | 1.8 | 0.96 |
| #9132 | Resolve native EasyEffects output chains | yashranaway | 2.3 | 1.9 | 0.96 |
| #12842 | fix(audio): resolve the fronted sink from the running graph, not only from a shi | sneemgp | 2.3 | 1.2 | 0.97 |
| #6849 | Fix jittery scrolling on Dell XPS 13 Wildcat Lake by disabling PSR and Panel Rep | zoan37 | 2.3 | 1.1 | 0.97 |
| #10364 | Preserve keyboard backlight across repeated blanks | catlee | 2.2 | 1.5 | 0.96 |
| #12241 | Keep bluetooth bar icon visible after adapter disappears | RushiChaganti | 2.2 | 1.1 | 0.91 |
| #12231 | List local audio outputs before network ones in the audio panel | mike-echo-oscar-whiskey | 2.2 | 1.7 | 0.65 |
| #9637 | Restore brightness when the laptop lid opens | fresh3nough | 2.2 | 1.3 | 0.96 |
| #13099 | Write output volume through pactl, not the node-bound setter | surim0n | 2.2 | 1.1 | 0.97 |
| #13680 | Center network Forget control and add Cancel while connecting | AnPod | 2.2 | 1.7 | 0.63 |
| #8017 | Hibernate with shutdown mode on ThinkBook X IMH so the machine powers off | tuthan | 2.2 | 1.1 | 0.89 |
| #11415 | Dismiss stale low battery warnings | gaburn | 2.2 | 1.3 | 0.96 |
| #9483 | Only point the session at NVIDIA when NVIDIA is driving the screen | VykosMolt | 2.2 | 1.4 | 0.79 |
| #13598 | Back off bt-agent restarts while a device flaps | AnPod | 2.2 | 1.4 | 0.96 |
| #9997 | bluetooth: surface passkey prompt during device pairing | Johann-S | 2.2 | 1.1 | 0.88 |
| #13199 | Clean up legacy NVIDIA driver overrides during upgrades | ryanrhughes | 2.1 | 1.8 | 0.86 |
| #12950 | Keep Bluetooth USB controllers awake when TLP manages USB power | s-gato | 2.1 | 1.2 | 0.88 |
| #11312 | Software brightness fallback when DRM backlight is missing | Infringer13 | 2.1 | 2.3 | 0.66 |
| #8284 | Delay the first low-battery check until UPower settles | thecdrz | 2.1 | 0.9 | 0.96 |
| #10501 | Keep Bluetooth device actions on the panel adapter | Drecullith | 2.1 | 2.1 | 0.93 |
| #7915 | Treat pending-charge as a hold only inside a real charge limit | tahadx | 2.1 | 2.0 | 0.93 |
| #6388 | Fix ASUS ExpertBook B9406 touchpad quirk never being applied | dhh | 2.1 | 1.5 | 0.97 |
| #13639 | Pin Voxtype capture to the Asahi mic map on Apple Silicon | AnPod | 2.0 | 1.8 | 0.94 |
| #9218 | Detect Apple bcm5974 trackpads in omarchy-hw-touchpad | DeanWahle | 2.0 | 0.5 | 0.97 |
| #10366 | Fix keyboard backlight restore after screensaver dismiss | marcindyguda | 2.0 | 1.7 | 0.98 |
| #8221 | Reference count the Wi-Fi scanner so a closed panel cannot scan | xraid | 2.0 | 2.7 | 0.98 |
| #10148 | Use software volume for Audient USB audio interfaces | kmpeeduwee | 2.0 | 1.5 | 0.87 |
| #8226 | Stop one speaker dropping out on the Dell XPS 14 | hartct | 2.0 | 1.2 | 0.93 |
| #10196 | Require a real charge threshold before reporting a held charge | gabamnml | 2.0 | 1.8 | 0.97 |
| #7196 | Lock the lid and idle the Radeon on 15-inch 2016–2017 MacBook Pros | shawnyeager | 2.0 | 2.1 | 0.72 |
| #5193 | fix(hardware): add Alienware Area-51 iwd boot-delay workaround | long-island | 2.0 | 0.9 | 0.97 |
| #13622 | Bound Bluetooth discoveryRetry StartDiscovery attempts | AnPod | 2.0 | 1.4 | 0.97 |
| #10926 | fix(systemd): rebind ASUS touchpad after s2idle resume | ottosilva | 2.0 | 0.9 | 0.97 |
| #8524 | Fix brightness lockout on displays with small max_brightness ranges | gorem | 2.0 | 1.4 | 0.98 |
| #10320 | Drop a Bluetooth power change that lands mid-transition | dontm1nd | 1.9 | 2.1 | 0.95 |
| #12696 | Fall back to the kernel HID battery when BlueZ reports none | EttienneM | 1.9 | 1.6 | 0.92 |
| #12484 | Report an unavailable battery cycle count as unknown | mateuseap | 1.9 | 1.8 | 0.96 |
| #7965 | Gate low-battery warn and sleep on live remaining energy | hilather | 1.9 | 2.5 | 0.88 |
| #7329 | Re-detect external displays that no hotplug brought back after resume | paracycle | 1.9 | 2.2 | 0.96 |
| #13655 | Allow Bluetooth bar toggle when adapter is rfkill-blocked | AnPod | 1.9 | 1.2 | 0.96 |
| #10071 | Dedupe sound menu output and input entries | fresh3nough | 1.9 | 1.9 | 0.91 |
| #13659 | Only export NVIDIA env when NVIDIA drives a display | AnPod | 1.9 | 1.4 | 0.96 |
| #11831 | Disable PSR2 selective fetch on the Dell Latitude 9440 2-in-1 | pelifix | 1.9 | 0.9 | 0.77 |
| #11387 | Detect FocalTech match-on-chip fingerprint readers | alanwcurry-dev | 1.9 | 1.2 | 0.95 |
| #12953 | Detect Realtek USB Finger Print readers (2541) | Chessing234 | 1.9 | 1.3 | 0.95 |
| #10485 | Send Broadcom's ACL-priority command to fix Bluetooth A2DP stutter on T2 Macs | csk-grit42 | 1.9 | 1.7 | 0.89 |
| #9131 | Wait for Bluetooth before starting its agent | yashranaway | 1.9 | 1.0 | 0.96 |
| #12671 | omarchy-hibernation-available: return failure when the kernel will refuse to hib | juan-LARRAYA | 1.9 | 1.8 | 0.96 |
| #8713 | Resolve through EasyEffects to its configured output device | tzssangglass | 1.9 | 2.0 | 0.95 |
| #13292 | Fix battery status reading a phantom BAT device on dual-bay ThinkPads | andreyse | 1.9 | 1.9 | 0.98 |
| #13797 | Smooth out battery time | shawnyeager | 1.9 | 1.6 | 0.92 |
| #9370 | Prefer nvidia_wmi_ec_backlight over cosmetic nvidia_0 | megascan | 1.8 | 1.3 | 0.87 |
| #8227 | feat(asus): follow GZ302 keyboard backlight on the chassis window LED | JustNak | 1.8 | 2.5 | 0.60 |

## Tranche: shell-cli — 62 PRs recommended as a merge-ready roll-up

| PR | title | author | finished | effort | fix |
|---|---|---|---|---|---|
| #12138 | Keep both coordinates when wttr.in auto-detects a location as lat,lon | SirJul1337 | 3.0 | 1.0 | 0.98 |
| #7370 | Fire the restart-terminal toast after a font change | 686f6c61 | 3.0 | 0.6 | 0.98 |
| #13712 | dev font add: require --codepoint in the private-use range | kvnloo | 2.9 | 1.1 | 0.96 |
| #8084 | Leave the alternate screen only when the connection dropped | eng1n88r | 2.9 | 1.1 | 0.97 |
| #11742 | Coerce omarchy-show-done exit code to numeric before arithmetic test | foxxmo51 | 2.9 | 1.1 | 0.97 |
| #9977 | Keep wttr coordinate fallbacks intact in weather location | fresh3nough | 2.9 | 0.9 | 0.97 |
| #12841 | Fix omarchy-launch-browser crashing Chrome when man-db is absent | AyanMulla09 | 2.9 | 1.1 | 0.98 |
| #8941 | Add omarchy-ascii so stable matches the published branding manual | fresh3nough | 2.9 | 2.0 | 0.86 |
| #11670 | Render git ahead/behind counts in the starship prompt | anant1811 | 2.9 | 0.9 | 0.96 |
| #7365 | Stop advertising empty command groups in omarchy --help | 686f6c61 | 2.9 | 1.1 | 0.96 |
| #9425 | Keep four commands from building a path that climbs out of its directory | VykosMolt | 2.9 | 1.9 | 0.96 |
| #8597 | Preserve alacritty font styles when changing font family | ParadokS81 | 2.9 | 1.0 | 0.98 |
| #12456 | Quote OMARCHY_PATH in the function loader glob | cYoren | 2.8 | 0.9 | 0.98 |
| #12364 | Only restart the shell after Voxtype configure if the config changed | Yacl222 | 2.8 | 1.0 | 0.87 |
| #12992 | fix(shell): keep last valid shell.json when the file truncates (#12990) | kvnloo | 2.8 | 1.2 | 0.98 |
| #9583 | Exec mise wrappers by resolved path, not by name | mrdavidlaing | 2.8 | 1.6 | 0.96 |
| #7366 | Stop cloning plugins into the reserved omarchy.* namespace | 686f6c61 | 2.8 | 1.0 | 0.97 |
| #13446 | Add the Ctrl+Shift clipboard chords to older foot configs | stevederico | 2.8 | 1.3 | 0.89 |
| #12600 | font-set: actually show the terminal restart notification | llkkk | 2.7 | 1.4 | 0.98 |
| #7387 | plugin cli: force LC_ALL=C so plugin ids validate under any locale | jjanis | 2.7 | 1.2 | 0.97 |
| #11484 | Preserve custom launchers when installing mise wrappers | yashranaway | 2.7 | 1.8 | 0.93 |
| #11205 | Fix default tmux splits to preserve the current directory | SamRoehrich | 2.7 | 0.9 | 0.74 |
| #12837 | Fix tab completion for typed omarchy-* commands | Zelmari | 2.6 | 0.9 | 0.97 |
| #12670 | omarchy-font-set: fire terminal-restart notifications and stop leaking PIDs (#12 | juan-LARRAYA | 2.6 | 1.7 | 0.98 |
| #13706 | Avoid sentence-ending periods in clipboard links | Inference1 | 2.6 | 1.1 | 0.95 |
| #10095 | Add live-screen fallback for capture tools | nixfred | 2.6 | 2.1 | 0.86 |
| #10259 | Report Custom DNS when public resolvers are only secondary | fresh3nough | 2.6 | 1.1 | 0.96 |
| #11482 | Preserve presentation command exit status | yashranaway | 2.6 | 1.2 | 0.94 |
| #7235 | Don't let a failed self-update abort a working mise-wrapped tool | pedrosekine | 2.5 | 0.9 | 0.91 |
| #7796 | Drop stale group descriptions from CLI router | Shaivarth | 2.5 | 0.8 | 0.88 |
| #13720 | group listing: describe the visible share/show/upgrade groups | kvnloo | 2.5 | 0.8 | 0.78 |
| #9912 | Handle package groups in omarchy pkg add | suvikyi | 2.4 | 1.5 | 0.90 |
| #7338 | Remove redundant tmux escape-time setting | thomasdoan | 2.4 | 0.3 | 0.67 |
| #6839 | Show errors from the open helper | yashranaway | 2.4 | 1.0 | 0.94 |
| #13614 | Guard mise stubs against PATH recursion when a tool is missing | AnPod | 2.4 | 2.1 | 0.96 |
| #10716 | Keep drive selector arguments on separate rows | yashranaway | 2.4 | 1.0 | 0.93 |
| #13116 | Only leave the alternate screen after SSH when it is still on | fbritoferreira | 2.4 | 1.5 | 0.97 |
| #13716 | restart-app: require the application name | kvnloo | 2.3 | 1.0 | 0.92 |
| #9040 | Hand the presentation terminal Omarchy's BROWSER default | PyRo1121 | 2.3 | 1.0 | 0.96 |
| #10847 | fix: clamp omarchy commands table to terminal width | harlanljones | 2.3 | 1.0 | 0.93 |
| #6761 | Keep tmux clipboard copies working over mosh | yashranaway | 2.3 | 2.5 | 0.95 |
| #13715 | brightness-keyboard: reject unknown directions before touching hardware | kvnloo | 2.2 | 1.1 | 0.96 |
| #9503 | Keep the sudo editor on one that blocks | d-zalewski | 2.2 | 1.2 | 0.94 |
| #11853 | Cover omarchy debug dispatch in CLI tests | rishabhiskawai | 2.2 | 0.6 | 0.82 |
| #11117 | Make the closing plugin rescan best-effort | Mario-Mohar | 2.2 | 1.3 | 0.96 |
| #8866 | Fix network panel behind VPN policy routes | hehh2001 | 2.2 | 1.7 | 0.95 |
| #10864 | Restore Ghostty's default scroll speed for discrete mouse wheels | dimenus | 2.2 | 0.7 | 0.93 |
| #12644 | Return the menu cursor to the entered row when going back | kmpeeduwee | 2.1 | 1.4 | 0.94 |
| #13107 | Fall back to Cloudflare endpoints when api.fast.com is unreachable | surim0n | 2.1 | 2.0 | 0.79 |
| #11962 | Keep alias and id separators searchable in the menu | a-kar | 2.1 | 1.1 | 0.97 |
| #8880 | Report the selected terminal font size | yashranaway | 2.1 | 1.2 | 0.94 |
| #8796 | windows-vm: negotiate RDP with /sec:tls by default | joeldeteves | 2.1 | 1.0 | 0.76 |
| #8630 | Wait longer for a restarted shell to become ready | lamchun1110 | 2.1 | 1.2 | 0.94 |
| #9164 | Default OMARCHY_PATH in channel-current and audio-tuning; add env-robustness tes | kfchai | 2.1 | 1.2 | 0.93 |
| #6963 | Remove unsafe Ghostty epoll workaround | stappmus | 2.0 | 1.5 | 0.90 |
| #9487 | Stop omarchy-restart-terminal silently no-opping for foot | perryqh | 2.0 | 1.5 | 0.93 |
| #8927 | Anchor dip and lip matches on the ssh binary | Chessing234 | 2.0 | 0.9 | 0.94 |
| #9039 | Validate pane counts before creating layouts | PyRo1121 | 1.9 | 1.0 | 0.96 |
| #13197 | Follow symlink dirs in omarchy-menu-file | Bartok9 | 1.9 | 1.6 | 0.96 |
| #13678 | Only claim Restored when plugin remove re-enables the source | AnPod | 1.9 | 1.0 | 0.96 |
| #8466 | Report Omarchy dev-link session state accurately | Skeptomenos | 1.8 | 1.8 | 0.92 |
| #12063 | Only leave the alternate screen after a session that actually dropped | AronBakes | 1.8 | 1.1 | 0.97 |

## Tranche: apps-integrations — 53 PRs recommended as a merge-ready roll-up

| PR | title | author | finished | effort | fix |
|---|---|---|---|---|---|
| #7778 | Remove GeForce NOW launcher leftovers on uninstall | husamemadH | 3.0 | 1.2 | 0.97 |
| #13123 | Default image opens to imv-dir for folder navigation | anandude | 3.0 | 1.2 | 0.79 |
| #9365 | Fail terminal install before rewriting the default | fresh3nough | 2.9 | 1.4 | 0.98 |
| #9364 | Label Tailscale profiles by tailnet, not nickname | fresh3nough | 2.9 | 1.0 | 0.97 |
| #8379 | Use the real game title for RetroArch launchers installed from arcade ROMs | axelfontaine | 2.9 | 1.8 | 0.77 |
| #7356 | Detect the tailscale CLI without the which package | anupanup2001 | 2.9 | 0.9 | 0.97 |
| #13710 | Refuse to launch when no default browser is configured | kvnloo | 2.9 | 1.1 | 0.97 |
| #12533 | Resolve wrapped desktop Exec= in browser and webapp launchers | paulogeyer | 2.9 | 1.6 | 0.97 |
| #9431 | Read the default browser once, and recognise one that registered itself | VykosMolt | 2.9 | 1.9 | 0.88 |
| #11344 | Support both zed and zeditor editor binaries | rand0mdud3 | 2.8 | 1.9 | 0.77 |
| #5934 | omarchy-webapp-install: set StartupWMClass so app switchers find the icon | andyjeffries | 2.8 | 0.8 | 0.94 |
| #11955 | Keep the Dropbox panel polling until the account link completes | procrypto | 2.8 | 2.1 | 0.92 |
| #13858 | Hide Hermes' renamed CLI launcher from Apps | manuaudio | 2.8 | 0.5 | 0.97 |
| #12801 | Explicitly set text/plain UTF-8 MIME type in omarchy-clipboard-paste-text | sanjyay | 2.8 | 1.0 | 0.97 |
| #11998 | fix: type image path when pasting clipboard images into terminals | HIMANSHU11827 | 2.7 | 1.1 | 0.97 |
| #12988 | Stop dropbox-cli status polling while Dropbox is unlinked | surim0n | 2.7 | 1.2 | 0.98 |
| #9449 | Read the default terminal back from the file that sets it | VykosMolt | 2.6 | 1.7 | 0.93 |
| #8299 | Launch Opera webapps as a tab URL instead of --app= | Ojisan1 | 2.6 | 1.1 | 0.96 |
| #11758 | Enable native Wayland rendering for Spotify | RVPick | 2.6 | 1.9 | 0.76 |
| #8343 | Fix omarchy share clipboard sending an empty file for image clipboard content | dima-engineer | 2.6 | 1.7 | 0.98 |
| #7599 | Convert downloaded web app icons to PNG | pjgeutjens | 2.5 | 2.1 | 0.91 |
| #12974 | Stop Dropbox panel inventing quota from plan name | kvnloo | 2.5 | 1.3 | 0.96 |
| #10567 | Match the class the standalone Battle.net install produces | pmbemax | 2.5 | 0.8 | 0.93 |
| #10513 | Drop browser codec preloads from yt-dlp host | Drecullith | 2.5 | 1.0 | 0.97 |
| #8932 | Tile the Battle.net client instead of floating it | michielvandermeer | 2.5 | 2.0 | 0.89 |
| #8533 | fix(tailscale): isolate claim path argument | ketpatil77 | 2.5 | 0.9 | 0.95 |
| #9927 | Avoid focusing Quickshell plugin windows | imzihuailin | 2.4 | 1.8 | 0.92 |
| #7797 | Add Remove > 1Password to the shell menu | Shaivarth | 2.4 | 0.8 | 0.71 |
| #8761 | Keep mailto parameters out of HEY's recipient | tony-roslund | 2.4 | 1.1 | 0.97 |
| #13843 | Provision Helix theme links for existing installations | Susensio | 2.4 | 1.6 | 0.83 |
| #8879 | Use Sunshine's packaged systemd unit | yashranaway | 2.3 | 0.9 | 0.97 |
| #11631 | Open web app links in the default browser | tumbleweedlabs | 2.3 | 2.2 | 0.71 |
| #7886 | Detach 1Password from the installer terminal | kx0101 | 2.3 | 1.3 | 0.92 |
| #12256 | Probe Tailscale with omarchy-cmd-present instead of which | z23 | 2.2 | 0.8 | 0.97 |
| #8153 | Repair Copy URL after install-time migration stamping | Chessing234 | 2.2 | 2.1 | 0.97 |
| #12148 | Point Zen's policy at the directory the package uses | JoshJAL | 2.2 | 1.3 | 0.96 |
| #6333 | Prevent Chromium Vulkan crashes on Wayland | a-b | 2.1 | 1.6 | 0.89 |
| #13830 | Read the default browser without xdg-settings | hegjon | 2.1 | 1.9 | 0.87 |
| #12834 | Stop web app launches from disabling TLS for the whole browser session | taufderl | 2.1 | 2.0 | 0.93 |
| #9621 | Set StartupWMClass on Chromium web app launchers | seanpk | 2.1 | 1.2 | 0.80 |
| #11393 | Use a generic icon when webapp favicon lookup fails | nicknack5050 | 2.1 | 1.8 | 0.60 |
| #8383 | Fix Dropbox panel pause/resume snapping back to the wrong state | ryanyogan | 2.1 | 2.2 | 0.98 |
| #12368 | fix(imv): open AVIF, HEIF, and JXL files | lukehsiao | 2.0 | 1.1 | 0.94 |
| #11706 | Show this machine in the Tailscale machines list | elpargo | 2.0 | 1.6 | 0.71 |
| #13619 | Refuse a second Battle.net launch while one is already running | AnPod | 2.0 | 1.4 | 0.93 |
| #7039 | Support Firefox as a web app browser | alkevintan | 2.0 | 1.5 | 0.82 |
| #9891 | Stop previewing received Taildrop images | rcssdy | 2.0 | 1.1 | 0.95 |
| #13685 | Fix Obsidian Electron flags and float Mullvad VPN | AnPod | 1.9 | 1.6 | 0.89 |
| #10370 | Install ffmpeg 4.4 with Spotify so Local Files can play | cempack | 1.9 | 1.2 | 0.91 |
| #9206 | Warn clearly when no Chromium browser can launch a web app | linuts | 1.9 | 1.8 | 0.96 |
| #13354 | Refuse to stack another Battle.net Proton tree | Bartok9 | 1.9 | 1.7 | 0.94 |
| #9191 | Dropbox widget: scan the team root, not the member folder | renerocksai | 1.8 | 0.9 | 0.97 |
| #12786 | Follow an opened link to the browser window, never an open web app | legendik | 1.8 | 1.3 | 0.96 |

## Tranche: agents-ai — 45 PRs recommended as a merge-ready roll-up

| PR | title | author | finished | effort | fix |
|---|---|---|---|---|---|
| #13209 | fix(agents): count pi sessions when HOME is a git checkout | kvnloo | 2.9 | 0.7 | 0.98 |
| #12979 | Fix Codex usage timeouts on batched replies | orienw | 2.9 | 2.3 | 0.98 |
| #13458 | Raise Codex usage RPC timeout from 4s to 10s | AnPod | 2.9 | 0.3 | 0.95 |
| #13464 | Make Codex account/read optional in the usage collector | AnPod | 2.9 | 1.3 | 0.94 |
| #7924 | Fix Codex usage collector's stale --ask-for-approval value | iaikanshb | 2.9 | 0.3 | 0.98 |
| #13102 | Read codex app-server replies unbuffered in the usage collector | surim0n | 2.8 | 2.0 | 0.97 |
| #8254 | Defeat mise's release cooldown when selecting the default agent | yashksaini-coder | 2.7 | 0.5 | 0.97 |
| #8004 | Stop killing running opencode sessions when changing themes | ADIBAINS | 2.7 | 0.9 | 0.95 |
| #10606 | Count streamed Claude messages by their highest-output usage line | st-eez | 2.7 | 1.3 | 0.97 |
| #13059 | Describe Codex rate-limit RPC timeouts instead of the method name | Bartok9 | 2.7 | 1.0 | 0.93 |
| #11267 | Silence Claude auth nag when local API usage exists | barrydeen | 2.6 | 1.7 | 0.93 |
| #7400 | Prevent duplicate agents widget during migration | mdenesfe | 2.6 | 1.3 | 0.98 |
| #13740 | Keep RPC method names out of the Codex limits help text | alanw707 | 2.6 | 1.2 | 0.94 |
| #11360 | Fix debuginfod initialization in diagnose-crash skill | LouisDeconinck | 2.6 | 1.0 | 0.97 |
| #7298 | Stop the agents panel scrolling by a few pixels | YehudaGurovich | 2.5 | 0.9 | 0.68 |
| #13693 | Sync the Pi theme into PI_CODING_AGENT_DIR when it is set | manuaudio | 2.5 | 1.0 | 0.95 |
| #6478 | Attribute Codex sessions to their model from thread settings | dalmasluca | 2.4 | 1.5 | 0.96 |
| #10531 | Skip unchanged native Codex token snapshots | Brams-s | 2.4 | 1.6 | 0.93 |
| #8257 | Warn the agent skill off pulling graphical-session.target | kkoontz | 2.4 | 1.9 | 0.71 |
| #12986 | fix(agents): surface stale usage from record updatedAt (#12849) | kvnloo | 2.4 | 1.9 | 0.95 |
| #10633 | Mark retained Claude limits as last-known after a failed probe | fresh3nough | 2.3 | 0.9 | 0.97 |
| #13621 | Scan Codex pi sessions with rg --no-ignore | AnPod | 2.3 | 0.9 | 0.96 |
| #8399 | Migrate invitation hooks to notification argv | salemsayed | 2.3 | 2.1 | 0.88 |
| #10067 | Add fallback reload Timer for agent usage records | fresh3nough | 2.3 | 1.1 | 0.95 |
| #9697 | Report unreadable Claude transcripts once per scan | shaynhornik | 2.2 | 1.0 | 0.96 |
| #12547 | Activate the Omarchy theme for Claude Code when it's set as the agent | prusso | 2.2 | 1.5 | 0.76 |
| #13339 | Guard synced agent snapshot aggregation | AFOliveira | 2.2 | 2.2 | 0.92 |
| #13611 | Give default agents explicit mise packages including Copilot npm | AnPod | 2.1 | 1.6 | 0.93 |
| #12487 | fix: write Hermes bootstrap marker after headless install | adriannoes | 2.1 | 1.9 | 0.97 |
| #6828 | Open the first agent session in a normal tiled window too | 28allday | 2.1 | 1.3 | 0.94 |
| #11109 | Label a Claude Team seat by its subscription, not its rate-limit tier | omdenton | 2.1 | 1.0 | 0.96 |
| #13703 | Fix Codex limits timing out on buffered app-server replies | tossbaws | 2.1 | 1.4 | 0.96 |
| #8892 | Clear stale agent login guidance after successful probes | Hek846 | 2.1 | 1.3 | 0.94 |
| #9546 | Count omp and pi profile sessions in the agent usage collectors | This-Is-NPC | 2.1 | 1.6 | 0.91 |
| #8602 | Deduplicate Codex usage across Pi forked sessions | arisgysel-design | 2.0 | 2.0 | 0.90 |
| #8497 | Stop the agents status card rendering as an empty box | btsouth | 2.0 | 0.9 | 0.97 |
| #8073 | fix: detect early Codex app-server exits | dcalliari | 2.0 | 1.6 | 0.96 |
| #13816 | Handle interleaved Codex RPC notifications without timing out (#13773) | szaidi-code | 1.9 | 2.2 | 0.97 |
| #7225 | Label the Claude plan from the profile the CLI refreshes | IgorKramar | 1.9 | 1.8 | 0.96 |
| #8267 | Discover agent usage collectors in ~/.local/bin | manuelbecker123 | 1.9 | 1.7 | 0.85 |
| #11466 | Tell the agent skill to use omarchy pkg and omarchy update, not pacman | daja77 | 1.9 | 2.0 | 0.78 |
| #8345 | Fix Pi Codex session discovery | Longado | 1.9 | 2.1 | 0.94 |
| #12595 | Read only the session files that changed since the last scan | PapistProtocol | 1.9 | 2.9 | 0.67 |
| #10040 | Render usageStatusText in the agents status banner | Bartok9 | 1.9 | 0.5 | 0.97 |
| #12032 | Count only subscription-backed sessions as Codex usage | Ronin11 | 1.9 | 1.1 | 0.95 |

## Tranche: update-release — 31 PRs recommended as a merge-ready roll-up

| PR | title | author | finished | effort | fix |
|---|---|---|---|---|---|
| #13556 | Keep the Elsewhen migration test out of the real cache | manuaudio | 3.0 | 0.9 | 0.97 |
| #9286 | Skip tmux.conf migration when the file is not writable | fresh3nough | 3.0 | 1.1 | 0.98 |
| #8081 | Stop AUR daemons from keeping the omarchy-update lock | kdriedger | 3.0 | 1.3 | 0.97 |
| #12860 | Default OMARCHY_PATH in update-dev and channel-current | anandude | 2.9 | 1.5 | 0.96 |
| #12535 | Stop fetching the deleted master branch | paulogeyer | 2.9 | 1.8 | 0.96 |
| #8824 | Skip orphan prompt during unattended updates | maxcroy1 | 2.8 | 1.7 | 0.94 |
| #10066 | Distinguish checkupdates failure from up to date in update widget | fresh3nough | 2.8 | 1.3 | 0.97 |
| #13538 | Say which files block an upgrade the conflict recovery won't clear | stevederico | 2.7 | 1.1 | 0.73 |
| #9423 | Bound the browser policy refresh so a wedged browser can't stall an update | VykosMolt | 2.7 | 1.4 | 0.95 |
| #12503 | Skip CUPS discovery cleanup when the scheduler is stopped | paulogeyer | 2.7 | 1.0 | 0.97 |
| #8992 | Skip reboot prompts in unattended updates | maxcroy1 | 2.6 | 1.6 | 0.91 |
| #12174 | Give the Mise PATH cleanup a collision-free migration id | ekollof | 2.6 | 0.7 | 0.96 |
| #10524 | Avoid reboot prompts after identical Hyprland reinstalls | Brams-s | 2.5 | 2.0 | 0.96 |
| #6972 | Restore leftover app-menu icons after the Quattro upgrade | calledtoconstruct | 2.5 | 1.6 | 0.97 |
| #11480 | Serialize package availability checks across callers | yashranaway | 2.5 | 1.8 | 0.96 |
| #7398 | Resolve package-backed OMARCHY_PATH symlinks | mdenesfe | 2.5 | 1.8 | 0.98 |
| #13617 | Skip orphan gum confirm when omarchy-update runs unattended | AnPod | 2.5 | 1.2 | 0.96 |
| #11217 | Exit cleanly when the update log is missing | Bartok9 | 2.5 | 1.0 | 0.95 |
| #9568 | Defer XCompose reloads from migrations | rookepoole | 2.4 | 1.2 | 0.90 |
| #8042 | Regenerate mise wrappers that still print mise's output to stdout (backport of # | dhh | 2.3 | 1.1 | 0.96 |
| #12797 | Retry omarchy-bar put when omarchy-shell times out while busy | sanjyay | 2.3 | 1.0 | 0.98 |
| #13468 | Carry omarchy-bar put past a timing-out shell | AnPod | 2.2 | 1.6 | 0.97 |
| #7474 | Repair fcitx5 restart loops from user autostarts | nsumbadze | 2.2 | 1.9 | 0.95 |
| #10232 | fix(update): detect aarch64 kernels without vmlinuz | kvnloo | 2.1 | 1.1 | 0.96 |
| #12421 | Route Chromium notifications through the system center without joining flags | sprajs | 2.1 | 1.2 | 0.78 |
| #12722 | Keep installed ARM recovery packages during orphan cleanup | jdvmi00 | 2.1 | 0.9 | 0.89 |
| #13345 | Show plugin update diffs without git's pager | elberacasa | 2.0 | 0.5 | 0.93 |
| #8724 | Skip the reboot prompt when the flag predates the current boot | Pillumz | 2.0 | 1.2 | 0.96 |
| #9343 | Fail migrate --pending when the migrations directory is missing | Chessing234 | 1.9 | 1.0 | 0.97 |
| #13061 | Accept the -- operand separator in the kernel migration test pacman stubs | en3r0 | 1.9 | 1.4 | 0.97 |
| #12920 | Seed fcitx5 DefaultIM from vconsole XKBLAYOUT | Chessing234 | 1.8 | 1.6 | 0.87 |

## Tranche: install-setup — 29 PRs recommended as a merge-ready roll-up

| PR | title | author | finished | effort | fix |
|---|---|---|---|---|---|
| #13721 | setup-form: reject usernames longer than 32 characters | kvnloo | 2.9 | 1.1 | 0.97 |
| #12384 | Encode browser native-host paths as JSON | yashranaway | 2.9 | 1.7 | 0.97 |
| #12004 | Remove Herdr with preinstalls | markallisongit | 2.9 | 1.3 | 0.95 |
| #8486 | Detect Broadcom fingerprint readers by vendor ID | gbillium143 | 2.8 | 0.8 | 0.97 |
| #13079 | Remove the hey, basecamp, and cf stubs with preinstalls | yamz8 | 2.8 | 1.2 | 0.96 |
| #13470 | Add recursion guard to omarchy-mise-install wrappers | AnPod | 2.8 | 1.2 | 0.97 |
| #7473 | Preserve XCompose customizations on setup rerun | nsumbadze | 2.8 | 1.0 | 0.96 |
| #9626 | Set the Windows VM guest timezone to match the host | beatrizmitre | 2.7 | 1.6 | 0.84 |
| #11953 | Select iso2sd drives by removability, not by /dev/sd name | Dayocom | 2.6 | 1.0 | 0.95 |
| #11842 | Give a clear diagnosis when libfprint has no driver for the detected fingerprint | busbyjon | 2.5 | 1.4 | 0.95 |
| #9563 | fix: keep XDG desktop out of home | motodriver | 2.5 | 2.1 | 0.80 |
| #12545 | Reject usernames that collide with system groups | paulogeyer | 2.5 | 1.9 | 0.94 |
| #7890 | Reject Voxtype on CPUs without AVX2 | kx0101 | 2.4 | 1.6 | 0.95 |
| #13765 | Write GTK bookmarks atomically instead of check-then-act | SorenHJohansen | 2.4 | 1.7 | 0.97 |
| #13719 | install-xcompose: stop blanking ~/.XCompose on refresh with empty inputs | kvnloo | 2.4 | 1.1 | 0.96 |
| #11694 | Keep the fcitx5 unit inert when fcitx5 isn't installed | therk | 2.3 | 0.8 | 0.95 |
| #12971 | Omit --load-extension from Google Chrome browser flags | kvnloo | 2.3 | 1.6 | 0.94 |
| #7667 | Hint at the ELAN 04f3:0c4b generic-driver matching bug in fingerprint setup | jcperdomoybarra | 2.2 | 0.9 | 0.61 |
| #8682 | Use German console keymap with umlauts | Witteborn | 2.1 | 1.1 | 0.93 |
| #9420 | Escape the values written into retro game desktop files | Adolanium | 2.1 | 1.4 | 0.96 |
| #12733 | Refuse direct boot on Surface firmware | kermes | 2.0 | 0.8 | 0.63 |
| #8141 | Fix install-and-launch done prompt race | CooperSheroy | 2.0 | 1.2 | 0.96 |
| #11973 | Regenerate mise wrappers that still print mise's output on every run | jayrascodes | 2.0 | 2.0 | 0.96 |
| #8631 | Route the Voxtype model picker to the install flow when voxtype is missing | alexandru-savinov | 2.0 | 1.0 | 0.95 |
| #11125 | Retry first-run when user finalization fails | vovarbv | 1.9 | 1.6 | 0.96 |
| #7661 | fix(menu): rank apps above destructive actions | ketpatil77 | 1.9 | 1.2 | 0.92 |
| #11056 | Point six installer keymaps at ones systemd can map | BRashad | 1.8 | 1.3 | 0.96 |
| #11691 | Make the install entries work where the repo package is missing | therk | 1.8 | 1.4 | 0.90 |
| #10599 | Detach Windows installer progress browser from its terminal | reoring | 1.8 | 1.3 | 0.93 |

## Tranche: docs — 9 PRs recommended as a merge-ready roll-up

| PR | title | author | finished | effort | fix |
|---|---|---|---|---|---|
| #10017 | Note that service-plugin constants need a shell restart | hudsonwa | 2.9 | 0.7 | 0.64 |
| #11284 | Fix Bash learning link | hussainanjar | 2.9 | 0.3 | 0.96 |
| #11708 | Fix the speaker tuning service documentation link | matthewkrausse | 2.8 | 0.1 | 0.94 |
| #11026 | Document that resize Super+Minus/Equal are physical AE11/AE12 | kvnloo | 2.7 | 0.8 | 0.72 |
| #8585 | Add the 2020 Intel MacBook Air to the T2 device list | equivalent | 2.6 | 0.6 | 0.64 |
| #11483 | Extract crash cores on disk instead of tmpfs | yashranaway | 2.6 | 1.1 | 0.86 |
| #10499 | Point the plugin manual at plugins.omarchy.org | kkoontz | 2.4 | 0.3 | 0.80 |
| #8846 | List the Herdr PREFIX chord first in the learn guide | daveyb | 2.2 | 0.8 | 0.84 |
| #13717 | menu-images: document --prepare-only in args header and usage | kvnloo | 1.9 | 0.7 | 0.63 |

## Duplicate / overlapping clusters (consolidate; maintainer picks the winner)

- #9605 (canonical candidate), #10411 (superseded), #12019 (superseded), #12264 (superseded), #12323 (superseded), #13154 (superseded), #13213 (superseded), #13750 (superseded) — e.g. “Clear set-ID bits when securing the Windows VM mount sources”
- #7765 (canonical candidate), #8065 (superseded), #12635 (superseded), #12651 (superseded) — e.g. “Add OpenCode Zen usage to the agents panel”
- #6572 (canonical candidate), #7877 (superseded), #8955 (superseded), #13359 (superseded) — e.g. “Re-implement D-Bus idle-inhibit support dropped in the Quattro rewrite”
- #6834 (canonical candidate), #12350 (superseded), #12679 (superseded) — e.g. “Ignore T2 headset remotes when switching layouts”
- #6485 (canonical candidate), #12352 (superseded), #13219 (superseded) — e.g. “Add a Grok usage collector”
- #7659 (canonical candidate), #8023 (superseded), #12574 (superseded) — e.g. “fix(menu): accept plus in search input”
- #12074 (canonical candidate), #12090 (superseded), #12680 (superseded) — e.g. “Install stock kernel headers for broadcom-wl-dkms on upgraded Macs”
- #12649 (canonical candidate), #12755 (superseded), #13009 (superseded) — e.g. “Keep UPower rate when sysfs power read fails with ENODEV”
- #5774 (canonical candidate), #9430 (superseded), #12754 (superseded) — e.g. “Add Vivaldi browser support (fixed)”
- #11023 (canonical candidate), #11025 (superseded), #12932 (superseded) — e.g. “Warn when root Btrfs spans extra LUKS devices the initramfs cannot unl”
- #11021 (canonical candidate), #11022 (superseded), #12955 (superseded) — e.g. “Skip tray grab until the SNI menu has children”
- #7577 (canonical candidate), #9803 (superseded), #13024 (superseded) — e.g. “Stop the Broadcom Wi-Fi quirk breaking Apple Silicon Macs”
- #10194 (canonical candidate), #11112 (superseded), #13223 (superseded) — e.g. “Fix the display panel's on/off rows under the Lua config parser”
- #13165 (canonical candidate), #13477 (superseded), #13645 (superseded) — e.g. “Skip placeholder screens when building bars”
- #13459 (canonical candidate), #13463 (superseded), #13613 (superseded) — e.g. “Scale clock panel hero date with fontScale”
- #13467 (canonical candidate), #13542 (superseded), #13612 (superseded) — e.g. “Let fingerprint setup adopt an already-enrolled print”
- #10430 (canonical candidate), #12337 (superseded) — e.g. “Make night light temperature configurable”
- #8537 (canonical candidate), #10294 (superseded) — e.g. “Add Alfred/Raycast-style live query plugins to the menu”
- #9127 (canonical candidate), #12424 (superseded) — e.g. “Add a notification for hyprpicker”
- #9885 (canonical candidate), #12425 (superseded) — e.g. “Notify when agent limits reset”
- #9189 (canonical candidate), #12423 (superseded) — e.g. “Keep the backlight off while the laptop panel is disabled”
- #12024 (canonical candidate), #12445 (superseded) — e.g. “Aggregate battery status across all packs”
- #7568 (canonical candidate), #12446 (superseded) — e.g. “Add dynamic bar transparency mode”
- #10413 (canonical candidate), #13214 (superseded) — e.g. “Harden omarchy-refresh-config against path traversal”
- #11918 (canonical candidate), #12461 (superseded) — e.g. “Back off fingerprint retries that fail immediately”
- #12505 (canonical candidate), #13331 (superseded) — e.g. “Enable Sunshine by its real systemd user unit name”
- #10463 (canonical candidate), #10920 (superseded) — e.g. “Fix display backlight on Lenovo Yoga Pro 7 15IPH11”
- #10476 (canonical candidate), #13186 (superseded) — e.g. “Build the calendar month grid in UTC”
- #8429 (canonical candidate), #12957 (superseded) — e.g. “[Security] Keep the update transcript out of world-writable /tmp”
- #6951 (canonical candidate), #12548 (superseded) — e.g. “Pin root= before the packages that can drop it”
- #8875 (canonical candidate), #12569 (superseded) — e.g. “Install lib32 GPU drivers before Steam”
- #10530 (canonical candidate), #12667 (superseded) — e.g. “Map keypad digits in the polkit dialog when Qt ignores NumLock”
- #7087 (canonical candidate), #12582 (superseded) — e.g. “Add Cursor usage collector to the agents panel”
- #10586 (canonical candidate), #13749 (superseded) — e.g. “Ignore Hyprland FALLBACK in external-monitor checks”
- #10587 (canonical candidate), #13517 (superseded) — e.g. “Dismiss screensaver on bare Ctrl while it is open”
- #12184 (canonical candidate), #12646 (superseded) — e.g. “Fix bar reposition-drag on an empty desktop (#11915)”
- #7783 (canonical candidate), #12658 (superseded) — e.g. “Keep PwNode objects out of the audio panel's Repeater models”
- #10610 (canonical candidate), #12048 (superseded) — e.g. “Add Muse usage collector to the agents panel”
- #9735 (canonical candidate), #12685 (superseded) — e.g. “Force SPI PIO on MacBook8,1 so the built-in keyboard works”
- #6587 (canonical candidate), #13137 (superseded) — e.g. “Let [bar] in shell.toml set every token Style reads”
- #7074 (canonical candidate), #12759 (superseded) — e.g. “Remember cursor position when navigating back in the root menu”
- #9490 (canonical candidate), #12800 (superseded) — e.g. “Quote omarchy-launch-or-focus-tui and -webapp arguments like install-a”
- #11565 (canonical candidate), #12831 (superseded) — e.g. “Scope LocalSend firewall rules to private and local subnets (#11560)”
- #10789 (canonical candidate), #13545 (superseded) — e.g. “Keep the bar center pinned when centerAnchor's widget leaves the layou”
- #6924 (canonical candidate), #12851 (superseded) — e.g. “Prevent togglesplit error in scrolling layout”
- #11933 (canonical candidate), #12870 (superseded) — e.g. “Install Bitwarden desktop even when CLI conflicts with nodejs”
- #6058 (canonical candidate), #10867 (superseded) — e.g. “Theme Zen Browser chrome”
- #12939 (canonical candidate), #13109 (superseded) — e.g. “Don't let the Codex usage collector install Codex”
- #6098 (canonical candidate), #6802 (superseded) — e.g. “feat(webapps): add Zen browser support to launcher”
- #10231 (canonical candidate), #12956 (superseded) — e.g. “fix(herdr): free swap_pane_up from close_workspace chord”
- #8872 (canonical candidate), #8881 (superseded) — e.g. “fix(notification): bound omarchy-notification-wait by wall clock”
- #8884 (canonical candidate), #13568 (superseded) — e.g. “Load the image thumbnail index once”
- #6847 (canonical candidate), #13699 (superseded) — e.g. “Preserve shared boot entries through factory reset”
- #9130 (canonical candidate), #13007 (superseded) — e.g. “Send clipboard shortcuts using physical XKB keys”
- #7373 (canonical candidate), #13029 (superseded) — e.g. “update battery lookup”
- #13041 (canonical candidate), #13673 (superseded) — e.g. “Honour explicit expireTimeout for critical notifications (#12911)”
- #5431 (canonical candidate), #6897 (superseded) — e.g. “feat(hardware): sync ThinkBook mute LEDs with WirePlumber state”
- #13044 (canonical candidate), #13094 (superseded) — e.g. “fix(launch-editor): pass wait flags to GUI editors in inline mode (#13”
- #8952 (canonical candidate), #13848 (superseded) — e.g. “Replace Gemini coding agent with Antigravity (backport of #6900)”
- #5332 (canonical candidate), #13055 (superseded) — e.g. “Enable SSD TRIM for LUKS-encrypted drives”
- #5099 (canonical candidate), #11008 (superseded) — e.g. “Fix layout toggle script for special workspaces”
- #13090 (canonical candidate), #13677 (superseded) — e.g. “Resolve mise wrapper binaries to absolute paths”
- #13101 (canonical candidate), #13668 (superseded) — e.g. “Actually restart bluetooth.service in omarchy-restart-bluetooth”
- #11069 (canonical candidate), #11470 (superseded) — e.g. “Run declared plugin cleanup before removal”
- #4928 (canonical candidate), #7700 (superseded) — e.g. “Only match window class in omarchy-launch-or-focus”
- #9071 (canonical candidate), #9073 (superseded) — e.g. “Backport constrained Quattro ownership bootstrap to dev”
- #7023 (canonical candidate), #12022 (superseded) — e.g. “Fix inverted on/off semantics in omarchy-toggle-bar”
- #7040 (canonical candidate), #11612 (superseded) — e.g. “feat(security): Add face authentication setup and removal commands”
- #12177 (canonical candidate), #13205 (superseded) — e.g. “Add 80% battery charge cap toggle”
- #7075 (canonical candidate), #8012 (superseded) — e.g. “menu: add web search fallback for unmatched queries”
- #8005 (canonical candidate), #13233 (superseded) — e.g. “Fix grammar in navigation manual”
- #7102 (canonical candidate), #13637 (superseded) — e.g. “Only treat lost focus as a dismissal once the screensaver has held foc”
- #13258 (canonical candidate), #13620 (superseded) — e.g. “Retry bt-agent after bluetooth.service instead of skipping”
- #13314 (canonical candidate), #13651 (superseded) — e.g. “Prune stale Quickshell instance logs from the user runtime”
- #7180 (canonical candidate), #7333 (superseded) — e.g. “Work around Apple BCM4350 suspend failures”
- #5600 (canonical candidate), #11294 (superseded) — e.g. “fix imv image navigation”
- #10138 (canonical candidate), #13347 (superseded) — e.g. “Resync the clock when the wall clock is stepped”
- #11976 (canonical candidate), #13369 (superseded) — e.g. “Highlight each monitor's own active workspace in the bar”
- #13377 (canonical candidate), #13660 (superseded) — e.g. “Refuse omarchy-update when invoked as root”
- #11364 (canonical candidate), #12089 (superseded) — e.g. “Keep existing wine when installing Lutris”
- #13444 (canonical candidate), #13544 (superseded) — e.g. “Keep the reboot offer after a channel switch”
- #13462 (canonical candidate), #13602 (superseded) — e.g. “Preflight the ESP free space before an update”
- #13466 (canonical candidate), #13543 (superseded) — e.g. “Back off Bluetooth discovery retries instead of spamming at 1 Hz”
- #13471 (canonical candidate), #13633 (superseded) — e.g. “Give replacement-bar entries their own service lookup”
- #13474 (canonical candidate), #13646 (superseded) — e.g. “Soften yay go-mod caches and warn on AUR update failure”
- #13476 (canonical candidate), #13643 (superseded) — e.g. “Exit compositor fullscreen before launching web apps”
- #13478 (canonical candidate), #13641 (superseded) — e.g. “Floor Apple Silicon top bars to the camera notch cutout”
- #13480 (canonical candidate), #13640 (superseded) — e.g. “Wait for an active output before sleep-lock finishes”
- #7345 (canonical candidate), #7737 (superseded) — e.g. “Let users rebind the menu's navigation keys”
- #9871 (canonical candidate), #13505 (superseded) — e.g. “Add Hermes usage collector for the agents panel”
- #9429 (canonical candidate), #13756 (superseded) — e.g. “Verify the session is secure before system lock succeeds”
- #13540 (canonical candidate), #13610 (superseded) — e.g. “Hibernate laptops on critical battery once hibernation is set up”
- #9958 (canonical candidate), #13548 (superseded) — e.g. “Add minimax agent usage collector for opencode”
- #13626 (canonical candidate), #13656 (superseded) — e.g. “Stamp new migrations with wall-clock time”
- #11751 (canonical candidate), #13648 (superseded) — e.g. “Unmap KeyboardPanel even when owner.close() throws”
- #12150 (canonical candidate), #13670 (superseded) — e.g. “Make omarchy toggle bar on/off match bar visibility”
- #11669 (canonical candidate), #13729 (superseded) — e.g. “Restore the keyboard backlight level after hibernation”
- #6105 (canonical candidate), #9679 (superseded) — e.g. “Make webapps profile-aware for Chromium-based browsers”
- #7894 (canonical candidate), #12142 (superseded) — e.g. “Add fcitx5 theme sync helper”
- #6019 (canonical candidate), #7945 (superseded) — e.g. “Expand Nautilus into usage as file picker in Open/Save dialog (provide”
- #10007 (canonical candidate), #12255 (superseded) — e.g. “Preserve built-in fields in partial menu overrides”

## Uncertain pairs — Jev is undecided, human decides

- #13444 ↔ #13616 (P(same)=0.64): “Keep the reboot offer after a channel switch” / “Keep sudo alive and offer reboot after channel switch”
- #11381 ↔ #12686 (P(same)=0.64): “Install the pre-T2 FaceTime HD camera driver and firmwa” / “[Intel Mac P08] Consolidate FaceTime PCIe camera suppor”
- #11055 ↔ #11080 (P(same)=0.63): “Move setCenterHoverRevealSuppressed into Panel base to ” / “Fix PluginBarApi hover-reveal writes so cloned panels c”
- #12067 ↔ #12686 (P(same)=0.63): “Install the FaceTime HD camera driver on Intel Macs tha” / “[Intel Mac P08] Consolidate FaceTime PCIe camera suppor”
- #7158 ↔ #8531 (P(same)=0.62): “Keep the lock screen fingerprint working across suspend” / “Keep fingerprint unlock working across suspend”
- #8414 ↔ #12936 (P(same)=0.60): “Detect Microarray MAFP fingerprint reader” / “Detect Microarray MAFP fingerprint readers (3274:8012)”
- #7528 ↔ #8048 (P(same)=0.60): “Dismiss the screensaver on touch and pointer input, blu” / “Dismiss screensaver on pointer motion”
- #7577 ↔ #9803 (P(same)=0.59): “Stop the Broadcom Wi-Fi quirk breaking Apple Silicon Ma” / “Fix WPA3 on MacBookPro16,1”
- #8210 ↔ #8720 (P(same)=0.59): “Let themes set Hyprland rounding and shadow through col” / “Add declarative Hyprland and terminal theming”
- #8685 ↔ #11056 (P(same)=0.57): “Derive the Hyprland keyboard layout from the console ke” / “Point six installer keymaps at ones systemd can map”
- #6907 ↔ #13378 (P(same)=0.57): “Restore conventional copy/paste bindings in foot config” / “Add Ctrl+Shift+C/V to existing Foot clipboard bindings”
- #11033 ↔ #11652 (P(same)=0.56): “Make the Intel IPU6 camera work out of the box” / “Make the Intel IPU6 webcam behind an IVSC work”
- #8609 ↔ #9095 (P(same)=0.56): “Tell contributors to check for duplicates and the right” / “Tell contributors to search open PRs before writing a f”
- #10198 ↔ #12683 (P(same)=0.54): “Disable ghost internal display connectors” / “[Intel Mac P05] Handle ghost internal displays”
- #12020 ↔ #12189 (P(same)=0.54): “Ignore bytecode and temp files in local plugin watcher” / “Only reload local plugins when loadable sources change”
- #5975 ↔ #10430 (P(same)=0.53): “Make nightlight temperature configurable via env variab” / “Make night light temperature configurable”
- #6849 ↔ #11076 (P(same)=0.53): “Fix jittery scrolling on Dell XPS 13 Wildcat Lake by di” / “Disable broken eDP Panel Replay on Dell XPS Panther Lak”
- #11904 ↔ #12692 (P(same)=0.53): “Add omarchy-diagnose-suspend-wake” / “[Intel Mac P14] Consolidate suspend diagnostics”
- #9880 ↔ #12684 (P(same)=0.53): “Stop installing the obsolete SPI keyboard DKMS package” / “[Intel Mac P06] Retire the legacy SPI package alongside”
- #10660 ↔ #10677 (P(same)=0.52): “Background wipe animates on only one output” / “Continue the background wipe across every output”
- #10232 ↔ #12956 (P(same)=0.52): “fix(update): detect aarch64 kernels without vmlinuz” / “fix: herdr swap_pane_up + aarch64 kernel restart (#1023”
- #11792 ↔ #13205 (P(same)=0.51): “Add battery charge-limit presets to the power panel” / “Add battery charge-limit toggle to power panel (UPower ”
- #5686 ↔ #10185 (P(same)=0.51): “Add speech-dispatcher and espeak-ng for text-to-speech ” / “Add speech-dispatcher so Brave Web Speech has voices”
- #8771 ↔ #9164 (P(same)=0.50): “Default OMARCHY_PATH in omarchy-update-available” / “Default OMARCHY_PATH in channel-current and audio-tunin”
- #10989 ↔ #12955 (P(same)=0.50): “fix: keep 1.25x tooltip and scale-pill borders from dro” / “fix: shell bar/tray/agents leftovers (#10989 #11021 #11”
- #10393 ↔ #12461 (P(same)=0.50): “Cap lock fingerprint retries; skip closed-lid fingerpri” / “Stop the lock fingerprint retry loop instead of slowing”
- #5975 ↔ #12337 (P(same)=0.49): “Make nightlight temperature configurable via env variab” / “Make night light temperatures configurable in shell.jso”
- #11080 ↔ #11751 (P(same)=0.49): “Fix PluginBarApi hover-reveal writes so cloned panels c” / “Unmap KeyboardPanel even when owner.close() throws”
- #5317 ↔ #8820 (P(same)=0.48): “feat: gracefully swap ALSA hardware profiles on single-” / “Show inactive audio card outputs in picker”
- #13544 ↔ #13616 (P(same)=0.47): “Offer the reboot after a channel switch” / “Keep sudo alive and offer reboot after channel switch”
- #12972 ↔ #13019 (P(same)=0.47): “Add a camera bar widget that turns every USB camera off” / “Add a camera bar widget that shows when a webcam is in ”
- #12253 ↔ #12857 (P(same)=0.47): “Require a mode before counting an external monitor as a” / “Don't reload a 0x0 monitor that already has video modes”
- #12007 ↔ #12684 (P(same)=0.47): “Drop macbook12-spi-driver-dkms, which no longer builds ” / “[Intel Mac P06] Retire the legacy SPI package alongside”
- #7471 ↔ #7592 (P(same)=0.46): “Wake the blanked lock screen from the keyboard” / “Refocus the lock password field after resume”
- #8709 ↔ #9461 (P(same)=0.45): “fix: arm signature verification for the T2 repo and clo” / “[codex] OM-SEC-05: Remove the unsigned Apple T2 package”
- #9725 ↔ #13138 (P(same)=0.45): “Feature: Allow user to create floating bar by adding su” / “Floating bar: margin, radius, a switch and Hyprland-der”
- #8169 ↔ #9465 (P(same)=0.44): “Stop apply-system reruns leaving the install log world-” / “[codex] OM-SEC-10: Replace the world-writable installer”
- #5343 ↔ #7363 (P(same)=0.44): “Install nautilus-open-any-terminal to open the default ” / “Add Open in Terminal to the Files context menu”
- #7283 ↔ #13007 (P(same)=0.44): “Use layout-independent universal clipboard shortcuts” / “fix(hypr): resolve universal clipboard letters from pri”
- #7179 ↔ #12420 (P(same)=0.44): “Stop the lock screen overheating the fingerprint reader” / “lock: stop fingerprint scans while the display is blank”
- #8866 ↔ #12071 (P(same)=0.43): “Fix network panel behind VPN policy routes” / “Show physical network behind TUN routes”
- #9632 ↔ #11746 (P(same)=0.43): “Keep idle lock handoff concealed” / “Dismiss screensaver on seat input and conceal idle lock”
- #11477 ↔ #13768 (P(same)=0.42): “Reconcile hibernation resume parameters with the swapfi” / “Keep hibernation resume offset in sync with the swapfil”
- #8581 ↔ #10130 (P(same)=0.42): “Re-arm lock blank timer with backoff on screen changes” / “Re-arm the lock screen's blank timer from any input whi”
- #7449 ↔ #8573 (P(same)=0.41): “emoji-insert: persist clipboard instead of clearing it ” / “Fix Emoji Picker for all apps with both keyboard and mo”
- #7564 ↔ #11733 (P(same)=0.40): “Make the keybindings menu's Lua bind scan safe against ” / “Read keybindings from the running compositor instead of”
- #9546 ↔ #10330 (P(same)=0.40): “Count omp and pi profile sessions in the agent usage co” / “Add a dedicated pi agent usage collector”
- #6892 ↔ #8573 (P(same)=0.40): “Fix emoji paste in Firefox” / “Fix Emoji Picker for all apps with both keyboard and mo”
- #9296 ↔ #12471 (P(same)=0.40): “Recover screen-recording indicator after stuck probes” / “Fix recording indicator stuck 'active' after a force-ki”
- #9780 ↔ #12016 (P(same)=0.39): “Switch to a workspace on the focused monitor” / “Open a hidden workspace on the bar that was clicked”
- #10270 ↔ #11394 (P(same)=0.38): “Reduce notification overlay surface area” / “Reduce OSD and notification layer surface area”
- #10845 ↔ #11121 (P(same)=0.38): “Show API-equivalent agent usage cost” / “Show local agent API cost estimates with stable, respon”
- #10330 ↔ #10824 (P(same)=0.38): “Add a dedicated pi agent usage collector” / “Add OpenRouter usage collector to the agents panel”
- #7333 ↔ #12688 (P(same)=0.38): “Reset Apple BCM4350/BCM43602 Wi-Fi around sleep” / “[Intel Mac P10] Consolidate Broadcom calibration and sl”
- #7187 ↔ #13070 (P(same)=0.37): “Fix image paste in Kitty and Ghostty” / “Paste clipboard images into foot (and Kitty/Ghostty) wi”
- #12328 ↔ #12691 (P(same)=0.37): “Keep every Intel Mac on its kernel in the linux-omarchy” / “[Intel Mac P13] Consolidate the Intel Mac kernel migrat”
- #7880 ↔ #13811 (P(same)=0.36): “Don't treat Bluetooth Trusted as a completed pairing” / “fix(bluetooth): recover incomplete pairing”
- #12248 ↔ #13568 (P(same)=0.36): “Perf: disk speedtest staging, batched window pop, in-me” / “Read the thumbnail index once in the direct image scan”
- #9070 ↔ #9073 (P(same)=0.35): “Make package ownership the Quattro update boundary” / “Backport constrained Quattro ownership bootstrap to rc”
- #7180 ↔ #12688 (P(same)=0.35): “Work around Apple BCM4350 suspend failures” / “[Intel Mac P10] Consolidate Broadcom calibration and sl”
- …and 1 more in out/dupes.json

## Escalate to senior review (high risk or security-relevant)

- #4997 Add NetBird as optional VPN service (security 0.83)
- #5035 Prevent empty passwords in omarchy-drive-set-password (security 0.95)
- #5139 Add Orca screen reader with Piper TTS (security 0.50)
- #5284 Add NuPhy Air75 V3 keyboard support (security 0.89)
- #5431 feat(hardware): sync ThinkBook mute LEDs with WirePlumber state (security 0.86)
- #5545 Stop package install flows after aborts or failures (security 0.82)
- #5654 Add Install -> Editor -> Jetbrains menu (security 0.73)
- #5744 feat: Add installer for official Obsidian CLI (security 0.85)
- #6474 Add Android development environment (security 0.64)
- #6513 Enable DNS-over-TLS for custom DNS providers (security 0.51)
- #6515 Support hardware, fingerprint, and password Polkit flows (security 0.51)
- #6532 Abort pkg-install when the package transaction fails or is interrupted (security 0.52)
- #6557 feature(editor) add Doom Emacs installer, uninstaller, and theming integration (security 0.65)
- #6647 Add local and remote Hermes usage sources to Agents panel (security 0.93)
- #6664 Fix fingerprint setup script to detect non-libfprint-git providers (security 0.51)
- #6697 Adding Atuin be default for better shell search / history (security 0.56)
- #6736 Docker multi-arch build with sudo support (security 0.94)
- #6807 Detect captive portals and offer to sign in (security 0.69)
- #6844 Add Amp as a default coding agent (security 0.71)
- #6847 Preserve shared boot entries through factory reset (security 0.77)
- #6912 Fix FIDO2 setup on keys that require user verification (security 0.72)
- #6965 Add git-based backup and restore (security 0.67)
- #6980 Add agent security scans for untrusted software (security 0.78)
- #7040 feat(security): Add face authentication setup and removal commands (security 0.79)
- #7051 Add Synthetic Labs quotas to the agents panel (security 0.90)
- #7071 Migrate Brave Origin Beta profile data to stable (security 0.60)
- #7087 Add Cursor usage collector to the agents panel (security 0.83)
- #7258 Restore early Thunderbolt authorization for LUKS unlock (risk 3.0, security 0.75)
- #7272 Switch between subscription accounts (security 0.93)
- #7274 Add a Kimi usage collector to the agents panel (security 0.95)
- #7417 Add NetBird mesh VPN integration (security 0.91)
- #7435 Add Wi-Fi hotspot hosting to the network panel (security 0.97)
- #7455 Read Fireworks credentials from pi's auth.json (security 0.95)
- #7485 Add Firebase CLI development environment via mise (security 0.64)
- #7501 Apply session monitor scale to the SDDM greeter (security 0.94)
- #7537 Show limits for OpenCode's OpenAI account (security 0.84)
- #7554 Add bb to the AI install menu (security 0.79)
- #7622 Add an omarchy:// link handler for installing plugins from a web page (security 0.62)
- #7680 Add a reveal toggle to the lock screen password field (security 0.54)
- #7731 Show Windows PCs and admin shares in Files (security 0.66)
- #7799 Show banked rate limit resets on the Codex tab (security 0.65)
- #7814 Add encrypted, versioned, off-site backups (security 0.93)
- #7828 Add "Join hidden network" to the Wi-Fi panel (security 0.96)
- #7831 Reload a wedged Wi-Fi radio without waiting for the user (security 0.71)
- #7857 feat(surface-touch): add touchscreen support for Surface devices via linux-surfa (security 0.78)
- #7871 Stop the lid gate logging a PAM failure on every open-lid sudo (security 0.50)
- #7882 Add native Syncthing integration (security 0.69)
- #7913 Add maker install group with ESP32/ESP-IDF toolchain setup (security 0.90)
- #7971 Let the compositor and audio graph take the realtime priority they ask for (security 0.77)
- #7990 Clear passwordless sudo grants at boot (security 0.89)
- #7995 Stage diagnostics logs privately instead of at fixed /tmp paths (security 0.61)
- #8001 Fix GitHub credential helpers after mise gh upgrades (security 0.69)
- #8014 Keep Wi-Fi password entry stable during scans (security 0.89)
- #8019 Eye toggle to show/hide the Wi-Fi password (security 0.81)
- #8035 Add VPN section to the network panel (security 0.70)
- #8065 Add OpenCode Go usage collector for the agents panel (security 0.74)
- #8093 Call a lapsed Claude access token paused, not signed out (security 0.55)
- #8130 Stop NordVPN installation after setup failure (security 0.68)
- #8169 Stop apply-system reruns leaving the install log world-writable (security 0.89)
- #8188 Add and remove tailnets from the Tailscale panel (security 0.80)
- #8204 Stop probing the internal T2 network interface (security 0.55)
- #8251 Add a copy action for the revealed wifi password (security 0.91)
- #8294 Add Wi-Fi QR code scanning (security 0.92)
- #8326 Read Claude limits with a sibling CLI's token when the saved one lapsed (security 0.92)
- #8336 Add face authentication (howdy) to the lock screen (security 0.91)
- #8413 Add Scanner support (security 0.52)
- #8441 Pin Cursor password store to gnome-libsecret so GitHub login can use the OS keyr (security 0.83)
- #8472 Omarchy v4.0.2 (security 0.85)
- #8487 Add openzoo as a coding agent option: claude code, no api key, pays per call (security 0.85)
- #8532 Constrain the asdcontrol sudoers rule to hiddev detect/get/set (security 0.96)
- #8534 Take privileged usernames from id -un, not USER (security 0.95)
- #8537 Add Alfred/Raycast-style live query plugins to the menu (security 0.62)
- #8578 Update installed themes in parallel (security 0.51)
- #8588 Install system-sleep hooks executable (security 0.50)
- #8662 Sanitize legacy Windows VM usernames (security 0.78)
- #8707 Set Tailscale operator for Taildrop (security 0.87)
- #8709 fix: arm signature verification for the T2 repo and close the quattro override w (security 0.82)
- #8801 Add Helium and Ungoogled Chromium browser support (security 0.57)
- #8831 Allow IGMP so multicast group queries stop flooding the firewall log (security 0.91)
- #8889 Apply uinput permissions through tmpfiles (security 0.94)
- #8908 Switch DNS providers without DHCP churn or profile rewrites (security 0.58)
- #8910 Avoid redundant lock after encrypted hibernate (security 0.53)
- #8930 Harden lock lifecycle, recovery, and keyboard wake (risk 3.1, security 0.61)
- #8952 Replace Gemini coding agent with Antigravity (backport of #6900) (security 0.56)
- #8994 Isolate /var/lib/docker on a top-level Btrfs subvolume (risk 3.3)
- #9024 Auto-create /etc/1password/custom_allowed_browsers on install (security 0.63)
- #9043 Authorize SSH keys into the invoking user's home (security 0.93)
- #9044 Keep SDDM auto-login off encrypted roots in the quattro upgrade (security 0.69)
- #9221 Add AirPlay audio output (security 0.94)
- #9227 Require interactive confirmation for AUR installs and updates (security 0.72)
- #9239 Sync the GNOME keyring on user password changes (security 0.93)
- #9248 Add managed account website allowlists (security 0.94)
- #9288 Set kernel.kptr_restrict=1 in the shipped sysctl drop-in (security 0.53)
- #9307 Clarify that "grab key from github" in sshd setup authorizes EVERY machine that  (security 0.89)
- #9319 Give the Secret portal a provider so Chromium can open its password store (security 0.86)
- #9320 Add Oma, voice control for the desktop, as an optional service (security 0.53)
- #9459 [codex] OM-SEC-03: Remove public Windows VM default credentials (security 0.98)
- #9460 [codex] OM-SEC-04: Require package authenticity during Quattro (security 0.86)
- #9461 [codex] OM-SEC-05: Remove the unsigned Apple T2 package source (security 0.74)
- #9463 [codex] OM-SEC-08: Publish SSH only after proving key-only access (security 0.93)
- #9464 [codex] OM-SEC-09: Generate private credentials for development databases (risk 3.1, security 0.98)
- #9465 [codex] OM-SEC-10: Replace the world-writable installer log (risk 3.1, security 0.93)
- #9470 [codex] OM-SEC-15: Keep mixed-trust installers outside sudo lifetime (security 0.94)
- #9474 [codex] OM-SEC-19: Protect migration and SSH setup authorization (security 0.92)
- #9475 [codex] OM-SEC-21: Authenticate only after package picker code exits (security 0.89)
- #9477 [codex] OM-SEC-23: Keep debug collectors outside dmesg authorization (security 0.95)
- #9500 Give visudo an editor that Omarchy actually installs (security 0.82)
- #9506 Keep SSH setup from disabling passwords on a writable home (security 0.91)
- #9511 Support non-interactive updates with --yes (security 0.76)
- #9531 Wait for the Windows VM RDP service before connecting (security 0.54)
- #9539 Add cursor theme selection to the Style menu (security 0.68)
- #9571 Resolve the invoking user's home in removal cleanup scripts (security 0.68)
- #9573 Judge the invoking user's authorized keys when removing SSH access (risk 3.0, security 0.92)
- #9594 Fix XDG Secret portal keyring access (security 0.68)
- #9597 Add MiniMax Token Plan support (security 0.88)
- #9605 Clear set-ID bits when securing the Windows VM mount sources (security 0.92)
- #9695 Add a Setup > Region toggle with Chinese language and input method (security 0.77)
- #9700 Seed Chromium's first-run preferences with a mode the browser can read (security 0.93)
- #9723 Add an embedded dev-env for ESP32 and Arduino boards (security 0.86)
- #9729 Add Setup Wizard for NVIDIA DisplayPort 1.4 EDID Fix (security 0.61)
- #9750 Kids mode: child installs with a kid password and a parent password (security 0.97)
- #9777 Add DeepSeek Harness to the agent roster and Install > AI (security 0.62)
- #9783 Fix Windows VM helper rejecting setgid source directories (security 0.93)
- #9834 Refuse to run the shell suite as root (security 0.84)
- #9873 Defer to system-auth in the polkit stack written by fingerprint/FIDO2 setup (security 0.78)
- #9875 Probe sudo non-interactively so unattended updates cannot hang (security 0.87)
- #9878 Re-apply hardware pacman repos after a refresh restore (security 0.66)
- #9894 Fix Tailscale plugin failing to reconnect when accept-routes is enabled (security 0.76)
- #9909 Track AppImages from GitHub releases and update them daily (security 0.76)
- #9946 Reach the forwarded SSH agent from Herdr panes (security 0.85)
- #9965 Show Bluetooth pairing codes in the Omarchy panel (security 0.89)
- #9995 Pin Helium password store to libsecret (security 0.86)
- #10018 Pin Signal to gnome-libsecret like the browsers (security 0.95)
- #10022 Do not let a migration inherit its path overrides from the caller (security 0.89)
- #10082 Bound lock authentication resource use (security 0.91)
- #10088 Add omarchy-install-blesh for opt-in ble.sh autocompletion (security 0.52)
- #10109 Add a disposable Omarchy lab VM (security 0.54)
- #10110 Add DaVinci Resolve and DaVinci Resolve Studio installers (security 0.80)
- #10113 fix(windows-vm): accept dockur 2777 shared mount mode on launch (security 0.77)
- #10172 Add Ollama Cloud usage collector to the agents panel (security 0.90)
- #10185 Add speech-dispatcher so Brave Web Speech has voices (security 0.50)
- #10219 security: add a disk-unlock duress password that factory-resets (security 0.97)
- #10257 Redact network identifiers from debug output (security 0.61)
- #10262 Snapshot BASHPID before /proc fd walks in windows-vm mounts (security 0.63)
- #10338 Fix the Windows VM refusing to start after its first launch (security 0.78)
- #10346 Pin Electron password store to gnome-libsecret (security 0.56)
- #10393 Cap lock fingerprint retries; skip closed-lid fingerprint; silence sudo/polkit P (security 0.56)
- #10396 Strip password keyring auth from sddm-autologin too (security 0.90)
- #10411 Clear setgid before setting the Windows VM mount modes (security 0.87)
- #10428 Distinguish sudo failure from missing Snapper configs (security 0.57)
- #10435 Add VSCodium as a default editor and installer option (security 0.79)
- #10473 network speedtest: use tokenless Cloudflare endpoints (security 0.78)
- #10602 Fix Wi-Fi password recovery after authentication failure (security 0.90)
- #10610 Add Muse usage collector to the agents panel (security 0.67)
- #10644 Guide an offline first login through terminal network setup (security 0.77)
- #10655 Harden linux-modules-cleanup.service with a systemd drop-in (security 0.87)
- #10689 Fingerprint setup and enrolment as a shell overlay (security 0.94)
- #10717 Report SSH service disable failures before cleanup (security 0.77)
- #10738 Require auth to change system NetworkManager connections (security 0.93)
- #10769 Restrict clipboard history file modes (security 0.93)
- #10824 Add OpenRouter usage collector to the agents panel (security 0.82)
- #10962 Unattended domain join and domain logon for the Windows VM (security 0.96)
- #10974 Rust-first sandboxed Quickshell plugins (security 0.74)
- #10977 Add `omarchy vm`, a disposable Omarchy in QEMU/KVM (security 0.91)
- #11017 Install missing BCM43602 board NVRAM on MacBookPro13,3 (security 0.65)
- #11032 Make Podman native with optional Docker compatibility (security 0.86)
- #11037 Harden FIDO2 setup against cached sudo reuse (security 0.96)
- #11067 Add Qwen Code as a default coding agent (security 0.50)
- #11097 Keep the powerprofilesctl shebang fix applied across daemon upgrades (#11031) (security 0.86)
- #11144 Add Axon as a default coding agent (security 0.73)
- #11172 Add opt-in sudo authentication policy (risk 3.0, security 0.97)
- #11196 Screen time for the child profile, with two modes (security 0.89)
- #11197 Make network speed test resilient with dynamic token fetch and Cloudflare fallba (security 0.81)
- #11242 Install the marketplace-verified snapshot by default in plugin add (security 0.68)
- #11289 Add the headless server edition (security 0.55)
- #11314 System security hardening (security 0.93)
- #11322 Recreate lock screen fingerprint PAM file for pre-quattro setups (security 0.77)
- #11367 Add MiniMax Code (mcode) to the agents panel and default agent switch (security 0.85)
- #11379 Add TPM2-backed PIN authentication for login, sudo, polkit, and lock screen (security 0.96)
- #11381 Install the pre-T2 FaceTime HD camera driver and firmware (risk 3.0, security 0.72)
- #11386 Run development containers with rootless Docker (security 0.90)
- #11388 Sync the pacman databases before the first package install (security 0.50)
- #11423 Install OpenCode V2 through mise's npm backend (security 0.81)
- #11428 Add ZeroTier as an installable service (security 0.90)
- #11438 Support mounting and unlocking internal and LVM-backed storage in UDisks (security 0.95)
- #11444 Add GitLab Duo CLI as a default coding agent (security 0.90)
- #11461 Keep the caller's editor across sudo for vipw and vigr (security 0.94)
- #11470 Run declared plugin cleanup before removal (security 0.75)
- #11471 Open Steam Remote Play ports when installing Steam (security 0.96)
- #11479 Reject root-run updates before changing user state (security 0.85)
- #11565 Scope LocalSend firewall rules to private and local subnets (#11560) (security 0.96)
- #11574 Add expandable hourly rain tables to the weather panel (security 0.76)
- #11612 feat(security): Facelock face unlock for lock screen, sudo, and polkit (risk 3.0, security 0.95)
- #11697 Repair a broken passwordless default keyring before session apps use it (security 0.94)
- #11720 Add eye toggle to reveal the Wi-Fi passphrase (security 0.88)
- #11722 Add llmman to Install > AI and Remove > AI (security 0.64)
- #11725 feat(config): configure gnome-libsecret password store for VS Code (security 0.80)
- #11786 Reclaim pre-4.0 user-owned Plymouth and SDDM theme directories (security 0.94)
- #11804 Tell agents to retry with pkexec when sudo needs a password (security 0.82)
- #11839 feat: add commandcode, qwen audio agent, and colibri to AI installs (security 0.76)
- #11874 Require approval for new USB and Thunderbolt devices by default (security 0.70)
- #11907 Stop Chromium Google OAuth workaround that causes SIGTRAP crashes (security 0.79)
- #11966 Fix captive portal sign-in URL (#11961) (security 0.85)
- #11967 Agents: user collectors + Go connection settings card (security 0.92)
- #11983 Show which processes asked for a polkit password (security 0.62)
- #11984 Explain polkit commands with the default coding agent on request (security 0.51)
- #11989 Add Google Antigravity usage collector and panel integration (security 0.93)
- #12001 Pass Download Video extension tab cookies to yt-dlp (security 0.86)
- #12015 Restore the input group for Voxtype evdev hotkey users (security 0.88)
- #12019 Clear special bits when hardening Windows VM dirs (security 0.89)
- #12059 Run the default agent on another machine (security 0.73)
- #12070 Answer ARP only from the interface that owns the address (security 0.67)
- #12078 Import saved iwd Wi-Fi networks into NetworkManager (security 0.97)
- #12099 Harden sshd: localhost bind, key before listen (risk 3.2, security 0.94)
- #12103 Strip dangerous caps from gsr-kms-server and btop (security 0.94)
- #12105 Intelligently fallback to available agent when default agent has exhausted usage (security 0.57)
- #12110 Fingerprint setup: keep working forks; silent lid-open PAM gate (security 0.83)
- #12111 Harden notification image copies, exec tokens, and hint reads (security 0.64)
- #12155 Fix six reported bugs: bar toggle, hibernation, weather, VM mounts, keybindings  (security 0.74)
- #12159 Harden kernel and network sysctl parameters (security 0.81)
- #12160 Disable core dump generation to prevent memory exposure (security 0.66)
- #12161 Blacklist uncommon network protocols and legacy filesystem modules (security 0.61)
- #12162 Harden SSH client and daemon cryptographic defaults (risk 3.1, security 0.88)
- #12164 Apply sudo session isolation and security flags (security 0.94)
- #12165 Tighten system and authentication file permissions (security 0.96)
- #12167 Add audit rules for sensitive files and privilege changes (security 0.63)
- #12169 Configure default deny firewall rules with UFW (security 0.86)
- #12170 Apply systemd sandboxing drop-ins for core system services (security 0.73)
- #12177 Add 80% battery charge cap toggle (security 0.93)
- #12244 Chromium: overrideable OAuth env and CVE security-floor upgrade (security 0.90)
- #12245 Lock/sleep: fail-closed, clamshell, auth UI, lid focus, logind (security 0.69)
- #12246 Boot: ESP free space, Limine prune, /boot perms, signed upgrade, SDDM keyring (security 0.91)
- #12260 Give third-party plugins their own entry settings and auth service (security 0.58)
- #12264 Windows VM: create launcher after start; clear setgid on harden (security 0.84)
- #12265 Agent usage: config-dir cache key and owner-only modes (security 0.89)
- #12266 Security: id -un sudo grants, TUI desktop escape, Docker DB secrets (security 0.90)
- #12279 Clear the eight-second enterprise Wi-Fi auth timeout (security 0.72)
- #12287 Add the theme marketplace: browse, install and update community themes (security 0.59)
- #12323 Clear setgid when hardening Windows VM directories (security 0.92)
- #12329 Add Remove menu for coding agents (security 0.54)
- #12394 hw: cover all Framework 16 input-module product IDs in qmk_hid udev rule (security 0.51)
- #12459 Add an optional installer for the asciipaper live wallpaper (security 0.56)
- #12475 network: keep passphrase prompt focused through scan reorders (security 0.63)
- #12542 Sort passwd_tries sudoers before user overrides (security 0.87)
- #12582 Add a Cursor collector to the agents panel (security 0.86)
- #12583 Let the Wi-Fi passphrase be read back while typing it (security 0.90)
- #12651 feat(agents): add OpenCode Go usage with V2 support (security 0.87)
- #12698 Add omarchy menu secret for masked secret entry (security 0.83)
- #12715 Finish 1Password install: local polkit owners and MCP setgid (security 0.92)
- #12717 Drive: disk parent, mmcblk/loop names, password lsblk/cancel (security 0.79)
- #12718 Security: refresh-config path, password sync, input names, plugin USER, ldisc, f (security 0.94)
- #12766 Add Bluetooth file receiving to the Bluetooth panel (security 0.69)
- #12788 Add optional AirPods bar integration (security 0.93)
- #12796 Fix omarchy update under sudo: unset OMARCHY_PATH and yay-as-root (security 0.76)
- #12815 Refuse to run the tailscale and sshd setup commands as root (security 0.83)
- #12817 Face authentication: lock screen, sudo and polkit by IR camera (security 0.93)
- #12831 Scope the LocalSend firewall rule to private networks (security 0.96)
- #12836 Install Hermes as the self-updating runtime in every flow (security 0.79)
- #12883 Scope the dev-link secure_path drop-in to the linking user (security 0.91)
- #12888 Abort Tailscale remove when sudo is cancelled (security 0.88)
- #12889 Reuse existing enterprise Wi-Fi profiles on reconnect (security 0.93)
- #12891 Add show/hide toggle to the Wi-Fi passphrase field (security 0.81)
- #12895 Don't add controller users to the input group (security 0.89)
- #12896 Persist XKBLAYOUT for LUKS so non-US layouts stay typeable (security 0.60)
- #12897 Accept device-initiated Bluetooth Just Works pairing (security 0.68)
- #12901 Enable Voxtype GPU backend through sudo (security 0.94)
- #12925 Add a reveal toggle to masked TextFields, wired up for the Wi-Fi passphrase (security 0.68)
- #12957 Keep the update transcript out of world-writable /tmp (security 0.67)
- #12972 Add a camera bar widget that turns every USB camera off (security 0.91)
- #13036 Add Local AI: run the model validated for your GPU and open a coding agent on it (security 0.81)
- #13047 Pin factory-reset elevation to the packaged command (security 0.66)
- #13052 Add a LiteLLM collector for the agents usage panel (security 0.92)
- #13075 Add Cloudflare to Install > Service (security 0.84)
- #13085 Restart bluetoothd and reload btusb when the adapter is wedged (security 0.64)
- #13088 Fix network panel Forget centering, add Cancel for in-flight connects (security 0.69)
- #13098 Default dictation to verified Cohere Vulkan, paste and Atreyu visuals (security 0.52)
- #13101 Actually restart bluetooth.service in omarchy-restart-bluetooth (security 0.68)
- #13106 Skip the Codex app-server probe when there are no credentials (security 0.75)
- #13110 Ship a managed Chromium privacy policy alongside the theme color (security 0.56)
- #13112 Stop broadcasting hostname and permanent MAC on every network (security 0.93)
- #13154 Strip stray special mode bits when hardening Windows VM directories (security 0.85)
- #13183 Add password visibility toggle to lock screen (security 0.62)
- #13187 Setup fingerprint for Validity/Synaptics readers via python-validity (security 0.51)
- #13200 Sign in to captive portals in a dropdown instead of the browser (security 0.58)
- #13213 Clear setgid when hardening Windows VM mount sources (security 0.89)
- #13215 Sync root when updating the user password from the menu (security 0.93)
- #13280 Draft: bound the hotspot to a participant limit (security 0.84)
- #13283 Tell the user when pam_faillock has locked the account (security 0.57)
- #13296 Install OpenClaw as a self-updating copy under ~/.openclaw (security 0.76)
- #13312 Require a per-session token for notification click-exec (security 0.79)
- #13316 Preserve GUM environment records during factory-reset elevation (security 0.90)
- #13362 Converge omarchy-mac and omarchy-mx-mac into upstream Omarchy (risk 3.2, security 0.58)
- #13377 Refuse omarchy-update when invoked as root (security 0.89)
- #13432 Keep a legacy Windows VM password with $$ working after the Quattro migration (security 0.94)
- #13467 Let fingerprint setup adopt an already-enrolled print (security 0.85)
- #13474 Soften yay go-mod caches and warn on AUR update failure (security 0.91)
- #13479 Authorize omarchy-channel-set once for the whole switch (security 0.94)
- #13513 Run a lock hook when the screen locks (security 0.90)
- #13533 Join a self-hosted Tailscale coordination server (security 0.92)
- #13542 Finish fingerprint setup when a print is already enrolled (security 0.75)
- #13548 Add an OpenCode agent usage collector (security 0.87)
- #13563 Add animated installer presentation with embedded interactive controls (security 0.56)
- #13575 Bound the package-install sudo keepalive and revoke it on exit (security 0.96)
- #13612 Configure fingerprint PAM when prints are already enrolled (security 0.58)
- #13616 Keep sudo alive and offer reboot after channel switch (security 0.92)
- #13625 Do not block SDDM autologin on pam_gnome_keyring (security 0.52)
- #13630 Prefer IPP Everywhere when adding network printers (security 0.52)
- #13646 Soften yay go-mod caches and warn on AUR update failure (security 0.91)
- #13652 Drop pam_faillock preauth silent so lockouts are visible (security 0.72)
- #13660 Refuse to run omarchy-update as root (security 0.88)
- #13664 Give each webapp its own Chromium profile (security 0.56)
- #13690 Add region profiles, starting with China's package repositories (security 0.55)
- #13699 Keep other systems' boot entries through a factory reset (security 0.66)
- #13734 Add a sign-in button to the agents panel's auth card (security 0.64)
- #13745 Open the captive portal sign-in page on detection when asked to (security 0.50)
- #13750 Clear setgid when hardening Windows VM mount sources (security 0.91)
- #13763 Add Cloudmail to Install > Service (security 0.62)
- #13770 Switch between several Claude and Codex subscriptions, and build apps the Omarch (security 0.86)
- #13796 Keep an early polkit Enter and submit it when PAM asks (security 0.63)
- #13800 Strip setgid and setuid bits from Windows VM mount directories (#13558) (security 0.93)
- #13811 fix(bluetooth): recover incomplete pairing (security 0.73)
- #13845 Add omp (Oh My Pi) usage collector to the agents panel (security 0.86)
- #13848 [4.0.4/4.0.5] Replace deprecated Gemini CLI with Google Antigravity (#6900) (security 0.56)
- #13856 Launch Claude with a real permission bypass (security 0.88)

## Not in finished form — send back to authors

- #3507 Support theming for multiple Chromium Profiles
- #4962 Replace slashes in worktree path with dashes
- #4990 Add support for Code OSS
- #5011 feat: add smart tmux session management
- #5049 feat: support tmux in terminal cwd detection
- #5055 Add imv keybind to copy current image to clipboard
- #5069 Add single instance option for webapp installs
- #5112 Add Android Studio in dev install and remove menus
- #5148 Support Google Chrome theme color
- #5223 Add zsh support with aliases and shell config
- #5224 Add tmux extended-keys on for complex key bindings
- #5262 add i2c_hid modules to initramfs for laptops with I2C HID keyboards
- #5589 ghui autoreloads oma theme
- #5968 Install ghostty-nautilus for the 'Open in Ghostty' Nautilus extension…
- #5975 Make nightlight temperature configurable via env variables
- #5987 Add condensed mode toggle (SUPER + SHIFT + BACKSPACE)
- #6118 feat(bindings): automatically unbind defaults on override
- #6542 feat: replace provider buttons with dropdown in model usage widget
- #6606 feat: add Helium browser to quattro menu
- #6719 when installing Bitwarden, ask user if it should be used as SSH agent
- #6725 fix: collapse dropdown toggle on second click
- #6980 Add agent security scans for untrusted software
- #7092 fix: Add rocm-smi-lib for AMD GPU support in btop- #4999
- #7129 Fix Voxtype GPU setup failing silently
- #7161 Add Quattro first-boot sizzle clip and source stills
- #7247 Install Grok through mise's first-party registry
- #7297 Correctly name grok and add docs link
- #7463 Fix typo on 04_navigation.md
- #7995 Stage diagnostics logs privately instead of at fixed /tmp paths
- #8408 Theme GTK4 apps with Omarchy colors
- #8421 omarchy-windows-vm: enable windows activation via system firmware by …
- #8472 Omarchy v4.0.2
- #8481 Add OpenCode agent setup: default config, AGENTS.md, and installer
- #8532 Constrain the asdcontrol sudoers rule to hiddev detect/get/set
- #8783 Update 44-mac-support.md to add t2linux wiki link
- #8791 fix(update): guard against missing TMPDIR and support native ChatGPT …
- #8805 Fix grammar in security documentation
- #8829 Add PTL kernel in installation script for all Intel Panther Lake systems
- #8995 Fix additional assorted typos in navigation
- #9424 Replace Em Dash with Arrow
- #9492 #9489 Use correct language code for Norwegian keyboard layout
- #9557 Allow plugins to specify package dependencies (optional + required)
- #9739 Add hyfetch installer and menu entry
- #9741 Add Omarchy spelling correction to Voxtype
- #9806 Support browser flags in web app bindings
- #9815 Tag hotplugged USB dock/hub input devices for seat and enable wakeup
- #9860 Hibernation: fail when unsupported; refuse empty resume= device
- #9865 feat: cycle battery percentage placement
- #9867 docs: add Windows time synchronization fix to dual boot manual
- #9909 Track AppImages from GitHub releases and update them daily
- #10082 Bound lock authentication resource use
- #10172 Add Ollama Cloud usage collector to the agents panel
- #10373 Add SpaceBeach visual time machine and desktop-history game
- #10491 [fix] Sorting packages
- #10550 Add safe opt-in screen shader themes
- #10560 Theme Sublime Text from the Omarchy palette
- #10747 Release v4.0.3
- #10893 Add @kalomarchy as code owner for protected branches
- #10934 menu: navigate with Ctrl+N/Ctrl+P like Up/Down
- #10966 Add lock screen blur settings to shell.json
- #11070 Add LM Studio Bionic to AI menu
- #11314 System security hardening
- #11514 Mise: no forced release-age 0; SSE4.2 agent skip; keep OpenClaw CLI
- #11580 feat(menu): improve launcher with flat search, fuzzy matching, quicklinks, and frecency
- #11945 Align spacing in xcompose emoji
- #11959 Dismiss low-battery notification when charger is connected
- #11989 Add Google Antigravity usage collector and panel integration
- #12104 Validate omarchy-hook names on run and install
- #12114 Bar status: Steam idle-inhibit, Wi-Fi/SSID, Bluetooth alias/pairable
- #12115 Bar panel: audio/OSD/battery/weather/night light, cloned-bar Loader props
- #12165 Tighten system and authentication file permissions
- #12167 Add audit rules for sensitive files and privilege changes
- #12169 Configure default deny firewall rules with UFW
- #12170 Apply systemd sandboxing drop-ins for core system services
- #12244 Chromium: overrideable OAuth env and CVE security-floor upgrade
- #12245 Lock/sleep: fail-closed, clamshell, auth UI, lid focus, logind
- #12246 Boot: ESP free space, Limine prune, /boot perms, signed upgrade, SDDM keyring
- #12247 Theme: dark Yaru icons, bg/next/prev, themed Done logo, noprofile theme-set
- #12248 Perf: disk speedtest staging, batched window pop, in-memory image index
- #12250 Preserve shell.json and config migration file modes
- #12252 Capture/cursors: slurp snap, shot-only hardware cursors, vmwgfx software cursors
- #12263 Monitor: report Hyprland scale and persist named outputs
- #12266 Security: id -un sudo grants, TUI desktop escape, Docker DB secrets
- #12267 Backlight: AIO kernel route and apple-panel-bl priority
- #12268 Terminal logos: theme-colored ascii and fitted fastfetch
- #12269 Workspace layout by name; failing Lua assertions fail the test
- #12271 Sunshine: canonical unit enable and security-floor bump
- #12465 Exit screensaver on keyboard or mouse input
- #12485 feat: sync Starship prompt with active theme
- #12486 feat: sync Herdr multiplexer with active theme
- #12507 Add interactive stepped background alignment and slideshow transition controls to image-pi
- #12681 [Intel Mac P03] Consolidate Apple hardware detection
- #12682 [Intel Mac P04] Consolidate lid handling and display classification
- #12683 [Intel Mac P05] Handle ghost internal displays
- #12684 [Intel Mac P06] Retire the legacy SPI package alongside T1Bridge
- #12687 [Intel Mac P09] Consolidate NVMe suspend applicability
- #12688 [Intel Mac P10] Consolidate Broadcom calibration and sleep recovery
- #12689 [Intel Mac P11] Consolidate model-specific Cirrus audio support
- #12691 [Intel Mac P13] Consolidate the Intel Mac kernel migration policy
- #12717 Drive: disk parent, mmcblk/loop names, password lsblk/cancel
- #12718 Security: refresh-config path, password sync, input names, plugin USER, ldisc, first-run s
- #12730 Share QR, presentation mode, multi-monitor screensaver
- #12823 Add configurable short-term menu navigation memory
- #12883 Scope the dev-link secure_path drop-in to the linking user
- #13003 Document Dell power recovery configuration
- #13309 Add LibreWolf as supported browser
- #13366 Fix typo in navigation section of the manual
- #13605 Persist monitor scale to the focused output rule
- #13606 Stop Launching OSD from sticking after app launch
- #13607 Seed Codex auto-review in config.toml to keep shared server
- #13608 Make Elsewhen migration bar put best-effort on shell timeouts
- #13609 Keep connected Bluetooth devices with address-like names
- #13624 Keep keyboard focus on fullscreen Proton games
