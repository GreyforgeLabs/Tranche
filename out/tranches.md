# Tranche — PR review candidates

Corpus: 2836 observed open PRs; 2836 matching judgments; 0 unjudged/stale; 0 unbound legacy judgments.
Review candidates: 610. Model-consistent groups: 88. Groups needing relationship review: 10. Security-priority items: 378 (meta-category, reviewed first).

Evidence: titles and shortened descriptions (1200 characters per PR; 400 per pair). Diffstat is unknown unless captured input supplies it. Patches, CI, reproductions, fix coverage and security have not been verified. Model scores are suggestions, not calibrated guarantees or approval to merge/close. Pagination records an observation, not a point-in-time GitHub snapshot.

## Security review — top priority (meta-category)

These PRs touch credentials, remote code execution, sudo/permissions, network
exposure or crypto material (model probability ≥ 0.5). Review before any category batch.

| PR | Title | Author | Model finished | Model effort | Model fix |
|---|---|---|---|---|---|
| [#9459](https://github.com/omacom/omarchy/pull/9459) | [codex] OM-SEC-03: Remove public Windows VM default credentials | AFOliveira | 1.5 | 2.9 | 0.66 |
| [#9464](https://github.com/omacom/omarchy/pull/9464) | [codex] OM-SEC-09: Generate private credentials for development databases | AFOliveira | 2.4 | 2.9 | 0.24 |
| [#9750](https://github.com/omacom/omarchy/pull/9750) | Kids mode: child installs with a kid password and a parent password | peterholko | 1.0 | 3.0 | 0.04 |
| [#10219](https://github.com/omacom/omarchy/pull/10219) | security: add a disk-unlock duress password that factory-resets | calebdw | 1.1 | 3.0 | 0.04 |
| [#7435](https://github.com/omacom/omarchy/pull/7435) | Add Wi-Fi hotspot hosting to the network panel | ujo4eva | 1.0 | 3.0 | 0.03 |
| [#11172](https://github.com/omacom/omarchy/pull/11172) | Add opt-in sudo authentication policy | shelldandy | 1.2 | 3.0 | 0.08 |
| [#11379](https://github.com/omacom/omarchy/pull/11379) | Add TPM2-backed PIN authentication for login, sudo, polkit, and lock screen | LoboHacks | 1.2 | 3.0 | 0.05 |
| [#12078](https://github.com/omacom/omarchy/pull/12078) | Import saved iwd Wi-Fi networks into NetworkManager | oliverox | 1.1 | 2.6 | 0.58 |
| [#5035](https://github.com/omacom/omarchy/pull/5035) | Prevent empty passwords in omarchy-drive-set-password | marko-builds | 1.1 | 1.2 | 0.96 |
| [#7828](https://github.com/omacom/omarchy/pull/7828) | Add "Join hidden network" to the Wi-Fi panel | verkligheten | 2.2 | 1.9 | 0.07 |
| [#8532](https://github.com/omacom/omarchy/pull/8532) | Constrain the asdcontrol sudoers rule to hiddev detect/get/set | marty-schneider | 1.0 | 1.9 | 0.87 |
| [#8534](https://github.com/omacom/omarchy/pull/8534) | Take privileged usernames from id -un, not USER | marty-schneider | 1.1 | 1.8 | 0.97 |
| [#10962](https://github.com/omacom/omarchy/pull/10962) | Unattended domain join and domain logon for the Windows VM | ekollof | 1.0 | 3.0 | 0.04 |
| [#11037](https://github.com/omacom/omarchy/pull/11037) | Harden FIDO2 setup against cached sudo reuse | ErikMelton | 1.2 | 2.7 | 0.81 |
| [#11438](https://github.com/omacom/omarchy/pull/11438) | Support mounting and unlocking internal and LVM-backed storage in UDisks | 2fd5 | 1.1 | 2.1 | 0.24 |
| [#11471](https://github.com/omacom/omarchy/pull/11471) | Open Steam Remote Play ports when installing Steam | kh4rit-bot | 1.1 | 1.2 | 0.79 |
| [#11565](https://github.com/omacom/omarchy/pull/11565) | Scope LocalSend firewall rules to private and local subnets (#11560) | Cid-oe | 1.1 | 1.8 | 0.94 |
| [#12099](https://github.com/omacom/omarchy/pull/12099) | Harden sshd: localhost bind, key before listen | Chessing234 | 1.9 | 2.1 | 0.44 |
| [#12165](https://github.com/omacom/omarchy/pull/12165) | Tighten system and authentication file permissions | kairosci | 1.0 | 1.9 | 0.42 |
| [#12831](https://github.com/omacom/omarchy/pull/12831) | Scope the LocalSend firewall rule to private networks | taufderl | 2.4 | 1.0 | 0.85 |
| [#13575](https://github.com/omacom/omarchy/pull/13575) | Bound the package-install sudo keepalive and revoke it on exit | Arash-Afshar | 2.5 | 1.7 | 0.90 |
| [#7272](https://github.com/omacom/omarchy/pull/7272) | Switch between subscription accounts | omarchybot | 1.0 | 3.0 | 0.07 |
| [#7274](https://github.com/omacom/omarchy/pull/7274) | Add a Kimi usage collector to the agents panel | sorenmat | 1.0 | 2.3 | 0.04 |
| [#7455](https://github.com/omacom/omarchy/pull/7455) | Read Fireworks credentials from pi's auth.json | TyRichards | 1.2 | 1.9 | 0.68 |
| [#8889](https://github.com/omacom/omarchy/pull/8889) | Apply uinput permissions through tmpfiles | yashranaway | 2.0 | 1.6 | 0.93 |
| [#9043](https://github.com/omacom/omarchy/pull/9043) | Authorize SSH keys into the invoking user's home | PyRo1121 | 2.1 | 1.4 | 0.97 |
| [#9221](https://github.com/omacom/omarchy/pull/9221) | Add AirPlay audio output | jtsiros | 2.2 | 2.0 | 0.14 |
| [#9239](https://github.com/omacom/omarchy/pull/9239) | Sync the GNOME keyring on user password changes | hudsonwa | 1.1 | 2.0 | 0.95 |
| [#9248](https://github.com/omacom/omarchy/pull/9248) | Add managed account website allowlists | redreceipt | 1.6 | 3.0 | 0.03 |
| [#9463](https://github.com/omacom/omarchy/pull/9463) | [codex] OM-SEC-08: Publish SSH only after proving key-only access | AFOliveira | 1.0 | 3.0 | 0.77 |
| [#9470](https://github.com/omacom/omarchy/pull/9470) | [codex] OM-SEC-15: Keep mixed-trust installers outside sudo lifetime | AFOliveira | 1.2 | 3.0 | 0.81 |
| [#9477](https://github.com/omacom/omarchy/pull/9477) | [codex] OM-SEC-23: Keep debug collectors outside dmesg authorization | AFOliveira | 1.5 | 3.0 | 0.57 |
| [#10018](https://github.com/omacom/omarchy/pull/10018) | Pin Signal to gnome-libsecret like the browsers | hudsonwa | 1.2 | 2.0 | 0.94 |
| [#10689](https://github.com/omacom/omarchy/pull/10689) | Fingerprint setup and enrolment as a shell overlay | inauman | 1.0 | 3.0 | 0.04 |
| [#11314](https://github.com/omacom/omarchy/pull/11314) | System security hardening | kairosci | 1.0 | 3.0 | 0.06 |
| [#11612](https://github.com/omacom/omarchy/pull/11612) | feat(security): Facelock face unlock for lock screen, sudo, and polkit | GianlucaMinoprio | 2.0 | 3.0 | 0.07 |
| [#11697](https://github.com/omacom/omarchy/pull/11697) | Repair a broken passwordless default keyring before session apps use it | Chessing234 | 1.7 | 2.3 | 0.93 |
| [#12164](https://github.com/omacom/omarchy/pull/12164) | Apply sudo session isolation and security flags | kairosci | 1.0 | 1.8 | 0.14 |
| [#12718](https://github.com/omacom/omarchy/pull/12718) | Security: refresh-config path, password sync, input names, plugin USER, ldisc, f | Chessing234 | 0.9 | 2.9 | 0.86 |
| [#12817](https://github.com/omacom/omarchy/pull/12817) | Face authentication: lock screen, sudo and polkit by IR camera | mellismas | 1.0 | 3.0 | 0.03 |
| [#12901](https://github.com/omacom/omarchy/pull/12901) | Enable Voxtype GPU backend through sudo | Chessing234 | 1.7 | 1.2 | 0.85 |
| [#13432](https://github.com/omacom/omarchy/pull/13432) | Keep a legacy Windows VM password with $$ working after the Quattro migration | omarchybot | 1.1 | 1.1 | 0.95 |
| [#13479](https://github.com/omacom/omarchy/pull/13479) | Authorize omarchy-channel-set once for the whole switch | AnPod | 1.3 | 2.4 | 0.92 |
| [#6736](https://github.com/omacom/omarchy/pull/6736) | Docker multi-arch build with sudo support | axelfontaine | 2.5 | 2.2 | 0.87 |
| [#7501](https://github.com/omacom/omarchy/pull/7501) | Apply session monitor scale to the SDDM greeter | calledtoconstruct | 2.0 | 2.6 | 0.72 |
| [#7814](https://github.com/omacom/omarchy/pull/7814) | Add encrypted, versioned, off-site backups | achevalier-dev | 1.0 | 3.0 | 0.03 |
| [#7990](https://github.com/omacom/omarchy/pull/7990) | Clear passwordless sudo grants at boot | Adolanium | 1.1 | 2.0 | 0.93 |
| [#9474](https://github.com/omacom/omarchy/pull/9474) | [codex] OM-SEC-19: Protect migration and SSH setup authorization | AFOliveira | 1.2 | 3.0 | 0.86 |
| [#9573](https://github.com/omacom/omarchy/pull/9573) | Judge the invoking user's authorized keys when removing SSH access | shaynhornik | 2.1 | 1.5 | 0.96 |
| [#9605](https://github.com/omacom/omarchy/pull/9605) | Clear set-ID bits when securing the Windows VM mount sources | omarchybot | 1.1 | 1.6 | 0.97 |
| [#11461](https://github.com/omacom/omarchy/pull/11461) | Keep the caller's editor across sudo for vipw and vigr | photuris | 1.2 | 1.9 | 0.92 |
| [#11989](https://github.com/omacom/omarchy/pull/11989) | Add Google Antigravity usage collector and panel integration | steph4n-gh | 1.0 | 2.8 | 0.03 |
| [#12103](https://github.com/omacom/omarchy/pull/12103) | Strip dangerous caps from gsr-kms-server and btop | Chessing234 | 1.0 | 2.0 | 0.68 |
| [#12246](https://github.com/omacom/omarchy/pull/12246) | Boot: ESP free space, Limine prune, /boot perms, signed upgrade, SDDM keyring | Chessing234 | 1.0 | 2.8 | 0.45 |
| [#12266](https://github.com/omacom/omarchy/pull/12266) | Security: id -un sudo grants, TUI desktop escape, Docker DB secrets | Chessing234 | 0.7 | 2.7 | 0.67 |
| [#12788](https://github.com/omacom/omarchy/pull/12788) | Add optional AirPods bar integration | artinlenz | 2.0 | 3.0 | 0.03 |
| [#13215](https://github.com/omacom/omarchy/pull/13215) | Sync root when updating the user password from the menu | Chessing234 | 1.8 | 1.0 | 0.91 |
| [#13800](https://github.com/omacom/omarchy/pull/13800) | Strip setgid and setuid bits from Windows VM mount directories (#13558) | szaidi-code | 1.0 | 1.1 | 0.92 |
| [#6647](https://github.com/omacom/omarchy/pull/6647) | Add local and remote Hermes usage sources to Agents panel | okurmustafa | 1.0 | 3.0 | 0.04 |
| [#7417](https://github.com/omacom/omarchy/pull/7417) | Add NetBird mesh VPN integration | stijoh | 1.0 | 3.0 | 0.02 |
| [#8326](https://github.com/omacom/omarchy/pull/8326) | Read Claude limits with a sibling CLI's token when the saved one lapsed | lepht | 1.4 | 2.0 | 0.75 |
| [#9465](https://github.com/omacom/omarchy/pull/9465) | [codex] OM-SEC-10: Replace the world-writable installer log | AFOliveira | 1.2 | 3.0 | 0.82 |
| [#9475](https://github.com/omacom/omarchy/pull/9475) | [codex] OM-SEC-21: Authenticate only after package picker code exits | AFOliveira | 1.1 | 2.9 | 0.68 |
| [#9700](https://github.com/omacom/omarchy/pull/9700) | Seed Chromium's first-run preferences with a mode the browser can read | shaynhornik | 1.1 | 1.0 | 0.95 |
| [#9783](https://github.com/omacom/omarchy/pull/9783) | Fix Windows VM helper rejecting setgid source directories | ekollof | 1.1 | 2.0 | 0.97 |
| [#10602](https://github.com/omacom/omarchy/pull/10602) | Fix Wi-Fi password recovery after authentication failure | cristianbica | 2.9 | 1.9 | 0.98 |
| [#10738](https://github.com/omacom/omarchy/pull/10738) | Require auth to change system NetworkManager connections | danjonesio | 1.9 | 1.0 | 0.63 |
| [#10769](https://github.com/omacom/omarchy/pull/10769) | Restrict clipboard history file modes | danjonesio | 2.9 | 1.8 | 0.90 |
| [#10977](https://github.com/omacom/omarchy/pull/10977) | Add `omarchy vm`, a disposable Omarchy in QEMU/KVM | jankeesvw | 1.1 | 3.0 | 0.03 |
| [#11786](https://github.com/omacom/omarchy/pull/11786) | Reclaim pre-4.0 user-owned Plymouth and SDDM theme directories | Chessing234 | 1.8 | 2.0 | 0.93 |
| [#11967](https://github.com/omacom/omarchy/pull/11967) | Agents: user collectors + Go connection settings card | washburnello | 1.1 | 2.8 | 0.05 |
| [#12177](https://github.com/omacom/omarchy/pull/12177) | Add 80% battery charge cap toggle | Per0-1 | 2.1 | 2.1 | 0.04 |
| [#12244](https://github.com/omacom/omarchy/pull/12244) | Chromium: overrideable OAuth env and CVE security-floor upgrade | Chessing234 | 1.0 | 2.3 | 0.29 |
| [#12715](https://github.com/omacom/omarchy/pull/12715) | Finish 1Password install: local polkit owners and MCP setgid | Chessing234 | 1.5 | 1.9 | 0.82 |
| [#12888](https://github.com/omacom/omarchy/pull/12888) | Abort Tailscale remove when sudo is cancelled | Chessing234 | 1.9 | 1.7 | 0.97 |
| [#12889](https://github.com/omacom/omarchy/pull/12889) | Reuse existing enterprise Wi-Fi profiles on reconnect | Chessing234 | 1.9 | 2.2 | 0.89 |
| [#13052](https://github.com/omacom/omarchy/pull/13052) | Add a LiteLLM collector for the agents usage panel | brynnjocelyn | 1.2 | 2.1 | 0.04 |
| [#13112](https://github.com/omacom/omarchy/pull/13112) | Stop broadcasting hostname and permanent MAC on every network | surim0n | 1.7 | 2.1 | 0.25 |
| [#13533](https://github.com/omacom/omarchy/pull/13533) | Join a self-hosted Tailscale coordination server | z23 | 1.3 | 2.1 | 0.65 |
| [#13616](https://github.com/omacom/omarchy/pull/13616) | Keep sudo alive and offer reboot after channel switch | AnPod | 1.8 | 1.9 | 0.92 |
| [#8014](https://github.com/omacom/omarchy/pull/8014) | Keep Wi-Fi password entry stable during scans | jeremydixon22 | 2.8 | 2.0 | 0.86 |
| [#8251](https://github.com/omacom/omarchy/pull/8251) | Add a copy action for the revealed wifi password | pastawithpesto | 2.3 | 1.2 | 0.04 |
| [#8294](https://github.com/omacom/omarchy/pull/8294) | Add Wi-Fi QR code scanning | icehunt | 2.1 | 2.7 | 0.03 |
| [#8831](https://github.com/omacom/omarchy/pull/8831) | Allow IGMP so multicast group queries stop flooding the firewall log | pixelpush-io | 1.9 | 1.0 | 0.75 |
| [#9506](https://github.com/omacom/omarchy/pull/9506) | Keep SSH setup from disabling passwords on a writable home | mark-groves | 1.3 | 1.1 | 0.94 |
| [#9597](https://github.com/omacom/omarchy/pull/9597) | Add MiniMax Token Plan support | McoreD | 1.1 | 3.0 | 0.04 |
| [#9875](https://github.com/omacom/omarchy/pull/9875) | Probe sudo non-interactively so unattended updates cannot hang | konsorsiumai | 1.9 | 1.6 | 0.96 |
| [#10082](https://github.com/omacom/omarchy/pull/10082) | Bound lock authentication resource use | vip32 | 1.0 | 2.9 | 0.54 |
| [#10396](https://github.com/omacom/omarchy/pull/10396) | Strip password keyring auth from sddm-autologin too | calledtoconstruct | 1.0 | 1.6 | 0.90 |
| [#11196](https://github.com/omacom/omarchy/pull/11196) | Screen time for the child profile, with two modes | jankeesvw | 1.0 | 3.0 | 0.03 |
| [#11386](https://github.com/omacom/omarchy/pull/11386) | Run development containers with rootless Docker | acrogenesis | 1.0 | 3.0 | 0.10 |
| [#11428](https://github.com/omacom/omarchy/pull/11428) | Add ZeroTier as an installable service | Michallote | 1.3 | 1.9 | 0.03 |
| [#12162](https://github.com/omacom/omarchy/pull/12162) | Harden SSH client and daemon cryptographic defaults | kairosci | 1.0 | 1.9 | 0.12 |
| [#12265](https://github.com/omacom/omarchy/pull/12265) | Agent usage: config-dir cache key and owner-only modes | Chessing234 | 2.0 | 2.1 | 0.88 |
| [#12323](https://github.com/omacom/omarchy/pull/12323) | Clear setgid when hardening Windows VM directories | atoslins | 1.7 | 1.8 | 0.97 |
| [#12583](https://github.com/omacom/omarchy/pull/12583) | Let the Wi-Fi passphrase be read back while typing it | fazzledev | 1.1 | 1.8 | 0.19 |
| [#12883](https://github.com/omacom/omarchy/pull/12883) | Scope the dev-link secure_path drop-in to the linking user | taufderl | 1.0 | 1.1 | 0.66 |
| [#12895](https://github.com/omacom/omarchy/pull/12895) | Don't add controller users to the input group | taufderl | 1.9 | 1.0 | 0.84 |
| [#12972](https://github.com/omacom/omarchy/pull/12972) | Add a camera bar widget that turns every USB camera off | GustavoBelo | 1.1 | 2.8 | 0.04 |
| [#13474](https://github.com/omacom/omarchy/pull/13474) | Soften yay go-mod caches and warn on AUR update failure | AnPod | 2.5 | 1.8 | 0.94 |
| [#13513](https://github.com/omacom/omarchy/pull/13513) | Run a lock hook when the screen locks | kisom | 2.0 | 1.9 | 0.32 |
| [#13750](https://github.com/omacom/omarchy/pull/13750) | Clear setgid when hardening Windows VM mount sources | dhiasalhiQ | 1.4 | 1.3 | 0.96 |
| [#7913](https://github.com/omacom/omarchy/pull/7913) | Add maker install group with ESP32/ESP-IDF toolchain setup | JoseEchave | 1.1 | 2.8 | 0.04 |
| [#8169](https://github.com/omacom/omarchy/pull/8169) | Stop apply-system reruns leaving the install log world-writable | Adolanium | 1.1 | 1.0 | 0.96 |
| [#8336](https://github.com/omacom/omarchy/pull/8336) | Add face authentication (howdy) to the lock screen | krismach | 1.0 | 3.0 | 0.03 |
| [#10172](https://github.com/omacom/omarchy/pull/10172) | Add Ollama Cloud usage collector to the agents panel | DanteCpp | 1.0 | 2.3 | 0.03 |
| [#11444](https://github.com/omacom/omarchy/pull/11444) | Add GitLab Duo CLI as a default coding agent | vglafirov | 1.0 | 2.4 | 0.04 |
| [#11725](https://github.com/omacom/omarchy/pull/11725) | feat(config): configure gnome-libsecret password store for VS Code | SantoshTunga | 1.4 | 1.4 | 0.63 |
| [#11804](https://github.com/omacom/omarchy/pull/11804) | Tell agents to retry with pkexec when sudo needs a password | cristim | 2.0 | 1.0 | 0.46 |
| [#13316](https://github.com/omacom/omarchy/pull/13316) | Preserve GUM environment records during factory-reset elevation | AFOliveira | 2.0 | 1.9 | 0.90 |
| [#13770](https://github.com/omacom/omarchy/pull/13770) | Switch between several Claude and Codex subscriptions, and build apps the Omarch | dhh | 1.0 | 3.0 | 0.03 |
| [#9307](https://github.com/omacom/omarchy/pull/9307) | Clarify that "grab key from github" in sshd setup authorizes EVERY machine that  | simonallfrey | 1.4 | 1.9 | 0.46 |
| [#9965](https://github.com/omacom/omarchy/pull/9965) | Show Bluetooth pairing codes in the Omarchy panel | Zhaoyikaiii | 1.4 | 3.0 | 0.30 |
| [#9995](https://github.com/omacom/omarchy/pull/9995) | Pin Helium password store to libsecret | Ahmed-Sinkeat | 1.8 | 2.0 | 0.24 |
| [#10022](https://github.com/omacom/omarchy/pull/10022) | Do not let a migration inherit its path overrides from the caller | DanDreadless | 1.1 | 1.4 | 0.55 |
| [#10411](https://github.com/omacom/omarchy/pull/10411) | Clear setgid before setting the Windows VM mount modes | srikat | 1.4 | 1.1 | 0.97 |
| [#11032](https://github.com/omacom/omarchy/pull/11032) | Make Podman native with optional Docker compatibility | acrogenesis | 1.0 | 3.0 | 0.04 |
| [#11720](https://github.com/omacom/omarchy/pull/11720) | Add eye toggle to reveal the Wi-Fi passphrase | cristim | 2.8 | 1.3 | 0.07 |
| [#12542](https://github.com/omacom/omarchy/pull/12542) | Sort passwd_tries sudoers before user overrides | paulogeyer | 2.3 | 1.4 | 0.90 |
| [#12651](https://github.com/omacom/omarchy/pull/12651) | feat(agents): add OpenCode Go usage with V2 support | felixzsh | 1.1 | 3.0 | 0.07 |
| [#13377](https://github.com/omacom/omarchy/pull/13377) | Refuse omarchy-update when invoked as root | Chessing234 | 1.8 | 1.0 | 0.96 |
| [#13646](https://github.com/omacom/omarchy/pull/13646) | Soften yay go-mod caches and warn on AUR update failure | AnPod | 1.8 | 1.3 | 0.91 |
| [#13660](https://github.com/omacom/omarchy/pull/13660) | Refuse to run omarchy-update as root | AnPod | 1.8 | 1.0 | 0.94 |
| [#5284](https://github.com/omacom/omarchy/pull/5284) | Add NuPhy Air75 V3 keyboard support | felipe3dfx | 1.1 | 2.9 | 0.18 |
| [#7051](https://github.com/omacom/omarchy/pull/7051) | Add Synthetic Labs quotas to the agents panel | aserper | 1.4 | 2.4 | 0.04 |
| [#8441](https://github.com/omacom/omarchy/pull/8441) | Pin Cursor password store to gnome-libsecret so GitHub login can use the OS keyr | MrBazzieB | 1.1 | 2.0 | 0.75 |
| [#8487](https://github.com/omacom/omarchy/pull/8487) | Add openzoo as a coding agent option: claude code, no api key, pays per call | staccDOTsol | 1.1 | 1.9 | 0.03 |
| [#9319](https://github.com/omacom/omarchy/pull/9319) | Give the Secret portal a provider so Chromium can open its password store | wombatoperator | 1.2 | 1.1 | 0.91 |
| [#9723](https://github.com/omacom/omarchy/pull/9723) | Add an embedded dev-env for ESP32 and Arduino boards | HugoluizMTB | 1.2 | 2.2 | 0.09 |
| [#9946](https://github.com/omacom/omarchy/pull/9946) | Reach the forwarded SSH agent from Herdr panes | chriopter | 1.1 | 3.0 | 0.50 |
| [#10655](https://github.com/omacom/omarchy/pull/10655) | Harden linux-modules-cleanup.service with a systemd drop-in | surim0n | 2.2 | 2.6 | 0.73 |
| [#12015](https://github.com/omacom/omarchy/pull/12015) | Restore the input group for Voxtype evdev hotkey users | kurenn | 1.4 | 1.1 | 0.96 |
| [#12815](https://github.com/omacom/omarchy/pull/12815) | Refuse to run the tailscale and sshd setup commands as root | troelsim | 2.5 | 1.2 | 0.94 |
| [#13213](https://github.com/omacom/omarchy/pull/13213) | Clear setgid when hardening Windows VM mount sources | naseebnaushad | 2.5 | 1.0 | 0.97 |
| [#13467](https://github.com/omacom/omarchy/pull/13467) | Let fingerprint setup adopt an already-enrolled print | AnPod | 1.5 | 1.1 | 0.96 |
| [#13548](https://github.com/omacom/omarchy/pull/13548) | Add an OpenCode agent usage collector | bitbonsai | 1.2 | 2.3 | 0.06 |
| [#13845](https://github.com/omacom/omarchy/pull/13845) | Add omp (Oh My Pi) usage collector to the agents panel | Bekkenes | 1.0 | 2.0 | 0.04 |
| [#4997](https://github.com/omacom/omarchy/pull/4997) | Add NetBird as optional VPN service | n0pashkov | 1.2 | 2.0 | 0.02 |
| [#5545](https://github.com/omacom/omarchy/pull/5545) | Stop package install flows after aborts or failures | afurm | 1.7 | 2.0 | 0.96 |
| [#8472](https://github.com/omacom/omarchy/pull/8472) | Omarchy v4.0.2 | ryanrhughes | 1.0 | 3.0 | 0.59 |
| [#8709](https://github.com/omacom/omarchy/pull/8709) | fix: arm signature verification for the T2 repo and close the quattro override w | rmacy | 1.7 | 2.2 | 0.90 |
| [#9460](https://github.com/omacom/omarchy/pull/9460) | [codex] OM-SEC-04: Require package authenticity during Quattro | AFOliveira | 2.0 | 2.6 | 0.39 |
| [#12110](https://github.com/omacom/omarchy/pull/12110) | Fingerprint setup: keep working forks; silent lid-open PAM gate | Chessing234 | 1.5 | 2.1 | 0.82 |
| [#12169](https://github.com/omacom/omarchy/pull/12169) | Configure default deny firewall rules with UFW | kairosci | 1.0 | 1.3 | 0.11 |
| [#12582](https://github.com/omacom/omarchy/pull/12582) | Add a Cursor collector to the agents panel | markxiong0122 | 1.3 | 2.1 | 0.03 |
| [#5431](https://github.com/omacom/omarchy/pull/5431) | feat(hardware): sync ThinkBook mute LEDs with WirePlumber state | Dev-solder124 | 1.1 | 2.2 | 0.22 |
| [#7087](https://github.com/omacom/omarchy/pull/7087) | Add Cursor usage collector to the agents panel | AndrijaSkontra | 2.3 | 2.9 | 0.05 |
| [#8019](https://github.com/omacom/omarchy/pull/8019) | Eye toggle to show/hide the Wi-Fi password | lethaale | 1.0 | 1.2 | 0.11 |
| [#8707](https://github.com/omacom/omarchy/pull/8707) | Set Tailscale operator for Taildrop | Elshayib | 2.4 | 1.0 | 0.96 |
| [#10717](https://github.com/omacom/omarchy/pull/10717) | Report SSH service disable failures before cleanup | yashranaway | 2.0 | 1.1 | 0.94 |
| [#10824](https://github.com/omacom/omarchy/pull/10824) | Add OpenRouter usage collector to the agents panel | Azonnali | 1.1 | 2.2 | 0.13 |
| [#11097](https://github.com/omacom/omarchy/pull/11097) | Keep the powerprofilesctl shebang fix applied across daemon upgrades (#11031) | sandmor | 1.1 | 2.0 | 0.97 |
| [#11479](https://github.com/omacom/omarchy/pull/11479) | Reject root-run updates before changing user state | yashranaway | 2.3 | 1.3 | 0.95 |
| [#11966](https://github.com/omacom/omarchy/pull/11966) | Fix captive portal sign-in URL (#11961) | thescurry | 2.1 | 1.7 | 0.96 |
| [#12001](https://github.com/omacom/omarchy/pull/12001) | Pass Download Video extension tab cookies to yt-dlp | j-c-m | 1.1 | 1.9 | 0.77 |
| [#13856](https://github.com/omacom/omarchy/pull/13856) | Launch Claude with a real permission bypass | Chessing234 | 1.2 | 1.2 | 0.73 |
| [#5744](https://github.com/omacom/omarchy/pull/5744) | feat: Add installer for official Obsidian CLI | yugal1107 | 1.6 | 1.2 | 0.13 |
| [#7040](https://github.com/omacom/omarchy/pull/7040) | feat(security): Add face authentication setup and removal commands | tyvsmith | 1.0 | 2.9 | 0.03 |
| [#9834](https://github.com/omacom/omarchy/pull/9834) | Refuse to run the shell suite as root | maralcbr | 1.9 | 1.3 | 0.86 |
| [#9873](https://github.com/omacom/omarchy/pull/9873) | Defer to system-auth in the polkit stack written by fingerprint/FIDO2 setup | Wheel-Smith | 1.1 | 1.3 | 0.96 |
| [#10338](https://github.com/omacom/omarchy/pull/10338) | Fix the Windows VM refusing to start after its first launch | shilai-li | 1.1 | 1.4 | 0.97 |
| [#11322](https://github.com/omacom/omarchy/pull/11322) | Recreate lock screen fingerprint PAM file for pre-quattro setups | RobertStevenson | 1.8 | 1.6 | 0.94 |
| [#12019](https://github.com/omacom/omarchy/pull/12019) | Clear special bits when hardening Windows VM dirs | ram-devv1 | 2.3 | 1.3 | 0.97 |
| [#12698](https://github.com/omacom/omarchy/pull/12698) | Add omarchy menu secret for masked secret entry | hrnbld | 1.9 | 1.3 | 0.06 |
| [#12717](https://github.com/omacom/omarchy/pull/12717) | Drive: disk parent, mmcblk/loop names, password lsblk/cancel | Chessing234 | 1.0 | 2.7 | 0.85 |
| [#11367](https://github.com/omacom/omarchy/pull/11367) | Add MiniMax Code (mcode) to the agents panel and default agent switch | joshleblanc | 1.0 | 2.7 | 0.03 |
| [#11423](https://github.com/omacom/omarchy/pull/11423) | Install OpenCode V2 through mise's npm backend | AndreasHald | 1.1 | 2.3 | 0.34 |
| [#11907](https://github.com/omacom/omarchy/pull/11907) | Stop Chromium Google OAuth workaround that causes SIGTRAP crashes | AndrijaSkontra | 1.6 | 2.0 | 0.96 |
| [#12155](https://github.com/omacom/omarchy/pull/12155) | Fix six reported bugs: bar toggle, hibernation, weather, VM mounts, keybindings  | merkhanov | 1.6 | 2.6 | 0.98 |
| [#12264](https://github.com/omacom/omarchy/pull/12264) | Windows VM: create launcher after start; clear setgid on harden | Chessing234 | 0.7 | 2.3 | 0.54 |
| [#13036](https://github.com/omacom/omarchy/pull/13036) | Add Local AI: run the model validated for your GPU and open a coding agent on it | 0xSero | 1.5 | 3.0 | 0.03 |
| [#13075](https://github.com/omacom/omarchy/pull/13075) | Add Cloudflare to Install > Service | yamz8 | 2.0 | 1.8 | 0.04 |
| [#13154](https://github.com/omacom/omarchy/pull/13154) | Strip stray special mode bits when hardening Windows VM directories | MehrshadFb | 2.0 | 1.0 | 0.97 |
| [#13280](https://github.com/omacom/omarchy/pull/13280) | Draft: bound the hotspot to a participant limit | ujo4eva | 1.0 | 2.6 | 0.17 |
| [#6980](https://github.com/omacom/omarchy/pull/6980) | Add agent security scans for untrusted software | cempack | 1.0 | 3.0 | 0.05 |
| [#8065](https://github.com/omacom/omarchy/pull/8065) | Add OpenCode Go usage collector for the agents panel | rechedev9 | 1.1 | 2.2 | 0.03 |
| [#10113](https://github.com/omacom/omarchy/pull/10113) | fix(windows-vm): accept dockur 2777 shared mount mode on launch | lushprey | 1.7 | 1.5 | 0.96 |
| [#11197](https://github.com/omacom/omarchy/pull/11197) | Make network speed test resilient with dynamic token fetch and Cloudflare fallba | harshithnadig | 1.4 | 2.3 | 0.83 |
| [#12159](https://github.com/omacom/omarchy/pull/12159) | Harden kernel and network sysctl parameters | kairosci | 1.0 | 2.1 | 0.08 |
| [#12891](https://github.com/omacom/omarchy/pull/12891) | Add show/hide toggle to the Wi-Fi passphrase field | rewisch | 2.3 | 1.2 | 0.09 |
| [#7537](https://github.com/omacom/omarchy/pull/7537) | Show limits for OpenCode's OpenAI account | oorestisime | 2.4 | 2.2 | 0.16 |
| [#8130](https://github.com/omacom/omarchy/pull/8130) | Stop NordVPN installation after setup failure | llirik0 | 2.3 | 1.4 | 0.96 |
| [#9511](https://github.com/omacom/omarchy/pull/9511) | Support non-interactive updates with --yes | zerone0x | 2.0 | 2.5 | 0.27 |
| [#10644](https://github.com/omacom/omarchy/pull/10644) | Guide an offline first login through terminal network setup | NickThompson42 | 1.1 | 2.1 | 0.39 |
| [#12170](https://github.com/omacom/omarchy/pull/12170) | Apply systemd sandboxing drop-ins for core system services | kairosci | 1.0 | 2.3 | 0.08 |
| [#12836](https://github.com/omacom/omarchy/pull/12836) | Install Hermes as the self-updating runtime in every flow | spencerbull | 1.4 | 2.9 | 0.60 |
| [#13542](https://github.com/omacom/omarchy/pull/13542) | Finish fingerprint setup when a print is already enrolled | stevederico | 1.1 | 1.4 | 0.96 |
| [#7857](https://github.com/omacom/omarchy/pull/7857) | feat(surface-touch): add touchscreen support for Surface devices via linux-surfa | div5yesh | 1.1 | 2.7 | 0.06 |
| [#7971](https://github.com/omacom/omarchy/pull/7971) | Let the compositor and audio graph take the realtime priority they ask for | omarchybot | 1.2 | 1.3 | 0.81 |
| [#8188](https://github.com/omacom/omarchy/pull/8188) | Add and remove tailnets from the Tailscale panel | stephentaylor-com | 1.8 | 2.7 | 0.28 |
| [#10110](https://github.com/omacom/omarchy/pull/10110) | Add DaVinci Resolve and DaVinci Resolve Studio installers | sharms | 1.1 | 2.7 | 0.03 |
| [#10435](https://github.com/omacom/omarchy/pull/10435) | Add VSCodium as a default editor and installer option | epkoen | 1.1 | 2.1 | 0.03 |
| [#6912](https://github.com/omacom/omarchy/pull/6912) | Fix FIDO2 setup on keys that require user verification | Erijl | 1.5 | 1.7 | 0.96 |
| [#7554](https://github.com/omacom/omarchy/pull/7554) | Add bb to the AI install menu | melonamin | 1.8 | 2.0 | 0.03 |
| [#9227](https://github.com/omacom/omarchy/pull/9227) | Require interactive confirmation for AUR installs and updates | vikram | 1.1 | 2.0 | 0.12 |
| [#9695](https://github.com/omacom/omarchy/pull/9695) | Add a Setup > Region toggle with Chinese language and input method | ZacharyZhang-NY | 2.1 | 2.6 | 0.09 |
| [#9894](https://github.com/omacom/omarchy/pull/9894) | Fix Tailscale plugin failing to reconnect when accept-routes is enabled | llstrk | 1.0 | 2.8 | 0.92 |
| [#9909](https://github.com/omacom/omarchy/pull/9909) | Track AppImages from GitHub releases and update them daily | alfkonee | 1.0 | 2.9 | 0.06 |
| [#10473](https://github.com/omacom/omarchy/pull/10473) | network speedtest: use tokenless Cloudflare endpoints | Snowfedya | 2.8 | 1.7 | 0.96 |
| [#11470](https://github.com/omacom/omarchy/pull/11470) | Run declared plugin cleanup before removal | antongisli | 1.0 | 3.0 | 0.22 |
| [#12059](https://github.com/omacom/omarchy/pull/12059) | Run the default agent on another machine | CocaKova | 1.0 | 3.0 | 0.06 |
| [#13296](https://github.com/omacom/omarchy/pull/13296) | Install OpenClaw as a self-updating copy under ~/.openclaw | spencerbull | 1.2 | 2.9 | 0.72 |
| [#13652](https://github.com/omacom/omarchy/pull/13652) | Drop pam_faillock preauth silent so lockouts are visible | AnPod | 1.5 | 0.9 | 0.88 |
| [#8662](https://github.com/omacom/omarchy/pull/8662) | Sanitize legacy Windows VM usernames | Elshayib | 2.5 | 1.1 | 0.96 |
| [#9500](https://github.com/omacom/omarchy/pull/9500) | Give visudo an editor that Omarchy actually installs | d-zalewski | 1.5 | 1.0 | 0.95 |
| [#10974](https://github.com/omacom/omarchy/pull/10974) | Rust-first sandboxed Quickshell plugins | jacob-vincent-mink | 1.0 | 3.0 | 0.03 |
| [#11574](https://github.com/omacom/omarchy/pull/11574) | Add expandable hourly rain tables to the weather panel | AnPod | 1.1 | 2.6 | 0.03 |
| [#6807](https://github.com/omacom/omarchy/pull/6807) | Detect captive portals and offer to sign in | scottjones | 1.0 | 2.7 | 0.07 |
| [#6847](https://github.com/omacom/omarchy/pull/6847) | Preserve shared boot entries through factory reset | yashranaway | 1.2 | 3.0 | 0.87 |
| [#9571](https://github.com/omacom/omarchy/pull/9571) | Resolve the invoking user's home in removal cleanup scripts | shaynhornik | 1.2 | 2.1 | 0.97 |
| [#11839](https://github.com/omacom/omarchy/pull/11839) | feat: add commandcode, qwen audio agent, and colibri to AI installs | HIMANSHU11827 | 1.0 | 2.4 | 0.02 |
| [#12279](https://github.com/omacom/omarchy/pull/12279) | Clear the eight-second enterprise Wi-Fi auth timeout | DonnieFi | 1.1 | 1.9 | 0.92 |
| [#13106](https://github.com/omacom/omarchy/pull/13106) | Skip the Codex app-server probe when there are no credentials | surim0n | 2.4 | 1.1 | 0.78 |
| [#13811](https://github.com/omacom/omarchy/pull/13811) | fix(bluetooth): recover incomplete pairing | jsonMartin | 1.9 | 2.0 | 0.96 |
| [#6474](https://github.com/omacom/omarchy/pull/6474) | Add Android development environment | ryuhzk | 1.2 | 2.2 | 0.03 |
| [#7882](https://github.com/omacom/omarchy/pull/7882) | Add native Syncthing integration | k-bx | 1.5 | 3.0 | 0.03 |
| [#8035](https://github.com/omacom/omarchy/pull/8035) | Add VPN section to the network panel | thooams | 1.9 | 2.5 | 0.04 |
| [#9044](https://github.com/omacom/omarchy/pull/9044) | Keep SDDM auto-login off encrypted roots in the quattro upgrade | PyRo1121 | 1.7 | 1.3 | 0.96 |
| [#9461](https://github.com/omacom/omarchy/pull/9461) | [codex] OM-SEC-05: Remove the unsigned Apple T2 package source | AFOliveira | 1.0 | 3.0 | 0.45 |
| [#9594](https://github.com/omacom/omarchy/pull/9594) | Fix XDG Secret portal keyring access | pkwagner | 1.4 | 1.1 | 0.94 |
| [#5654](https://github.com/omacom/omarchy/pull/5654) | Add Install -> Editor -> Jetbrains menu | NicolasDorier | 1.4 | 2.6 | 0.18 |
| [#7258](https://github.com/omacom/omarchy/pull/7258) | Restore early Thunderbolt authorization for LUKS unlock | chriopter | 1.1 | 2.2 | 0.77 |
| [#8093](https://github.com/omacom/omarchy/pull/8093) | Call a lapsed Claude access token paused, not signed out | meibe-ab | 1.8 | 1.1 | 0.93 |
| [#9539](https://github.com/omacom/omarchy/pull/9539) | Add cursor theme selection to the Style menu | TheLinuxITGuy | 1.9 | 2.3 | 0.03 |
| [#11722](https://github.com/omacom/omarchy/pull/11722) | Add llmman to Install > AI and Remove > AI | ericcurtin | 1.1 | 1.9 | 0.04 |
| [#12245](https://github.com/omacom/omarchy/pull/12245) | Lock/sleep: fail-closed, clamshell, auth UI, lid focus, logind | Chessing234 | 0.9 | 2.7 | 0.66 |
| [#12796](https://github.com/omacom/omarchy/pull/12796) | Fix omarchy update under sudo: unset OMARCHY_PATH and yay-as-root | mrpink77it | 1.1 | 2.0 | 0.96 |
| [#12925](https://github.com/omacom/omarchy/pull/12925) | Add a reveal toggle to masked TextFields, wired up for the Wi-Fi passphrase | jankeesvw | 2.1 | 1.8 | 0.07 |
| [#13312](https://github.com/omacom/omarchy/pull/13312) | Require a per-session token for notification click-exec | Chessing234 | 1.9 | 2.3 | 0.85 |
| [#13796](https://github.com/omacom/omarchy/pull/13796) | Keep an early polkit Enter and submit it when PAM asks | cristim | 1.2 | 1.2 | 0.96 |
| [#9878](https://github.com/omacom/omarchy/pull/9878) | Re-apply hardware pacman repos after a refresh restore | hudsonwa | 1.1 | 1.0 | 0.97 |
| [#11381](https://github.com/omacom/omarchy/pull/11381) | Install the pre-T2 FaceTime HD camera driver and firmware | rand0mdud3 | 2.8 | 2.2 | 0.73 |
| [#12111](https://github.com/omacom/omarchy/pull/12111) | Harden notification image copies, exec tokens, and hint reads | Chessing234 | 1.3 | 2.1 | 0.57 |
| [#13047](https://github.com/omacom/omarchy/pull/13047) | Pin factory-reset elevation to the packaged command | AFOliveira | 1.9 | 1.0 | 0.92 |
| [#13101](https://github.com/omacom/omarchy/pull/13101) | Actually restart bluetooth.service in omarchy-restart-bluetooth | surim0n | 1.8 | 1.0 | 0.96 |
| [#6557](https://github.com/omacom/omarchy/pull/6557) | feature(editor) add Doom Emacs installer, uninstaller, and theming integration | Irfrit | 1.0 | 2.9 | 0.02 |
| [#7831](https://github.com/omacom/omarchy/pull/7831) | Reload a wedged Wi-Fi radio without waiting for the user | acrogenesis | 1.1 | 2.6 | 0.84 |
| [#8001](https://github.com/omacom/omarchy/pull/8001) | Fix GitHub credential helpers after mise gh upgrades | thecdrz | 2.0 | 1.4 | 0.96 |
| [#11144](https://github.com/omacom/omarchy/pull/11144) | Add Axon as a default coding agent | codywakeford | 2.4 | 2.2 | 0.04 |
| [#12070](https://github.com/omacom/omarchy/pull/12070) | Answer ARP only from the interface that owns the address | michaeldeby | 2.2 | 0.9 | 0.90 |
| [#13085](https://github.com/omacom/omarchy/pull/13085) | Restart bluetoothd and reload btusb when the adapter is wedged | pedrohfp | 1.2 | 1.1 | 0.96 |
| [#13734](https://github.com/omacom/omarchy/pull/13734) | Add a sign-in button to the agents panel's auth card | branewyn | 1.1 | 2.0 | 0.13 |
| [#13742](https://github.com/omacom/omarchy/pull/13742) | Test passwordless sudo revoke hook packaging | haiderakt | 2.6 | 0.9 | 0.64 |
| [#6965](https://github.com/omacom/omarchy/pull/6965) | Add git-based backup and restore | andresreibel | 1.1 | 3.0 | 0.03 |
| [#9729](https://github.com/omacom/omarchy/pull/9729) | Add Setup Wizard for NVIDIA DisplayPort 1.4 EDID Fix | JaxonWright | 1.1 | 2.9 | 0.27 |
| [#10610](https://github.com/omacom/omarchy/pull/10610) | Add Muse usage collector to the agents panel | andresantonioriveros | 1.2 | 3.0 | 0.03 |
| [#13088](https://github.com/omacom/omarchy/pull/13088) | Fix network panel Forget centering, add Cancel for in-flight connects | thedavidweng | 2.4 | 2.0 | 0.87 |
| [#13699](https://github.com/omacom/omarchy/pull/13699) | Keep other systems' boot entries through a factory reset | xdanger | 1.1 | 2.3 | 0.95 |
| [#13763](https://github.com/omacom/omarchy/pull/13763) | Add Cloudmail to Install > Service | ferdousbhai | 1.4 | 2.2 | 0.03 |
| [#12475](https://github.com/omacom/omarchy/pull/12475) | network: keep passphrase prompt focused through scan reorders | FernandoCassioDev | 1.5 | 1.1 | 0.97 |
| [#12957](https://github.com/omacom/omarchy/pull/12957) | Keep the update transcript out of world-writable /tmp | taufderl | 2.1 | 1.3 | 0.93 |
| [#6697](https://github.com/omacom/omarchy/pull/6697) | Adding Atuin be default for better shell search / history | mrpbennett | 1.0 | 1.9 | 0.04 |
| [#7485](https://github.com/omacom/omarchy/pull/7485) | Add Firebase CLI development environment via mise | calledtoconstruct | 1.9 | 1.4 | 0.04 |
| [#7731](https://github.com/omacom/omarchy/pull/7731) | Show Windows PCs and admin shares in Files | gmcclelland90 | 1.2 | 2.0 | 0.20 |
| [#8801](https://github.com/omacom/omarchy/pull/8801) | Add Helium and Ungoogled Chromium browser support | YamilG | 1.8 | 2.9 | 0.05 |
| [#8908](https://github.com/omacom/omarchy/pull/8908) | Switch DNS providers without DHCP churn or profile rewrites | danbosscher | 1.9 | 3.0 | 0.45 |
| [#9777](https://github.com/omacom/omarchy/pull/9777) | Add DeepSeek Harness to the agent roster and Install > AI | falser101 | 1.4 | 2.1 | 0.04 |
| [#10262](https://github.com/omacom/omarchy/pull/10262) | Snapshot BASHPID before /proc fd walks in windows-vm mounts | fresh3nough | 2.2 | 1.8 | 0.97 |
| [#11017](https://github.com/omacom/omarchy/pull/11017) | Install missing BCM43602 board NVRAM on MacBookPro13,3 | justin-schroeder | 2.4 | 2.2 | 0.71 |
| [#11874](https://github.com/omacom/omarchy/pull/11874) | Require approval for new USB and Thunderbolt devices by default | acrogenesis | 1.0 | 3.0 | 0.12 |
| [#9024](https://github.com/omacom/omarchy/pull/9024) | Auto-create /etc/1password/custom_allowed_browsers on install | spuder | 1.1 | 1.0 | 0.46 |
| [#13664](https://github.com/omacom/omarchy/pull/13664) | Give each webapp its own Chromium profile | AnPod | 1.4 | 1.5 | 0.80 |
| [#6844](https://github.com/omacom/omarchy/pull/6844) | Add Amp as a default coding agent | daveashworth | 2.6 | 2.6 | 0.06 |
| [#10109](https://github.com/omacom/omarchy/pull/10109) | Add a disposable Omarchy lab VM | acrogenesis | 1.0 | 3.0 | 0.03 |
| [#13362](https://github.com/omacom/omarchy/pull/13362) | Converge omarchy-mac and omarchy-mx-mac into upstream Omarchy | maralcbr | 1.5 | 3.0 | 0.15 |
| [#6513](https://github.com/omacom/omarchy/pull/6513) | Enable DNS-over-TLS for custom DNS providers | KazeTachinuu | 2.3 | 1.3 | 0.87 |
| [#7071](https://github.com/omacom/omarchy/pull/7071) | Migrate Brave Origin Beta profile data to stable | jakiurcore | 2.4 | 1.4 | 0.85 |
| [#7799](https://github.com/omacom/omarchy/pull/7799) | Show banked rate limit resets on the Codex tab | btsouth | 1.5 | 1.9 | 0.21 |
| [#8930](https://github.com/omacom/omarchy/pull/8930) | Harden lock lifecycle, recovery, and keyboard wake | AFOliveira | 1.8 | 3.0 | 0.69 |
| [#10393](https://github.com/omacom/omarchy/pull/10393) | Cap lock fingerprint retries; skip closed-lid fingerprint; silence sudo/polkit P | calledtoconstruct | 1.0 | 2.5 | 0.82 |
| [#11242](https://github.com/omacom/omarchy/pull/11242) | Install the marketplace-verified snapshot by default in plugin add | StavWasPlayZ | 1.1 | 2.3 | 0.34 |
| [#12287](https://github.com/omacom/omarchy/pull/12287) | Add the theme marketplace: browse, install and update community themes | tahayvr | 1.1 | 3.0 | 0.02 |
| [#12766](https://github.com/omacom/omarchy/pull/12766) | Add Bluetooth file receiving to the Bluetooth panel | krsna1729 | 1.1 | 2.4 | 0.04 |
| [#12897](https://github.com/omacom/omarchy/pull/12897) | Accept device-initiated Bluetooth Just Works pairing | Chessing234 | 1.6 | 2.5 | 0.76 |
| [#13200](https://github.com/omacom/omarchy/pull/13200) | Sign in to captive portals in a dropdown instead of the browser | JGh0stSecOps | 1.2 | 2.6 | 0.14 |
| [#13836](https://github.com/omacom/omarchy/pull/13836) | Link Pi agent skills into PI_CODING_AGENT_DIR | Chessing234 | 1.4 | 2.0 | 0.24 |
| [#6664](https://github.com/omacom/omarchy/pull/6664) | Fix fingerprint setup script to detect non-libfprint-git providers | abbaty48 | 1.1 | 1.1 | 0.97 |
| [#7622](https://github.com/omacom/omarchy/pull/7622) | Add an omarchy:// link handler for installing plugins from a web page | hegjon | 1.0 | 2.2 | 0.03 |
| [#7680](https://github.com/omacom/omarchy/pull/7680) | Add a reveal toggle to the lock screen password field | thooams | 1.1 | 1.8 | 0.09 |
| [#8952](https://github.com/omacom/omarchy/pull/8952) | Replace Gemini coding agent with Antigravity (backport of #6900) | KOUSTAV2409 | 1.9 | 2.3 | 0.62 |
| [#12160](https://github.com/omacom/omarchy/pull/12160) | Disable core dump generation to prevent memory exposure | kairosci | 1.0 | 1.6 | 0.36 |
| [#12167](https://github.com/omacom/omarchy/pull/12167) | Add audit rules for sensitive files and privilege changes | kairosci | 1.0 | 1.7 | 0.05 |
| [#7995](https://github.com/omacom/omarchy/pull/7995) | Stage diagnostics logs privately instead of at fixed /tmp paths | Adolanium | 1.0 | 2.0 | 0.74 |
| [#13829](https://github.com/omacom/omarchy/pull/13829) | Resync Wi-Fi rows when a listed network's saved profile attaches | mcurtis | 1.3 | 1.6 | 0.95 |
| [#6515](https://github.com/omacom/omarchy/pull/6515) | Support hardware, fingerprint, and password Polkit flows | mattrayner | 1.0 | 2.9 | 0.20 |
| [#10346](https://github.com/omacom/omarchy/pull/10346) | Pin Electron password store to gnome-libsecret | cempack | 1.7 | 1.7 | 0.32 |
| [#10428](https://github.com/omacom/omarchy/pull/10428) | Distinguish sudo failure from missing Snapper configs | fresh3nough | 2.9 | 1.0 | 0.97 |
| [#11216](https://github.com/omacom/omarchy/pull/11216) | Integrate NetClaw into Omarchy with Light and Full setup | automateyournetwork | 1.2 | 3.0 | 0.03 |
| [#11289](https://github.com/omacom/omarchy/pull/11289) | Add the headless server edition | bartex | 1.0 | 3.0 | 0.02 |
| [#11983](https://github.com/omacom/omarchy/pull/11983) | Show which processes asked for a polkit password | cristim | 1.1 | 2.6 | 0.23 |
| [#13187](https://github.com/omacom/omarchy/pull/13187) | Setup fingerprint for Validity/Synaptics readers via python-validity | prashanth-7861 | 1.1 | 2.8 | 0.56 |
| [#5562](https://github.com/omacom/omarchy/pull/5562) | fix(network): add default iwd config to prevent micro drops | nim-p99 | 1.5 | 1.5 | 0.73 |
| [#6719](https://github.com/omacom/omarchy/pull/6719) | when installing Bitwarden, ask user if it should be used as SSH agent | sgruendel | 0.7 | 1.2 | 0.09 |
| [#13110](https://github.com/omacom/omarchy/pull/13110) | Ship a managed Chromium privacy policy alongside the theme color | surim0n | 1.4 | 2.2 | 0.21 |
| [#13183](https://github.com/omacom/omarchy/pull/13183) | Add password visibility toggle to lock screen | cristim | 1.2 | 1.3 | 0.08 |
| [#13283](https://github.com/omacom/omarchy/pull/13283) | Tell the user when pam_faillock has locked the account | Chessing234 | 1.7 | 1.1 | 0.79 |
| [#9320](https://github.com/omacom/omarchy/pull/9320) | Add Oma, voice control for the desktop, as an optional service | wombatoperator | 1.2 | 1.9 | 0.02 |
| [#10257](https://github.com/omacom/omarchy/pull/10257) | Redact network identifiers from debug output | wbnns | 1.1 | 2.3 | 0.86 |
| [#11984](https://github.com/omacom/omarchy/pull/11984) | Explain polkit commands with the default coding agent on request | cristim | 1.0 | 2.3 | 0.07 |
| [#13690](https://github.com/omacom/omarchy/pull/13690) | Add region profiles, starting with China's package repositories | xdanger | 1.0 | 3.0 | 0.03 |
| [#8537](https://github.com/omacom/omarchy/pull/8537) | Add Alfred/Raycast-style live query plugins to the menu | avillagran | 1.3 | 3.0 | 0.02 |
| [#13098](https://github.com/omacom/omarchy/pull/13098) | Default dictation to verified Cohere Vulkan, paste and Atreyu visuals | ryanrhughes | 1.0 | 3.0 | 0.07 |
| [#13612](https://github.com/omacom/omarchy/pull/13612) | Configure fingerprint PAM when prints are already enrolled | AnPod | 1.1 | 1.9 | 0.90 |
| [#13625](https://github.com/omacom/omarchy/pull/13625) | Do not block SDDM autologin on pam_gnome_keyring | AnPod | 1.1 | 1.1 | 0.93 |
| [#5139](https://github.com/omacom/omarchy/pull/5139) | Add Orca screen reader with Piper TTS | fedesapuppo | 1.0 | 2.0 | 0.03 |
| [#8639](https://github.com/omacom/omarchy/pull/8639) | Allow forgetting the connected Wi-Fi network | Githubguy132010 | 2.2 | 1.0 | 0.82 |
| [#12105](https://github.com/omacom/omarchy/pull/12105) | Intelligently fallback to available agent when default agent has exhausted usage | davidsilvasmith | 1.5 | 2.1 | 0.49 |
| [#12260](https://github.com/omacom/omarchy/pull/12260) | Give third-party plugins their own entry settings and auth service | Chessing234 | 1.6 | 2.1 | 0.64 |
| [#12605](https://github.com/omacom/omarchy/pull/12605) | Add Devin collector to the agents panel | betizzel | 1.1 | 2.9 | 0.03 |
| [#13848](https://github.com/omacom/omarchy/pull/13848) | [4.0.4/4.0.5] Replace deprecated Gemini CLI with Google Antigravity (#6900) | Merxxotas | 2.0 | 2.8 | 0.53 |
| [#7566](https://github.com/omacom/omarchy/pull/7566) | Add Z.ai GLM Coding Plan agent usage collector | FelipeMayerDev | 1.9 | 2.0 | 0.03 |
| [#7871](https://github.com/omacom/omarchy/pull/7871) | Stop the lid gate logging a PAM failure on every open-lid sudo | vstoyanov | 1.1 | 1.7 | 0.92 |
| [#8204](https://github.com/omacom/omarchy/pull/8204) | Stop probing the internal T2 network interface | robzolkos | 2.5 | 1.8 | 0.83 |
| [#9009](https://github.com/omacom/omarchy/pull/9009) | Document re-enabling BitLocker after dual-boot installation | TNL402 | 1.1 | 1.3 | 0.53 |
| [#9531](https://github.com/omacom/omarchy/pull/9531) | Wait for the Windows VM RDP service before connecting | qybaihe | 2.2 | 1.6 | 0.94 |
| [#12329](https://github.com/omacom/omarchy/pull/12329) | Add Remove menu for coding agents | gitpushmainforce | 1.4 | 2.1 | 0.06 |
| [#12459](https://github.com/omacom/omarchy/pull/12459) | Add an optional installer for the asciipaper live wallpaper | cYoren | 1.3 | 2.6 | 0.02 |
| [#12896](https://github.com/omacom/omarchy/pull/12896) | Persist XKBLAYOUT for LUKS so non-US layouts stay typeable | Chessing234 | 1.7 | 2.1 | 0.87 |
| [#13630](https://github.com/omacom/omarchy/pull/13630) | Prefer IPP Everywhere when adding network printers | AnPod | 1.3 | 1.9 | 0.27 |
| [#8910](https://github.com/omacom/omarchy/pull/8910) | Avoid redundant lock after encrypted hibernate | ClGratton | 1.1 | 2.4 | 0.89 |
| [#10185](https://github.com/omacom/omarchy/pull/10185) | Add speech-dispatcher so Brave Web Speech has voices | fernandofreamunde | 1.5 | 2.2 | 0.64 |
| [#11067](https://github.com/omacom/omarchy/pull/11067) | Add Qwen Code as a default coding agent | cdenike | 1.8 | 2.0 | 0.03 |
| [#11956](https://github.com/omacom/omarchy/pull/11956) | Upgrade existing Sunshine installations to the security release | ErikMelton | 1.8 | 1.9 | 0.67 |
| [#8413](https://github.com/omacom/omarchy/pull/8413) | Add Scanner support | axelfontaine | 2.2 | 2.5 | 0.04 |
| [#11858](https://github.com/omacom/omarchy/pull/11858) | Clear and swallow the lock-screen wake key so it is not typed as a password char | h14h | 2.6 | 1.1 | 0.95 |
| [#12196](https://github.com/omacom/omarchy/pull/12196) | Stop speed test workers outliving a killed parent | Marjinoz | 2.7 | 1.5 | 0.98 |
| [#13745](https://github.com/omacom/omarchy/pull/13745) | Open the captive portal sign-in page on detection when asked to | phedoreanu | 2.2 | 1.9 | 0.11 |
| [#6532](https://github.com/omacom/omarchy/pull/6532) | Abort pkg-install when the package transaction fails or is interrupted | merdiofriviaisherebitch | 2.5 | 1.4 | 0.97 |
| [#8377](https://github.com/omacom/omarchy/pull/8377) | Browse and install any mise tool from the menu | nimixh | 2.2 | 2.0 | 0.05 |
| [#9557](https://github.com/omacom/omarchy/pull/9557) | Allow plugins to specify package dependencies (optional + required) | jamesmcm | 1.0 | 2.6 | 0.04 |
| [#10080](https://github.com/omacom/omarchy/pull/10080) | Agents panel: every signed-in Claude account, and an opt-in Columns layout | joelzamboni | 1.3 | 2.7 | 0.03 |
| [#10248](https://github.com/omacom/omarchy/pull/10248) | Add Update Plugin to Setup > Plugins menu | buffpesos | 1.1 | 2.0 | 0.05 |
| [#11768](https://github.com/omacom/omarchy/pull/11768) | Keep the Windows VM boundary probe off the host's mounts | therahul-yo | 1.1 | 2.2 | 0.93 |
| [#12114](https://github.com/omacom/omarchy/pull/12114) | Bar status: Steam idle-inhibit, Wi-Fi/SSID, Bluetooth alias/pairable | Chessing234 | 1.0 | 2.1 | 0.66 |
| [#12161](https://github.com/omacom/omarchy/pull/12161) | Blacklist uncommon network protocols and legacy filesystem modules | kairosci | 1.0 | 1.7 | 0.14 |
| [#12394](https://github.com/omacom/omarchy/pull/12394) | hw: cover all Framework 16 input-module product IDs in qmk_hid udev rule | CRTFD-DVLPR | 1.1 | 0.9 | 0.84 |
| [#7598](https://github.com/omacom/omarchy/pull/7598) | Fix orphaned network speed test workers | MBemera | 2.8 | 2.1 | 0.96 |
| [#10683](https://github.com/omacom/omarchy/pull/10683) | Add a DeepSeek usage collector for the agents panel | aholbreich | 1.1 | 1.9 | 0.09 |
| [#5177](https://github.com/omacom/omarchy/pull/5177) | Add NPU support to voxtype install and migration | jacob-vincent-mink | 1.0 | 3.0 | 0.05 |
| [#5279](https://github.com/omacom/omarchy/pull/5279) | Add per-network DNS configuration for WiFi | roib | 1.1 | 2.0 | 0.04 |
| [#9398](https://github.com/omacom/omarchy/pull/9398) | Discover LUKS drives via lsblk, not blkid | fresh3nough | 2.8 | 1.0 | 0.97 |
| [#10952](https://github.com/omacom/omarchy/pull/10952) | Start Omarchy Server edition predicates and menu | dl-alexandre | 2.1 | 2.9 | 0.05 |
| [#11398](https://github.com/omacom/omarchy/pull/11398) | feat(install): accept owner/repo shorthand in plugin add and theme install | rpaweb | 1.1 | 1.8 | 0.05 |
| [#13107](https://github.com/omacom/omarchy/pull/13107) | Fall back to Cloudflare endpoints when api.fast.com is unreachable | surim0n | 1.9 | 2.0 | 0.78 |
| [#13563](https://github.com/omacom/omarchy/pull/13563) | Add animated installer presentation with embedded interactive controls | tcballard | 1.6 | 3.0 | 0.04 |
| [#7062](https://github.com/omacom/omarchy/pull/7062) | Support DoT endpoints in `omarchy dns Custom` | ujo4eva | 1.1 | 1.9 | 0.12 |
| [#8578](https://github.com/omacom/omarchy/pull/8578) | Update installed themes in parallel | zackerydev | 2.4 | 1.9 | 0.16 |
| [#9381](https://github.com/omacom/omarchy/pull/9381) | Show what PAM asked for in the polkit dialog | julianduque | 1.2 | 1.3 | 0.92 |
| [#10944](https://github.com/omacom/omarchy/pull/10944) | Keep lock password field focused | ArveLomsland | 1.4 | 1.9 | 0.79 |
| [#11388](https://github.com/omacom/omarchy/pull/11388) | Sync the pacman databases before the first package install | mkenigs | 1.3 | 1.9 | 0.94 |
| [#11731](https://github.com/omacom/omarchy/pull/11731) | Add iPhone cable support via usbmuxd and gvfs-afc | basalto | 2.1 | 1.7 | 0.05 |
| [#8715](https://github.com/omacom/omarchy/pull/8715) | Add agent diagnostics, MCP inspection, and safe launch mode | jmohouse6 | 1.9 | 2.9 | 0.06 |
| [#11795](https://github.com/omacom/omarchy/pull/11795) | Show the command being authorized at the top of the polkit prompt | cristim | 1.1 | 1.9 | 0.72 |
| [#5136](https://github.com/omacom/omarchy/pull/5136) | Add auto power profile switching for T2 MacBooks | fedesapuppo | 1.2 | 2.4 | 0.06 |
| [#7890](https://github.com/omacom/omarchy/pull/7890) | Reject Voxtype on CPUs without AVX2 | kx0101 | 2.0 | 1.6 | 0.94 |
| [#9288](https://github.com/omacom/omarchy/pull/9288) | Set kernel.kptr_restrict=1 in the shipped sysctl drop-in | fresh3nough | 2.5 | 1.1 | 0.58 |
| [#10088](https://github.com/omacom/omarchy/pull/10088) | Add omarchy-install-blesh for opt-in ble.sh autocompletion | hen8y | 2.5 | 1.7 | 0.03 |
| [#10288](https://github.com/omacom/omarchy/pull/10288) | feat(network): add wired NIC DHCP/static IPv4 settings to the panel | hehh2001 | 1.1 | 2.4 | 0.03 |
| [#10730](https://github.com/omacom/omarchy/pull/10730) | Add Command Code as a coding agent choice | ahmadawais | 1.6 | 2.0 | 0.03 |
| [#11198](https://github.com/omacom/omarchy/pull/11198) | Make the adapter pairable while pairing a Bluetooth device | megamos | 1.1 | 1.4 | 0.95 |
| [#13481](https://github.com/omacom/omarchy/pull/13481) | Add opt-in default-browser links for web apps | JSRRosenbaum | 1.9 | 2.9 | 0.11 |
| [#5818](https://github.com/omacom/omarchy/pull/5818) | Add Affinity Suite installer with DPI scaling for Hyprland | Cliffback | 1.1 | 1.9 | 0.12 |
| [#7158](https://github.com/omacom/omarchy/pull/7158) | Keep the lock screen fingerprint working across suspend, and show when the reade | GeertJohan | 1.1 | 2.5 | 0.95 |
| [#8315](https://github.com/omacom/omarchy/pull/8315) | Network panel: show External IP in connection details | nixfred | 2.0 | 1.2 | 0.04 |
| [#9596](https://github.com/omacom/omarchy/pull/9596) | feat(mise): install default CLI tools through native lazy shims | jdx | 1.1 | 2.8 | 0.05 |
| [#10058](https://github.com/omacom/omarchy/pull/10058) | Add an Ethernet toggle to the network panel | e2jk | 1.3 | 2.0 | 0.05 |
| [#10530](https://github.com/omacom/omarchy/pull/10530) | Map keypad digits in the polkit dialog when Qt ignores NumLock | MADS0LADEN | 1.8 | 1.1 | 0.95 |
| [#10756](https://github.com/omacom/omarchy/pull/10756) | Add Ubuntu Cloud Agent environment for CLI and shell tests | ryanrhughes | 2.6 | 1.9 | 0.21 |
| [#10802](https://github.com/omacom/omarchy/pull/10802) | Keep web app and browser launches on http(s) | Chessing234 | 1.3 | 2.1 | 0.85 |
| [#12109](https://github.com/omacom/omarchy/pull/12109) | Keep update/runtime/diagnostics out of world-writable /tmp | Chessing234 | 1.9 | 2.1 | 0.83 |
| [#7609](https://github.com/omacom/omarchy/pull/7609) | Suppress keyring "reinstalling" warning in any locale | fldc | 2.2 | 0.7 | 0.94 |
| [#8051](https://github.com/omacom/omarchy/pull/8051) | Add Junie as a selectable default coding agent | reinierbutot | 1.0 | 2.0 | 0.03 |
| [#8704](https://github.com/omacom/omarchy/pull/8704) | Enable docker.service for Docker DBs | Elshayib | 2.3 | 1.9 | 0.92 |
| [#8796](https://github.com/omacom/omarchy/pull/8796) | windows-vm: negotiate RDP with /sec:tls by default | joeldeteves | 2.0 | 1.1 | 0.72 |
| [#10347](https://github.com/omacom/omarchy/pull/10347) | Add optional Ponte Android remote service commands | LucasOl1337 | 2.0 | 2.7 | 0.03 |
| [#10594](https://github.com/omacom/omarchy/pull/10594) | Add optional Agent Desktops app for background agent work | not-compromised | 1.1 | 2.9 | 0.02 |
| [#11129](https://github.com/omacom/omarchy/pull/11129) | Add Kilo AI | WebReflection | 1.0 | 2.0 | 0.03 |
| [#11286](https://github.com/omacom/omarchy/pull/11286) | Configure persistent Wi-Fi Direct PC identity | alchemy | 2.1 | 1.0 | 0.26 |

## Review candidates: desktop-config — 255 PRs

| PR | Title | Author | Model finished | Model effort | Model fix |
|---|---|---|---|---|---|
| [#5881](https://github.com/omacom/omarchy/pull/5881) | Account for keyboard layout variant for keybinding helper | blegat | 2.3 | 1.6 | 0.89 |
| [#6467](https://github.com/omacom/omarchy/pull/6467) | fix(panel-slider): color-match muted knob to dimmed fill line | itscallssh | 2.4 | 1.4 | 0.90 |
| [#6642](https://github.com/omacom/omarchy/pull/6642) | Keep the lock blank from turning the display off (DPMS link-drop crash) | akashgagda | 2.3 | 1.5 | 0.79 |
| [#6693](https://github.com/omacom/omarchy/pull/6693) | Preserve borders on Google Meet browser windows | timohubois | 2.4 | 1.1 | 0.94 |
| [#6834](https://github.com/omacom/omarchy/pull/6834) | Ignore T2 headset remotes when switching layouts | yashranaway | 1.9 | 1.0 | 0.97 |
| [#6871](https://github.com/omacom/omarchy/pull/6871) | Keep the menu populated across git swaps of its definition file | dhh | 2.6 | 1.1 | 0.95 |
| [#6896](https://github.com/omacom/omarchy/pull/6896) | Apply the system keyboard layout to the SDDM greeter | g-desoutter | 2.6 | 1.6 | 0.94 |
| [#6904](https://github.com/omacom/omarchy/pull/6904) | Dismiss an open shell panel with Super+W | csfh | 2.4 | 1.9 | 0.87 |
| [#6918](https://github.com/omacom/omarchy/pull/6918) | Keep Wi-Fi indicator online when AP object is missing | patrickrodrigues-aa | 2.2 | 1.6 | 0.95 |
| [#6958](https://github.com/omacom/omarchy/pull/6958) | Preserve terminal font size when changing font family | sbalbalosa | 2.4 | 1.4 | 0.96 |
| [#7011](https://github.com/omacom/omarchy/pull/7011) | Keep bar clicks out of login shells | SL0wZEr | 2.7 | 1.8 | 0.66 |
| [#7020](https://github.com/omacom/omarchy/pull/7020) | Float Java AWT XWayland popups instead of tiling them | v-t-r-gg | 2.0 | 1.0 | 0.86 |
| [#7023](https://github.com/omacom/omarchy/pull/7023) | Fix inverted on/off semantics in omarchy-toggle-bar | Amvurguezo | 2.3 | 1.2 | 0.98 |
| [#7029](https://github.com/omacom/omarchy/pull/7029) | Show the new track on the media OSD instead of the player name | Orkunnnn | 2.0 | 1.8 | 0.93 |
| [#7036](https://github.com/omacom/omarchy/pull/7036) | Fix enabling and disabling a display doing nothing | sterre-g | 2.6 | 1.0 | 0.97 |
| [#7088](https://github.com/omacom/omarchy/pull/7088) | Fix polkit password dots rendering as tiny specks | ax1g | 2.8 | 0.3 | 0.95 |
| [#7146](https://github.com/omacom/omarchy/pull/7146) | Disable the panel by overlay alone in clamshell recovery | mkelk | 2.0 | 2.6 | 0.92 |
| [#7173](https://github.com/omacom/omarchy/pull/7173) | Localize clock bar weekday/month names | dr-moreira | 2.9 | 1.0 | 0.90 |
| [#7240](https://github.com/omacom/omarchy/pull/7240) | Fix invisible VS Code list hover state | yacobmole | 2.7 | 0.6 | 0.94 |
| [#7241](https://github.com/omacom/omarchy/pull/7241) | Inset BorderSurface strokes a device pixel to survive clip edges | gsamokovarov | 2.1 | 1.0 | 0.93 |
| [#7245](https://github.com/omacom/omarchy/pull/7245) | fix(shell): position bar widget panels relative to anchor widget | ax1g | 2.0 | 1.5 | 0.97 |
| [#7269](https://github.com/omacom/omarchy/pull/7269) | Run the shell on the Vulkan backend on primary NVIDIA GPUs | PavelAlennikov | 2.3 | 1.7 | 0.90 |
| [#7273](https://github.com/omacom/omarchy/pull/7273) | Match the volume OSD icon to the output switcher | xymbol | 2.8 | 1.9 | 0.73 |
| [#7283](https://github.com/omacom/omarchy/pull/7283) | Use layout-independent universal clipboard shortcuts | janhesters | 2.4 | 1.7 | 0.93 |
| [#7296](https://github.com/omacom/omarchy/pull/7296) | feat: wrap the overflowing text in the menu | Sameer292 | 2.3 | 1.0 | 0.88 |
| [#7404](https://github.com/omacom/omarchy/pull/7404) | Accept theme-set display names in theme remove | 686f6c61 | 2.6 | 1.0 | 0.96 |
| [#7413](https://github.com/omacom/omarchy/pull/7413) | Keep background refreshes from scrolling an open select menu | melonamin | 2.4 | 1.7 | 0.96 |
| [#7419](https://github.com/omacom/omarchy/pull/7419) | Let Chromium size and position PiP windows (Fixes #7391) | shrijit37 | 2.6 | 1.1 | 0.96 |
| [#7451](https://github.com/omacom/omarchy/pull/7451) | menu: scale wheel events 3x for faster touchpad scrolling on long lists | tahadx | 2.0 | 1.1 | 0.71 |
| [#7465](https://github.com/omacom/omarchy/pull/7465) | Fix Obsidian focus pattern for its current app id | johnnynia | 2.6 | 0.5 | 0.97 |
| [#7471](https://github.com/omacom/omarchy/pull/7471) | Wake the blanked lock screen from the keyboard | notTanveer | 2.2 | 1.0 | 0.95 |
| [#7488](https://github.com/omacom/omarchy/pull/7488) | Detect Apple Silicon trackpads in omarchy-hw-touchpad | Skeptomenos | 2.4 | 0.6 | 0.92 |
| [#7495](https://github.com/omacom/omarchy/pull/7495) | Keep the monitor layout when changing scale | Piemme99 | 2.8 | 1.2 | 0.97 |
| [#7497](https://github.com/omacom/omarchy/pull/7497) | Stop monitor scaling from persisting a scale the reload will undo | davydotcom | 2.4 | 1.6 | 0.96 |
| [#7536](https://github.com/omacom/omarchy/pull/7536) | Treat Ctrl+[ as panel escape | NorthernReach | 2.4 | 1.2 | 0.82 |
| [#7560](https://github.com/omacom/omarchy/pull/7560) | Fix weather panel hero overlapping location at triple-digit temps | guilhermetk | 2.6 | 1.0 | 0.97 |
| [#7563](https://github.com/omacom/omarchy/pull/7563) | Clear a stuck bar-move ghost when the gesture is interrupted | calledtoconstruct | 2.4 | 1.2 | 0.97 |
| [#7592](https://github.com/omacom/omarchy/pull/7592) | Refocus the lock password field after resume | RovshanMuradov | 2.6 | 1.0 | 0.97 |
| [#7653](https://github.com/omacom/omarchy/pull/7653) | Keep menu empty-state text inside the card | benwillems | 2.5 | 1.6 | 0.94 |
| [#7713](https://github.com/omacom/omarchy/pull/7713) | Include dual-width fonts in font picker | OldJobobo | 2.7 | 1.3 | 0.87 |
| [#7716](https://github.com/omacom/omarchy/pull/7716) | Gate calculator keybindings with preinstalls | OldJobobo | 1.9 | 1.0 | 0.94 |
| [#7717](https://github.com/omacom/omarchy/pull/7717) | Widen the column for full width on scrolling workspaces | donperi | 2.6 | 1.1 | 0.91 |
| [#7723](https://github.com/omacom/omarchy/pull/7723) | Keep last good shell config when user shell.json fails to parse | felixzsh | 2.3 | 1.4 | 0.82 |
| [#7736](https://github.com/omacom/omarchy/pull/7736) | Match LocalSend's current Wayland app ID | OldJobobo | 2.9 | 1.1 | 0.96 |
| [#7738](https://github.com/omacom/omarchy/pull/7738) | Notifications: clicking a toast focuses the exact sending window when focus_on_a | nixfred | 2.1 | 1.0 | 0.94 |
| [#7756](https://github.com/omacom/omarchy/pull/7756) | Stop building a theme signature nothing reads | Adolanium | 2.9 | 1.1 | 0.63 |
| [#7794](https://github.com/omacom/omarchy/pull/7794) | Step running foot windows to the new text size | scottjones | 2.1 | 1.9 | 0.74 |
| [#7806](https://github.com/omacom/omarchy/pull/7806) | Drop key auto-repeat in the lock screen password field | berndb | 2.8 | 1.3 | 0.96 |
| [#7905](https://github.com/omacom/omarchy/pull/7905) | Dictation indicator toggles dictation on left click | tahadx | 2.0 | 1.2 | 0.92 |
| [#7910](https://github.com/omacom/omarchy/pull/7910) | window-pop: don't tile an already-floating window | tahadx | 1.8 | 1.1 | 0.97 |
| [#7954](https://github.com/omacom/omarchy/pull/7954) | Remember menu selection when navigating back | mauhaa | 2.4 | 1.8 | 0.66 |
| [#8048](https://github.com/omacom/omarchy/pull/8048) | Dismiss screensaver on pointer motion | kazeshini178 | 1.9 | 2.1 | 0.89 |
| [#8059](https://github.com/omacom/omarchy/pull/8059) | Keep Hyprland helpers global | catlee | 2.0 | 1.0 | 0.94 |
| [#8069](https://github.com/omacom/omarchy/pull/8069) | Add fallback logic to resolve current user in SDDM greeter | ErikMelton | 2.4 | 1.6 | 0.95 |
| [#8086](https://github.com/omacom/omarchy/pull/8086) | Re-arm idle monitor when timeouts change in shell.json (#8038) | askadityapandey | 2.0 | 1.8 | 0.96 |
| [#8258](https://github.com/omacom/omarchy/pull/8258) | Fix Brave Origin refresh collision | llirik0 | 2.5 | 1.2 | 0.97 |
| [#8259](https://github.com/omacom/omarchy/pull/8259) | Keep notification contents out of process arguments | llirik0 | 2.3 | 2.8 | 0.73 |
| [#8307](https://github.com/omacom/omarchy/pull/8307) | Stop re-sampling the wallpaper for the transparent bar on unrelated state writes | ryanyogan | 2.2 | 1.5 | 0.95 |
| [#8341](https://github.com/omacom/omarchy/pull/8341) | Fix Bitwarden extension popout rendering | TyRichards | 2.1 | 1.8 | 0.96 |
| [#8350](https://github.com/omacom/omarchy/pull/8350) | Paste clipboard history with Ctrl+V outside terminals | fregys | 2.3 | 1.7 | 0.90 |
| [#8393](https://github.com/omacom/omarchy/pull/8393) | Say when an installed theme's files are refused | scottjones | 2.4 | 1.5 | 0.66 |
| [#8411](https://github.com/omacom/omarchy/pull/8411) | Fix out-of-range group window shortcuts | wxasacoder | 2.6 | 1.2 | 0.97 |
| [#8437](https://github.com/omacom/omarchy/pull/8437) | Hide Obsidian's window buttons in the Omarchy theme | ecomodeller | 2.3 | 1.0 | 0.61 |
| [#8560](https://github.com/omacom/omarchy/pull/8560) | Restore lock screen password focus lost on suspend | robouk | 2.8 | 1.0 | 0.97 |
| [#8599](https://github.com/omacom/omarchy/pull/8599) | Add window-relayout command to recover stuck web app layouts | megabyte0x | 2.0 | 1.1 | 0.63 |
| [#8625](https://github.com/omacom/omarchy/pull/8625) | Keep kitty font zoom when switching themes | AccursedGalaxy | 2.4 | 1.5 | 0.83 |
| [#8681](https://github.com/omacom/omarchy/pull/8681) | Hide Ghostty scrollbar in screensaver | nameproof | 2.9 | 0.9 | 0.86 |
| [#8695](https://github.com/omacom/omarchy/pull/8695) | Cap screensaver frame rate at the panel refresh rate | nbeerbower | 2.6 | 1.2 | 0.60 |
| [#8768](https://github.com/omacom/omarchy/pull/8768) | Give btop a float big enough for its 80x24 minimum | nbeerbower | 2.5 | 0.9 | 0.93 |
| [#8773](https://github.com/omacom/omarchy/pull/8773) | Fix premature lock reblank on slow displays | ClGratton | 1.8 | 2.0 | 0.96 |
| [#8802](https://github.com/omacom/omarchy/pull/8802) | Show every Hyprland workspace in the bar, not only 1-10 | kizzd | 2.1 | 1.6 | 0.73 |
| [#8825](https://github.com/omacom/omarchy/pull/8825) | Add --no-gtk option to display text size command | pazthor | 2.0 | 1.9 | 0.71 |
| [#8846](https://github.com/omacom/omarchy/pull/8846) | List the Herdr PREFIX chord first in the learn guide | daveyb | 1.9 | 1.0 | 0.81 |
| [#8876](https://github.com/omacom/omarchy/pull/8876) | Stop keybinding scans from looping on mocked APIs | yashranaway | 2.3 | 1.9 | 0.97 |
| [#8885](https://github.com/omacom/omarchy/pull/8885) | Batch window pop dispatches | yashranaway | 2.0 | 2.0 | 0.88 |
| [#8907](https://github.com/omacom/omarchy/pull/8907) | foot: render light themes into [colors-light] so foot reports the right color-th | rubas | 2.1 | 1.0 | 0.95 |
| [#8922](https://github.com/omacom/omarchy/pull/8922) | Keep the image selector fast when vips cannot read an image | bjarneo | 2.0 | 1.6 | 0.91 |
| [#8942](https://github.com/omacom/omarchy/pull/8942) | Anchor the clock and weather popups under their widgets | scottjones | 2.4 | 1.1 | 0.90 |
| [#8978](https://github.com/omacom/omarchy/pull/8978) | fix(shell): report failed desktop entry launches | fgrehm | 2.1 | 1.7 | 0.90 |
| [#8980](https://github.com/omacom/omarchy/pull/8980) | fix(shell): keep notification dismiss button visible | fgrehm | 2.8 | 1.2 | 0.91 |
| [#8982](https://github.com/omacom/omarchy/pull/8982) | Fix/monitor scale persistence named output | 69Harold69 | 1.9 | 1.2 | 0.95 |
| [#9000](https://github.com/omacom/omarchy/pull/9000) | Fix clipped left border on Display scale 1x pill | mubshrx | 2.7 | 1.0 | 0.97 |
| [#9015](https://github.com/omacom/omarchy/pull/9015) | Make scrolling columns resizable at workspace edge | hancengiz | 2.2 | 1.6 | 0.81 |
| [#9049](https://github.com/omacom/omarchy/pull/9049) | Give TUI windows a terminal-sized touchpad scroll rule | PyRo1121 | 2.4 | 1.4 | 0.90 |
| [#9129](https://github.com/omacom/omarchy/pull/9129) | Ignore vendor hotkey keyboard devices | yashranaway | 1.9 | 1.0 | 0.95 |
| [#9130](https://github.com/omacom/omarchy/pull/9130) | Send clipboard shortcuts using physical XKB keys | yashranaway | 2.0 | 1.2 | 0.95 |
| [#9133](https://github.com/omacom/omarchy/pull/9133) | Resolve keycodes with the active keyboard layout | yashranaway | 2.2 | 1.8 | 0.95 |
| [#9135](https://github.com/omacom/omarchy/pull/9135) | Let on-screen keyboards reach the menu | yashranaway | 2.2 | 1.7 | 0.95 |
| [#9186](https://github.com/omacom/omarchy/pull/9186) | Reapply clamshell disable after idle wake | pauloklaus | 1.8 | 1.0 | 0.97 |
| [#9203](https://github.com/omacom/omarchy/pull/9203) | Stop restoring a stale keyboard backlight on idle-cycle cancel | phedoreanu | 2.0 | 1.2 | 0.96 |
| [#9211](https://github.com/omacom/omarchy/pull/9211) | Wake the lock screen on resume and keep wake keys out of the password | phedoreanu | 2.3 | 1.9 | 0.88 |
| [#9245](https://github.com/omacom/omarchy/pull/9245) | Fix context menus for Wine tray items | clementrog | 2.3 | 1.9 | 0.96 |
| [#9279](https://github.com/omacom/omarchy/pull/9279) | Tag Vivaldi's window class case-insensitively in browser.lua | reverb256 | 1.9 | 0.8 | 0.97 |
| [#9280](https://github.com/omacom/omarchy/pull/9280) | Dereference relative symlinks when staging user themes | fresh3nough | 2.9 | 1.4 | 0.97 |
| [#9281](https://github.com/omacom/omarchy/pull/9281) | Fit the presentation terminal to its logo instead of a fixed 875x600 | londospark | 2.4 | 1.9 | 0.86 |
| [#9296](https://github.com/omacom/omarchy/pull/9296) | Recover screen-recording indicator after stuck probes | fresh3nough | 2.3 | 1.6 | 0.97 |
| [#9345](https://github.com/omacom/omarchy/pull/9345) | Fix slider knob stopping short of the track end | ejuro | 1.8 | 1.0 | 0.92 |
| [#9362](https://github.com/omacom/omarchy/pull/9362) | Coerce bar set values to the widget manifest type | fresh3nough | 2.4 | 1.8 | 0.97 |
| [#9408](https://github.com/omacom/omarchy/pull/9408) | Follow the icon theme inheritance chain when building the app icon index | VykosMolt | 2.2 | 2.4 | 0.87 |
| [#9479](https://github.com/omacom/omarchy/pull/9479) | Keep launched apps on the workspace they started from | ClumZeez | 2.5 | 1.9 | 0.81 |
| [#9535](https://github.com/omacom/omarchy/pull/9535) | Show browser shortcuts only when their extensions are enabled | qybaihe | 2.2 | 1.9 | 0.63 |
| [#9565](https://github.com/omacom/omarchy/pull/9565) | Keep fcitx5 aligned with Hyprland keyboard layouts | rookepoole | 1.9 | 2.4 | 0.64 |
| [#9570](https://github.com/omacom/omarchy/pull/9570) | Rearm idle monitor after timeout changes | rookepoole | 2.2 | 1.7 | 0.94 |
| [#9590](https://github.com/omacom/omarchy/pull/9590) | Clear stale graphical-session before uwsm so SDDM autologin is not a blank scree | pib-nbsmedia | 1.9 | 1.9 | 0.95 |
| [#9614](https://github.com/omacom/omarchy/pull/9614) | omarchy #9544 launch-or-focus agent titles (fork PR) | kvnloo | 2.1 | 1.6 | 0.94 |
| [#9629](https://github.com/omacom/omarchy/pull/9629) | Hide notifications during screensaver | ClGratton | 2.9 | 1.5 | 0.90 |
| [#9649](https://github.com/omacom/omarchy/pull/9649) | Deduplicate monitor outputs with matching EDIDs | pallavk | 2.2 | 2.3 | 0.89 |
| [#9667](https://github.com/omacom/omarchy/pull/9667) | fix: idle-inhibit Steam games matching steam_app_* | kvnloo | 2.0 | 1.2 | 0.95 |
| [#9742](https://github.com/omacom/omarchy/pull/9742) | Float Omawrite's file dialogs | wulujia | 2.2 | 0.6 | 0.96 |
| [#9760](https://github.com/omacom/omarchy/pull/9760) | List hybrid plugins as enabled when they live in plugins[] | ujo4eva | 2.4 | 1.1 | 0.93 |
| [#9882](https://github.com/omacom/omarchy/pull/9882) | Tag Chromium --app web apps as chromium-based browsers | fresh3nough | 2.1 | 1.1 | 0.96 |
| [#9889](https://github.com/omacom/omarchy/pull/9889) | Load workspace layout saves from the layouts directory | fresh3nough | 1.8 | 1.8 | 0.96 |
| [#9967](https://github.com/omacom/omarchy/pull/9967) | Resolve a live Hyprland signature before restarting the shell | fresh3nough | 2.0 | 1.9 | 0.97 |
| [#9972](https://github.com/omacom/omarchy/pull/9972) | Skip readonly moduleName/settings writes in bar injectProps | fresh3nough | 2.3 | 1.0 | 0.97 |
| [#9976](https://github.com/omacom/omarchy/pull/9976) | Load personal Hyprland overrides through require_optional.safe | fresh3nough | 2.6 | 1.5 | 0.96 |
| [#9978](https://github.com/omacom/omarchy/pull/9978) | Load personal hypr.envs after package Hyprland defaults | fresh3nough | 2.6 | 1.9 | 0.96 |
| [#9984](https://github.com/omacom/omarchy/pull/9984) | Render bar tooltips as StyledText for rich plugin markup | fresh3nough | 2.5 | 0.8 | 0.95 |
| [#9985](https://github.com/omacom/omarchy/pull/9985) | Resolve notification image-path through iconSource | fresh3nough | 2.3 | 0.9 | 0.96 |
| [#9986](https://github.com/omacom/omarchy/pull/9986) | Theme Hyprland decoration glow with border colors | fresh3nough | 2.2 | 1.0 | 0.93 |
| [#10002](https://github.com/omacom/omarchy/pull/10002) | Add drop-zone candidates for empty bar sections | fresh3nough | 2.1 | 1.0 | 0.94 |
| [#10077](https://github.com/omacom/omarchy/pull/10077) | Release the panel cursor when the pointer leaves a row | ludagoo | 2.4 | 2.1 | 0.87 |
| [#10106](https://github.com/omacom/omarchy/pull/10106) | Float LibreOffice file dialogs | Mina-Sayed | 2.2 | 1.0 | 0.85 |
| [#10129](https://github.com/omacom/omarchy/pull/10129) | Restore the presentation terminal after a shell restart | falser101 | 2.7 | 1.4 | 0.95 |
| [#10130](https://github.com/omacom/omarchy/pull/10130) | Re-arm the lock screen's blank timer from any input while locked | Pillumz | 1.9 | 1.2 | 0.93 |
| [#10182](https://github.com/omacom/omarchy/pull/10182) | Tag Waterfox as a Firefox-based browser | nzkritik | 2.8 | 0.2 | 0.90 |
| [#10190](https://github.com/omacom/omarchy/pull/10190) | Fix workspace indicator after monitor move | dzanaga | 2.1 | 1.0 | 0.96 |
| [#10210](https://github.com/omacom/omarchy/pull/10210) | Fix theme switcher listing a theme twice when a user override has no preview | johnsideserf | 2.2 | 1.0 | 0.97 |
| [#10274](https://github.com/omacom/omarchy/pull/10274) | Keep panel sliders from losing the pointer grab inside a ScrollView | AntoineGagnon1 | 2.9 | 1.1 | 0.97 |
| [#10277](https://github.com/omacom/omarchy/pull/10277) | Enable bar widgets for active hybrid plugins | arisgysel-design | 2.4 | 1.6 | 0.96 |
| [#10291](https://github.com/omacom/omarchy/pull/10291) | Keep the Plymouth unlock entry field on-screen for large logos | org-tekeli-borisp | 2.8 | 1.1 | 0.96 |
| [#10343](https://github.com/omacom/omarchy/pull/10343) | Don't treat pointer motion right after an output change as lock-screen activity | johnkattenhorn | 2.0 | 1.7 | 0.96 |
| [#10361](https://github.com/omacom/omarchy/pull/10361) | Raise browser windows that open behind the presentation float | gradlman | 2.1 | 1.7 | 0.95 |
| [#10383](https://github.com/omacom/omarchy/pull/10383) | Open tray menus on left-click when a menu is exposed | fresh3nough | 2.7 | 1.1 | 0.95 |
| [#10414](https://github.com/omacom/omarchy/pull/10414) | Disable broken Inhibit portal so video holds off the screensaver | DegenApeDev | 1.9 | 1.2 | 0.93 |
| [#10468](https://github.com/omacom/omarchy/pull/10468) | Name keycode bindings after the layout the keyboard is using | seletz | 2.7 | 1.9 | 0.90 |
| [#10470](https://github.com/omacom/omarchy/pull/10470) | Fix SDDM password field sometimes not getting focus on load | woodenplastic | 2.3 | 1.0 | 0.98 |
| [#10494](https://github.com/omacom/omarchy/pull/10494) | Allow Hyprland binding switches in Lua diagnostics | jfturcot | 2.8 | 0.8 | 0.69 |
| [#10549](https://github.com/omacom/omarchy/pull/10549) | Use Display P3 on Dell XPS OLED internal panels | j-c-m | 1.9 | 1.1 | 0.66 |
| [#10564](https://github.com/omacom/omarchy/pull/10564) | Skip opening an empty scratchpad on Super+S | fresh3nough | 2.6 | 1.1 | 0.95 |
| [#10565](https://github.com/omacom/omarchy/pull/10565) | Drop shift:both_capslock_cancel from default kb_options | fresh3nough | 2.4 | 1.8 | 0.74 |
| [#10570](https://github.com/omacom/omarchy/pull/10570) | Sync GDK_SCALE into app launch environments on scale change | fresh3nough | 2.1 | 1.3 | 0.96 |
| [#10571](https://github.com/omacom/omarchy/pull/10571) | Raise themed readable-text mixes to WCAG AA contrast | fresh3nough | 2.5 | 1.6 | 0.87 |
| [#10577](https://github.com/omacom/omarchy/pull/10577) | Enable resolve_binds_by_sym for high XF86 keycodes | fresh3nough | 2.7 | 1.0 | 0.77 |
| [#10578](https://github.com/omacom/omarchy/pull/10578) | Silence fcitx5 startup layout tip notifications | fresh3nough | 2.1 | 1.8 | 0.95 |
| [#10628](https://github.com/omacom/omarchy/pull/10628) | Gate active-window title to the focused monitor | fresh3nough | 2.3 | 1.8 | 0.92 |
| [#10630](https://github.com/omacom/omarchy/pull/10630) | Fix stale Wi-Fi connection state in network bar | chivopic | 1.9 | 1.1 | 0.97 |
| [#10693](https://github.com/omacom/omarchy/pull/10693) | Ignore missing group window indexes | aastrand | 2.6 | 1.0 | 0.93 |
| [#10704](https://github.com/omacom/omarchy/pull/10704) | Prevent Super+C/V/X send_key_state from retriggering the bind | gw7523 | 2.7 | 1.1 | 0.96 |
| [#10743](https://github.com/omacom/omarchy/pull/10743) | Fix Super+V in Codex's integrated terminal | Skeptomenos | 2.9 | 1.5 | 0.96 |
| [#10931](https://github.com/omacom/omarchy/pull/10931) | Preserve bar widgets when the layout changes | kristofferR | 2.6 | 2.8 | 0.83 |
| [#10958](https://github.com/omacom/omarchy/pull/10958) | Fix bar reordering for duplicate widgets | roonakyadav | 2.3 | 2.0 | 0.97 |
| [#10984](https://github.com/omacom/omarchy/pull/10984) | Pin gcr-prompter so Unlock Keyring stays on the current workspace | Literato2 | 2.1 | 1.0 | 0.84 |
| [#10989](https://github.com/omacom/omarchy/pull/10989) | fix: keep 1.25x tooltip and scale-pill borders from dropping edges | kvnloo | 2.6 | 2.0 | 0.97 |
| [#11021](https://github.com/omacom/omarchy/pull/11021) | Skip tray grab until the SNI menu has children | kvnloo | 2.7 | 1.2 | 0.96 |
| [#11034](https://github.com/omacom/omarchy/pull/11034) | Clamp notification cards to the width their container has | SimonSchubert | 2.3 | 1.2 | 0.94 |
| [#11035](https://github.com/omacom/omarchy/pull/11035) | Toggle keybindings with Super+K | KrishRVH | 2.0 | 1.0 | 0.65 |
| [#11080](https://github.com/omacom/omarchy/pull/11080) | Fix PluginBarApi hover-reveal writes so cloned panels can close | SomeoneWithOptions | 2.5 | 1.8 | 0.97 |
| [#11223](https://github.com/omacom/omarchy/pull/11223) | Refuse a theme with no palette instead of applying it | vovarbv | 2.3 | 1.1 | 0.95 |
| [#11238](https://github.com/omacom/omarchy/pull/11238) | Fit the weather panel to narrow popups | SimonSchubert | 2.3 | 1.2 | 0.95 |
| [#11239](https://github.com/omacom/omarchy/pull/11239) | Close open bar panels while the screensaver is up | ninepointlabs | 2.3 | 1.6 | 0.93 |
| [#11244](https://github.com/omacom/omarchy/pull/11244) | Clamp the lock screen's password field to the screen width | SimonSchubert | 2.2 | 1.0 | 0.94 |
| [#11269](https://github.com/omacom/omarchy/pull/11269) | Fix DaVinci Resolve Download Manager focus lock | AksharP5 | 2.3 | 0.5 | 0.96 |
| [#11414](https://github.com/omacom/omarchy/pull/11414) | Fix monitor scaling widget coupling multiple monitors' scale | bfagundez | 2.2 | 1.6 | 0.97 |
| [#11441](https://github.com/omacom/omarchy/pull/11441) | Include windows from all visible displays in screenshot picker | Tunahanyrd | 2.4 | 2.1 | 0.87 |
| [#11447](https://github.com/omacom/omarchy/pull/11447) | Ship fcitx5 wayland.conf so layouts are not pushed to the compositor | twinkybot | 2.3 | 0.5 | 0.94 |
| [#11475](https://github.com/omacom/omarchy/pull/11475) | Detach nightlight startup from captured command output | yashranaway | 2.5 | 1.0 | 0.97 |
| [#11496](https://github.com/omacom/omarchy/pull/11496) | Size the weather bar icon like the other bar icons | SemihMutlu07 | 2.5 | 1.1 | 0.74 |
| [#11578](https://github.com/omacom/omarchy/pull/11578) | Derive publicBarConfig() from shellConfig to fix one-step-late plugin APIs | AnPod | 2.2 | 1.1 | 0.97 |
| [#11610](https://github.com/omacom/omarchy/pull/11610) | Debounce AppLibrary appsChanged() against spurious DesktopEntries churn | shingoku2 | 1.9 | 1.5 | 0.96 |
| [#11639](https://github.com/omacom/omarchy/pull/11639) | Fix calendar date clipping | MBemera | 2.9 | 1.2 | 0.96 |
| [#11756](https://github.com/omacom/omarchy/pull/11756) | Dim the workspace marker on unfocused monitors | jacobs852 | 1.9 | 1.0 | 0.68 |
| [#11838](https://github.com/omacom/omarchy/pull/11838) | Fix calendar and weather popup text colours | tcballard | 2.1 | 1.2 | 0.96 |
| [#11863](https://github.com/omacom/omarchy/pull/11863) | Skip dwindle togglesplit on scrolling workspaces | Per0-1 | 2.6 | 1.1 | 0.93 |
| [#11882](https://github.com/omacom/omarchy/pull/11882) | Fix stale menu-image thumbnails after in-place overwrite (#11806) | thescurry | 2.6 | 1.2 | 0.98 |
| [#11887](https://github.com/omacom/omarchy/pull/11887) | Preserve bar space while the shell restarts | jkarmel | 2.8 | 2.9 | 0.74 |
| [#11946](https://github.com/omacom/omarchy/pull/11946) | Fix calendar hero overflowing on narrow panels (MacBook M1 Pro) | marcindyguda | 2.0 | 1.8 | 0.97 |
| [#11970](https://github.com/omacom/omarchy/pull/11970) | Wire serviceFor for installed third-party bar plugins (#11949) | thescurry | 2.4 | 1.1 | 0.97 |
| [#11981](https://github.com/omacom/omarchy/pull/11981) | Fix fullscreen Steam game window rules | flrsn | 2.0 | 2.0 | 0.94 |
| [#12022](https://github.com/omacom/omarchy/pull/12022) | Fix inverted on/off semantics of toggle bar | ram-devv1 | 2.2 | 1.8 | 0.97 |
| [#12042](https://github.com/omacom/omarchy/pull/12042) | Render every modifier Hyprland can bind in the keybindings menu | jimjimovich | 2.6 | 1.0 | 0.92 |
| [#12118](https://github.com/omacom/omarchy/pull/12118) | Make scrolling Alt-Tab follow visual order | DaDecky | 2.2 | 2.0 | 0.66 |
| [#12183](https://github.com/omacom/omarchy/pull/12183) | Keep weather widget visible when wttr.in TLS fails (#11999) | thescurry | 1.9 | 1.2 | 0.95 |
| [#12189](https://github.com/omacom/omarchy/pull/12189) | Only reload local plugins when loadable sources change | DonnieFi | 2.4 | 2.0 | 0.88 |
| [#12257](https://github.com/omacom/omarchy/pull/12257) | fix(bar/tray): collapse the tray drawer's reserved space | nas3ts | 2.1 | 1.8 | 0.91 |
| [#12258](https://github.com/omacom/omarchy/pull/12258) | Keep the screensaver up until it has been focused once | z23 | 1.9 | 1.1 | 0.96 |
| [#12307](https://github.com/omacom/omarchy/pull/12307) | Prefer a known internal touchpad when an external trackpad is connected | shmlkv | 2.6 | 1.8 | 0.85 |
| [#12360](https://github.com/omacom/omarchy/pull/12360) | Toggle a touchpad's mouse-emulation sibling with it | z23 | 2.0 | 1.8 | 0.94 |
| [#12362](https://github.com/omacom/omarchy/pull/12362) | Pin the keybindings row order to one collation | linyiru | 2.1 | 1.0 | 0.87 |
| [#12377](https://github.com/omacom/omarchy/pull/12377) | Fix emoji/clipboard paste into browsers with Ctrl+V | AndrijaSkontra | 2.2 | 1.9 | 0.92 |
| [#12385](https://github.com/omacom/omarchy/pull/12385) | Report failed theme removal before announcing success | yashranaway | 2.8 | 1.1 | 0.97 |
| [#12431](https://github.com/omacom/omarchy/pull/12431) | Fix: menu `No matches for "abc.."` message overflow | kaunkrishna | 2.1 | 0.6 | 0.92 |
| [#12512](https://github.com/omacom/omarchy/pull/12512) | Exclude covered windows from the capture picker | sanjyay | 2.9 | 1.0 | 0.96 |
| [#12517](https://github.com/omacom/omarchy/pull/12517) | Position picture-in-picture from its final size, like webcam overlay | ludagoo | 2.5 | 1.2 | 0.93 |
| [#12538](https://github.com/omacom/omarchy/pull/12538) | Treat idle timeout 0 as disabled, not immediate | paulogeyer | 2.4 | 1.0 | 0.97 |
| [#12541](https://github.com/omacom/omarchy/pull/12541) | Apply brightness to mirrored external displays | paulogeyer | 2.5 | 1.2 | 0.92 |
| [#12579](https://github.com/omacom/omarchy/pull/12579) | Keep the Omarchy screensaver from firing during VLC playback | evandrojr | 2.2 | 1.0 | 0.91 |
| [#12606](https://github.com/omacom/omarchy/pull/12606) | Inhibit idle and screensaver when browsers or video web apps are fullscreen | murdawkmedia | 2.1 | 1.1 | 0.77 |
| [#12654](https://github.com/omacom/omarchy/pull/12654) | Prevent screensaver during fullscreen browser video | Caya231 | 2.1 | 1.8 | 0.75 |
| [#12666](https://github.com/omacom/omarchy/pull/12666) | shell: clamp notification toast width to viewport; battery warning auto-expires | 0xdfi | 1.9 | 1.9 | 0.94 |
| [#12676](https://github.com/omacom/omarchy/pull/12676) | Parse keys whose type is spelled out in the keybindings menu | seletz | 2.8 | 1.2 | 0.95 |
| [#12712](https://github.com/omacom/omarchy/pull/12712) | Fix infinite iteration in keybinding scanner API stubs | wulujia | 2.6 | 1.0 | 0.97 |
| [#12763](https://github.com/omacom/omarchy/pull/12763) | Recover off-screen JetBrains Toolbox windows | nikooo777 | 2.9 | 1.3 | 0.95 |
| [#12794](https://github.com/omacom/omarchy/pull/12794) | Correct why the notification click falls back to focusing the app | davidboulay | 1.9 | 0.9 | 0.62 |
| [#12814](https://github.com/omacom/omarchy/pull/12814) | Keep panel focus during panel switches | dt-lindberg | 2.7 | 1.0 | 0.96 |
| [#12857](https://github.com/omacom/omarchy/pull/12857) | Don't reload a 0x0 monitor that already has video modes | suhitanantula | 1.9 | 1.5 | 0.95 |
| [#12862](https://github.com/omacom/omarchy/pull/12862) | Re-tile Meet meeting windows caught by the PiP rule | anandude | 2.5 | 1.5 | 0.95 |
| [#12931](https://github.com/omacom/omarchy/pull/12931) | Load high contrast VS Code themes as hc-black/hc-light | Bryan-Legend | 2.1 | 1.0 | 0.84 |
| [#12961](https://github.com/omacom/omarchy/pull/12961) | fix(hypr): layout-toggle named workspaces by name selector | kvnloo | 2.1 | 1.2 | 0.97 |
| [#12962](https://github.com/omacom/omarchy/pull/12962) | fix(lock): give session lock 1500ms to stabilize outputs | kvnloo | 2.0 | 0.1 | 0.96 |
| [#12975](https://github.com/omacom/omarchy/pull/12975) | Dismiss screensaver on pointer activity after launch settle | kvnloo | 1.9 | 2.0 | 0.95 |
| [#12991](https://github.com/omacom/omarchy/pull/12991) | fix(clipboard): paste into the window that opened the manager (#12987) | kvnloo | 2.2 | 1.7 | 0.98 |
| [#13063](https://github.com/omacom/omarchy/pull/13063) | fix: report panel plugin load failures instead of throwing | BernhardRode | 1.8 | 1.0 | 0.98 |
| [#13065](https://github.com/omacom/omarchy/pull/13065) | Update the VS Code theme CLI checks for the copied theme file | en3r0 | 2.6 | 1.2 | 0.89 |
| [#13092](https://github.com/omacom/omarchy/pull/13092) | Write the monospace rule to a conf.d drop-in, not fonts.conf | surim0n | 2.2 | 1.1 | 0.94 |
| [#13097](https://github.com/omacom/omarchy/pull/13097) | Label the weather panel with the location that supplied the weather | surim0n | 2.1 | 1.2 | 0.96 |
| [#13103](https://github.com/omacom/omarchy/pull/13103) | Refocus the origin window before pasting a picked clipboard entry | surim0n | 2.0 | 2.1 | 0.96 |
| [#13104](https://github.com/omacom/omarchy/pull/13104) | Keep the last valid shell.json when the user file is truncated | surim0n | 1.9 | 1.9 | 0.96 |
| [#13126](https://github.com/omacom/omarchy/pull/13126) | Keep the reveal mask rendering so background transitions animate | ScytheAkira | 1.9 | 1.0 | 0.97 |
| [#13132](https://github.com/omacom/omarchy/pull/13132) | Keep tmux from stamping backgrounds on self-reloading terminals | anandude | 2.5 | 1.5 | 0.91 |
| [#13133](https://github.com/omacom/omarchy/pull/13133) | Sync vscode theme test with the real-file extension | anandude | 2.9 | 1.1 | 0.91 |
| [#13190](https://github.com/omacom/omarchy/pull/13190) | Always show notification dismiss control | guillesrl | 2.4 | 1.2 | 0.61 |
| [#13255](https://github.com/omacom/omarchy/pull/13255) | Fix menu JSONC trailing-comma stripping corrupting string values | buger | 2.9 | 1.0 | 0.98 |
| [#13259](https://github.com/omacom/omarchy/pull/13259) | Force DPMS enable on system wake when status is stale | Bartok9 | 2.1 | 1.4 | 0.86 |
| [#13332](https://github.com/omacom/omarchy/pull/13332) | Fall back to hyprsunset gamma on displays without DDC/CI | C50NK4 | 2.0 | 1.8 | 0.67 |
| [#13379](https://github.com/omacom/omarchy/pull/13379) | Stop fetching system stats the power panel no longer shows | benwillems | 2.2 | 1.6 | 0.93 |
| [#13409](https://github.com/omacom/omarchy/pull/13409) | Wait for the shell (for its notification service) before launching autostart app | mihailo-obradovic | 2.0 | 1.0 | 0.94 |
| [#13473](https://github.com/omacom/omarchy/pull/13473) | Reserve only revealed tray drawer width when collapsed | AnPod | 2.1 | 1.0 | 0.96 |
| [#13475](https://github.com/omacom/omarchy/pull/13475) | Dismiss open panels and grant focus grace period on screensaver launch | AnPod | 2.6 | 1.8 | 0.96 |
| [#13483](https://github.com/omacom/omarchy/pull/13483) | Fix tooltip border clipping at fractional scales | iccodes | 1.9 | 1.0 | 0.97 |
| [#13495](https://github.com/omacom/omarchy/pull/13495) | clock: make panel SystemClock precision follow the bar's seconds detection | aasmpro | 2.5 | 1.1 | 0.87 |
| [#13497](https://github.com/omacom/omarchy/pull/13497) | Fix: white/vantablack request a Yaru grey variant no package ships | baron-hines | 2.2 | 0.9 | 0.96 |
| [#13503](https://github.com/omacom/omarchy/pull/13503) | Keep Foot's font size when changing the font | ashuttl | 2.7 | 1.0 | 0.97 |
| [#13511](https://github.com/omacom/omarchy/pull/13511) | Fix menu JSONC top-level array rendering phantom rows | buger | 2.8 | 0.8 | 0.98 |
| [#13512](https://github.com/omacom/omarchy/pull/13512) | Fix menu JSONC inline comment tails emptying the whole menu | buger | 2.8 | 1.1 | 0.98 |
| [#13541](https://github.com/omacom/omarchy/pull/13541) | Catch the bar clock up after a suspend | stevederico | 2.2 | 1.1 | 0.97 |
| [#13552](https://github.com/omacom/omarchy/pull/13552) | Route fcitx5 D-Bus activation through omarchy-fcitx5.service | Ray0907 | 2.7 | 1.5 | 0.93 |
| [#13564](https://github.com/omacom/omarchy/pull/13564) | Move the parked overlay to the focused monitor before it is shown | manuaudio | 2.9 | 1.0 | 0.97 |
| [#13579](https://github.com/omacom/omarchy/pull/13579) | Wait for the first plugin scan before building the stock bar | manuaudio | 2.2 | 1.5 | 0.97 |
| [#13580](https://github.com/omacom/omarchy/pull/13580) | Tint Cloudflare connected tray icon for light themes | ryantm | 2.3 | 1.0 | 0.70 |
| [#13581](https://github.com/omacom/omarchy/pull/13581) | Keep Google Meet browser border when switching tabs | ryantm | 2.6 | 1.1 | 0.90 |
| [#13593](https://github.com/omacom/omarchy/pull/13593) | Scale the bar spacer with the spacing scale and text size | Susensio | 2.5 | 1.0 | 0.71 |
| [#13636](https://github.com/omacom/omarchy/pull/13636) | Size bar tray drawer from reveal extent while collapsed | AnPod | 1.8 | 1.5 | 0.94 |
| [#13647](https://github.com/omacom/omarchy/pull/13647) | Clear fullscreen stolen when screensaver loses focus | AnPod | 1.9 | 1.0 | 0.96 |
| [#13658](https://github.com/omacom/omarchy/pull/13658) | Refresh bar clock when sleep monitor restarts after resume | AnPod | 1.8 | 1.0 | 0.96 |
| [#13679](https://github.com/omacom/omarchy/pull/13679) | Dismiss tray menu on activate and hide tooltip over it | AnPod | 1.9 | 1.5 | 0.82 |
| [#13684](https://github.com/omacom/omarchy/pull/13684) | Re-probe night light after each minute so the bar follows hyprsunset's schedule | Susensio | 2.2 | 1.2 | 0.95 |
| [#13709](https://github.com/omacom/omarchy/pull/13709) | fix(hyprland): reload guard skips instances whose getoption has no bool | kvnloo | 2.4 | 1.0 | 0.97 |
| [#13713](https://github.com/omacom/omarchy/pull/13713) | theme-set-claude/pi: clean up staged tmp file when settings update fails | kvnloo | 2.7 | 1.2 | 0.96 |
| [#13718](https://github.com/omacom/omarchy/pull/13718) | theme-set-pi: stop stomping the user's chosen theme on re-provision | kvnloo | 2.3 | 1.4 | 0.93 |
| [#13722](https://github.com/omacom/omarchy/pull/13722) | menu keybindings: --config requires a value, reject unknown flags | kvnloo | 2.5 | 1.2 | 0.94 |
| [#13755](https://github.com/omacom/omarchy/pull/13755) | Propagate display-power dispatch failures | mrcobas | 2.8 | 1.0 | 0.94 |
| [#13776](https://github.com/omacom/omarchy/pull/13776) | Step the bar below the screensaver while one is up | manuaudio | 2.2 | 1.2 | 0.96 |
| [#13784](https://github.com/omacom/omarchy/pull/13784) | Make the screensaver fullscreen when a layer surface holds keyboard focus | seantimm | 2.1 | 1.0 | 0.93 |
| [#13787](https://github.com/omacom/omarchy/pull/13787) | Fix square aspect toggle on scrolling workspaces | mkenter | 2.2 | 1.6 | 0.97 |
| [#13851](https://github.com/omacom/omarchy/pull/13851) | Fix clock widget rendering weekday/month names in English regardless of locale | SloBloLabs | 2.4 | 0.9 | 0.97 |

## Review candidates: fix-misc — 117 PRs

| PR | Title | Author | Model finished | Model effort | Model fix |
|---|---|---|---|---|---|
| [#6471](https://github.com/omacom/omarchy/pull/6471) | Hide sharee nodes from the Tailscale machines list | jmckible | 2.4 | 1.0 | 0.73 |
| [#6892](https://github.com/omacom/omarchy/pull/6892) | Fix emoji paste in Firefox | VBNorebert | 2.3 | 0.9 | 0.96 |
| [#7188](https://github.com/omacom/omarchy/pull/7188) | Honor OMARCHY_SCREENRECORD_USE_PORTAL when recording fullscreen | Literato2 | 2.0 | 1.0 | 0.94 |
| [#7189](https://github.com/omacom/omarchy/pull/7189) | Report screen recordings that fail to start | Literato2 | 2.0 | 1.0 | 0.93 |
| [#7216](https://github.com/omacom/omarchy/pull/7216) | Stub OSD calls in power tests | DatAIrchitect | 2.6 | 1.1 | 0.85 |
| [#7231](https://github.com/omacom/omarchy/pull/7231) | Dispatch shell commands without a login shell | achevalier-dev | 2.4 | 1.5 | 0.73 |
| [#7289](https://github.com/omacom/omarchy/pull/7289) | capture: exclude media-controller nodes from the webcam list | danteRub | 2.3 | 1.0 | 0.96 |
| [#7332](https://github.com/omacom/omarchy/pull/7332) | Scroll the Tailscale machine list independently of the panel | andrepadez | 2.0 | 1.3 | 0.75 |
| [#7402](https://github.com/omacom/omarchy/pull/7402) | Make stateful regression tests self-contained | mdenesfe | 2.1 | 1.9 | 0.93 |
| [#7405](https://github.com/omacom/omarchy/pull/7405) | Fail shell and CLI tests when ripgrep is missing | 686f6c61 | 2.6 | 1.2 | 0.95 |
| [#7406](https://github.com/omacom/omarchy/pull/7406) | Say when acceptance screenshots fail to capture | 686f6c61 | 2.4 | 1.2 | 0.96 |
| [#7491](https://github.com/omacom/omarchy/pull/7491) | Show the hourglass while dictation is transcribing | Kristijan-K | 2.5 | 1.0 | 0.96 |
| [#7551](https://github.com/omacom/omarchy/pull/7551) | Measure speedtest on the interface the transfer uses | Literato2 | 2.5 | 1.6 | 0.96 |
| [#7578](https://github.com/omacom/omarchy/pull/7578) | Clamp idle timeouts to the int32 millisecond timer ceiling | MBemera | 2.8 | 1.1 | 0.96 |
| [#7754](https://github.com/omacom/omarchy/pull/7754) | Avoid full plugin reload when discovering new plugins | sanjyay | 2.0 | 2.5 | 0.72 |
| [#7819](https://github.com/omacom/omarchy/pull/7819) | Stand down the tailscale poll watchdog once its polls exit | wico216 | 2.7 | 1.9 | 0.96 |
| [#7826](https://github.com/omacom/omarchy/pull/7826) | Finish superseded menu-select requests so their waiters exit | wico216 | 2.1 | 1.8 | 0.98 |
| [#8076](https://github.com/omacom/omarchy/pull/8076) | Stop the hybrid GPU test from failing without Omarchy installed | munzzyy | 2.9 | 0.9 | 0.96 |
| [#8128](https://github.com/omacom/omarchy/pull/8128) | Fix empty array shell IPC transport | llirik0 | 2.8 | 1.1 | 0.96 |
| [#8165](https://github.com/omacom/omarchy/pull/8165) | Give every silent test assertion a failure message | TinySkillet | 2.8 | 1.9 | 0.91 |
| [#8570](https://github.com/omacom/omarchy/pull/8570) | Focus existing windows after no-op app launches | npenza | 2.0 | 1.4 | 0.87 |
| [#8633](https://github.com/omacom/omarchy/pull/8633) | Stop network speed tests when their launcher dies | lamchun1110 | 2.1 | 2.0 | 0.96 |
| [#8692](https://github.com/omacom/omarchy/pull/8692) | Resolve mise wrapper binaries before execution | imadtg | 1.9 | 1.8 | 0.97 |
| [#8734](https://github.com/omacom/omarchy/pull/8734) | Share Voxtype status across bar surfaces | lamchun1110 | 1.9 | 2.7 | 0.71 |
| [#8741](https://github.com/omacom/omarchy/pull/8741) | Prevent network address values from overlapping labels | avk458 | 2.1 | 1.0 | 0.93 |
| [#8766](https://github.com/omacom/omarchy/pull/8766) | Fix local plugin reloads | catlee | 2.2 | 2.0 | 0.96 |
| [#8787](https://github.com/omacom/omarchy/pull/8787) | Fix lopsided cursor highlight on network panel header actions | mayaanhafeez | 2.8 | 1.0 | 0.95 |
| [#8792](https://github.com/omacom/omarchy/pull/8792) | Fix webcam MJPEG negotiation for screen recordings | ottosilva | 2.0 | 1.6 | 0.96 |
| [#8866](https://github.com/omacom/omarchy/pull/8866) | Fix network panel behind VPN policy routes | hehh2001 | 2.1 | 1.9 | 0.94 |
| [#9013](https://github.com/omacom/omarchy/pull/9013) | fix: address high-confidence shellcheck findings | fgrehm | 1.9 | 2.0 | 0.90 |
| [#9042](https://github.com/omacom/omarchy/pull/9042) | Run the screensaver exit handler exactly once | PyRo1121 | 2.5 | 1.1 | 0.98 |
| [#9161](https://github.com/omacom/omarchy/pull/9161) | Discover and normalize web app icons | DerpyCrabs | 1.9 | 2.0 | 0.76 |
| [#9344](https://github.com/omacom/omarchy/pull/9344) | Keep speed tests loaded during process cleanup | ptqa | 2.9 | 1.8 | 0.95 |
| [#9488](https://github.com/omacom/omarchy/pull/9488) | Prevent clipboard capture hangs | maxcroy1 | 2.3 | 1.9 | 0.96 |
| [#9551](https://github.com/omacom/omarchy/pull/9551) | Detect fingerprint enrollment by the enrolled entries, not the word "finger" | kahlin | 2.0 | 1.1 | 0.96 |
| [#9693](https://github.com/omacom/omarchy/pull/9693) | Pick the matching Noto CJK variant for language-tagged text | ZacharyZhang-NY | 2.1 | 2.0 | 0.93 |
| [#9819](https://github.com/omacom/omarchy/pull/9819) | Drive the launch OSD in-process so a lost close cannot strand it | Yiin | 2.8 | 1.5 | 0.94 |
| [#9903](https://github.com/omacom/omarchy/pull/9903) | Show useful app details in menu search | MansTomb | 2.0 | 1.0 | 0.66 |
| [#9973](https://github.com/omacom/omarchy/pull/9973) | Wrap polkit justification text instead of middle-eliding it | fresh3nough | 2.4 | 1.2 | 0.92 |
| [#10070](https://github.com/omacom/omarchy/pull/10070) | Remove dead Qt.clearComponentCache guard from plugin reload | fresh3nough | 2.2 | 1.0 | 0.90 |
| [#10095](https://github.com/omacom/omarchy/pull/10095) | Add live-screen fallback for capture tools | nixfred | 2.4 | 2.1 | 0.84 |
| [#10416](https://github.com/omacom/omarchy/pull/10416) | Fix cloned service lookups | imzihuailin | 2.6 | 1.7 | 0.97 |
| [#10457](https://github.com/omacom/omarchy/pull/10457) | Treat app word prefixes as label prefixes in menu search | benwillems | 2.8 | 1.0 | 0.92 |
| [#10557](https://github.com/omacom/omarchy/pull/10557) | fix: assert default-no confirmation in Hermes removal test | texasich | 2.2 | 0.9 | 0.85 |
| [#10576](https://github.com/omacom/omarchy/pull/10576) | Bust plugin component URLs on hot-reload | fresh3nough | 2.6 | 2.0 | 0.97 |
| [#10634](https://github.com/omacom/omarchy/pull/10634) | Coalesce concurrent shell restarts | chivopic | 2.4 | 1.2 | 0.97 |
| [#10679](https://github.com/omacom/omarchy/pull/10679) | Let reminders elapse during suspend | llirik0 | 2.4 | 1.1 | 0.96 |
| [#10680](https://github.com/omacom/omarchy/pull/10680) | Stop the crash watcher from reporting its own probe | llirik0 | 2.5 | 1.1 | 0.97 |
| [#10686](https://github.com/omacom/omarchy/pull/10686) | Reuse the sleep-lock failure notification | llirik0 | 2.5 | 1.9 | 0.96 |
| [#10705](https://github.com/omacom/omarchy/pull/10705) | Coalesce plugin reloads and exclude .git from inotify | gw7523 | 1.8 | 1.9 | 0.91 |
| [#10715](https://github.com/omacom/omarchy/pull/10715) | Stop package removal when the installed-package query fails | yashranaway | 2.1 | 1.2 | 0.96 |
| [#10785](https://github.com/omacom/omarchy/pull/10785) | Keep menu-plugin app-library when manifests cross the panel Instantiator | ekollof | 2.1 | 1.5 | 0.97 |
| [#11014](https://github.com/omacom/omarchy/pull/11014) | Recover shell restarts when the replacement launch is rejected | anovoselnik | 2.5 | 1.3 | 0.95 |
| [#11054](https://github.com/omacom/omarchy/pull/11054) | Fix orphaned speed test traffic when the overlay is dismissed mid-run | Melcus | 2.6 | 1.8 | 0.98 |
| [#11079](https://github.com/omacom/omarchy/pull/11079) | Keep plugin shell facades alive and intact for live consumers | joniler | 2.1 | 1.9 | 0.95 |
| [#11134](https://github.com/omacom/omarchy/pull/11134) | Reject disabling unknown plugin IDs in PluginRegistry | sanjyay | 1.8 | 1.4 | 0.95 |
| [#11177](https://github.com/omacom/omarchy/pull/11177) | Show wind in m/s for Russian locales | MicahelE | 2.8 | 2.0 | 0.74 |
| [#11235](https://github.com/omacom/omarchy/pull/11235) | Stop speedtest workers when their parent is killed | maandrij | 2.7 | 1.0 | 0.97 |
| [#11285](https://github.com/omacom/omarchy/pull/11285) | Give cloned menus their application library | sfk8815-create | 2.0 | 1.0 | 0.96 |
| [#11287](https://github.com/omacom/omarchy/pull/11287) | Explain snapshot failures caused by regular directories | hussainanjar | 2.7 | 1.8 | 0.72 |
| [#11385](https://github.com/omacom/omarchy/pull/11385) | Kill the local plugin watcher with the shell via pdeathsig | chadmandoo | 2.2 | 1.3 | 0.97 |
| [#11421](https://github.com/omacom/omarchy/pull/11421) | Fix stale city suggestions in weather location search | richardslatter | 2.6 | 1.9 | 0.97 |
| [#11483](https://github.com/omacom/omarchy/pull/11483) | Extract crash cores on disk instead of tmpfs | yashranaway | 2.5 | 1.4 | 0.84 |
| [#11520](https://github.com/omacom/omarchy/pull/11520) | fix(capture): single-flight screen recording stop and skip empty (#11508) | ansonboby | 2.3 | 1.5 | 0.98 |
| [#11606](https://github.com/omacom/omarchy/pull/11606) | Stop a web app's generated .desktop id from leaking into app search | brenoperucchi | 1.9 | 1.7 | 0.95 |
| [#11679](https://github.com/omacom/omarchy/pull/11679) | Keep living scripts off their historic siblings in Chromium fallback | anant1811 | 2.6 | 1.6 | 0.87 |
| [#11730](https://github.com/omacom/omarchy/pull/11730) | Rank an app above the menu actions that manage it | ivorycrayon | 2.4 | 1.1 | 0.92 |
| [#11847](https://github.com/omacom/omarchy/pull/11847) | Don't fail the locate test on non-UTF-8 files under bin/ | cristim | 2.8 | 0.9 | 0.97 |
| [#11918](https://github.com/omacom/omarchy/pull/11918) | Back off fingerprint retries that fail immediately | CoreyH | 1.9 | 1.6 | 0.96 |
| [#11965](https://github.com/omacom/omarchy/pull/11965) | fix: use the current login shell for desktop app launches | ralphsmith80 | 2.6 | 1.5 | 0.96 |
| [#12020](https://github.com/omacom/omarchy/pull/12020) | Ignore bytecode and temp files in local plugin watcher | ram-devv1 | 2.6 | 1.2 | 0.96 |
| [#12021](https://github.com/omacom/omarchy/pull/12021) | Escalate webcam overlay cleanup to SIGKILL and sweep on stop | ram-devv1 | 2.1 | 1.4 | 0.96 |
| [#12098](https://github.com/omacom/omarchy/pull/12098) | Remember highlighted menu item after returning from submenus | Teslicek | 2.1 | 1.3 | 0.94 |
| [#12234](https://github.com/omacom/omarchy/pull/12234) | fix(nvim): relink treesitter queries orphaned by retired lazyvim package | WhiteHades | 2.3 | 1.4 | 0.97 |
| [#12386](https://github.com/omacom/omarchy/pull/12386) | Report ASCII export write failures | yashranaway | 2.6 | 1.3 | 0.96 |
| [#12457](https://github.com/omacom/omarchy/pull/12457) | Escape font names before rewriting terminal and fontconfig files | cYoren | 2.0 | 1.8 | 0.97 |
| [#12479](https://github.com/omacom/omarchy/pull/12479) | Drop destroyed PipeWire nodes from the audio panel fallback cache | Abnersouza7 | 3.0 | 1.0 | 0.97 |
| [#12544](https://github.com/omacom/omarchy/pull/12544) | Back off fingerprint lock retries on hard device errors | thabopal | 2.1 | 1.0 | 0.96 |
| [#12575](https://github.com/omacom/omarchy/pull/12575) | Stub omarchy-osd in the system power test | davidboulay | 2.1 | 1.0 | 0.93 |
| [#12669](https://github.com/omacom/omarchy/pull/12669) | Follow symlink starting points in omarchy-menu-file | Bartok9 | 1.9 | 2.0 | 0.93 |
| [#12697](https://github.com/omacom/omarchy/pull/12697) | Preserve configured cursors for screenshots on transformed displays | DiegoYegros | 1.9 | 1.8 | 0.82 |
| [#12776](https://github.com/omacom/omarchy/pull/12776) | Restart media marquee once width bindings settle | D4RK0N3dev | 2.1 | 1.7 | 0.97 |
| [#12809](https://github.com/omacom/omarchy/pull/12809) | Use popup text color for network panel popup content | sanjyay | 2.5 | 1.7 | 0.95 |
| [#12828](https://github.com/omacom/omarchy/pull/12828) | test: avoid false failures in desktop OCR checks | jdx | 2.6 | 1.4 | 0.92 |
| [#12832](https://github.com/omacom/omarchy/pull/12832) | Escape notification body markup instead of only stripping image tags | taufderl | 2.3 | 1.2 | 0.91 |
| [#12866](https://github.com/omacom/omarchy/pull/12866) | Start speedtest measurement window on first sample | anandude | 2.5 | 1.9 | 0.96 |
| [#12867](https://github.com/omacom/omarchy/pull/12867) | Elide the head of the reminder typing line | anandude | 2.5 | 1.0 | 0.96 |
| [#12943](https://github.com/omacom/omarchy/pull/12943) | Build the clock month grid at noon so DST gaps do not repeat a day | Bartok9 | 2.2 | 1.1 | 0.96 |
| [#12966](https://github.com/omacom/omarchy/pull/12966) | Do not restart launchTimeout on retriggered launches | kvnloo | 1.9 | 1.0 | 0.97 |
| [#12967](https://github.com/omacom/omarchy/pull/12967) | Prefer weather report nearest_area over separate %l city label | kvnloo | 2.2 | 1.4 | 0.94 |
| [#12970](https://github.com/omacom/omarchy/pull/12970) | Defer tray submenu stack swaps past the click call stack | kvnloo | 2.2 | 1.4 | 0.97 |
| [#12981](https://github.com/omacom/omarchy/pull/12981) | Move plugin manifest scan into an external script | surim0n | 2.3 | 2.0 | 0.92 |
| [#12983](https://github.com/omacom/omarchy/pull/12983) | Add signal fallback to omarchy-restart-shell for IPC-wedged shells | surim0n | 2.0 | 2.0 | 0.96 |
| [#12985](https://github.com/omacom/omarchy/pull/12985) | Fix clock calendar grid shifting a day after a spring-forward DST transition | gtf-inet | 2.1 | 0.9 | 0.98 |
| [#12996](https://github.com/omacom/omarchy/pull/12996) | fix(shell): keep scoped APIs on cloned menu plugins (#12944) | kvnloo | 2.2 | 1.6 | 0.97 |
| [#13012](https://github.com/omacom/omarchy/pull/13012) | Restore menu selection when navigating back | onurersel | 1.9 | 1.9 | 0.88 |
| [#13096](https://github.com/omacom/omarchy/pull/13096) | Build the calendar grid cursor at noon, not midnight | surim0n | 2.1 | 1.0 | 0.97 |
| [#13113](https://github.com/omacom/omarchy/pull/13113) | Round weather coordinates to ~1 km before storing and sending | surim0n | 2.4 | 1.9 | 0.74 |
| [#13114](https://github.com/omacom/omarchy/pull/13114) | Skip read-only injectProps writes for the custom command module | surim0n | 2.3 | 1.0 | 0.95 |
| [#13127](https://github.com/omacom/omarchy/pull/13127) | Walk the calendar grid from noon across midnight DST switches | anandude | 2.8 | 1.8 | 0.97 |
| [#13141](https://github.com/omacom/omarchy/pull/13141) | Wait for a slow-exiting shell before restarting it | Nejcc | 2.2 | 1.1 | 0.97 |
| [#13151](https://github.com/omacom/omarchy/pull/13151) | Keep the Windows VM running through a guest restart | JamesStuder | 2.2 | 2.0 | 0.93 |
| [#13221](https://github.com/omacom/omarchy/pull/13221) | Load shell configuration before starting plugin discovery | sam-bee | 2.3 | 1.9 | 0.95 |
| [#13239](https://github.com/omacom/omarchy/pull/13239) | Bound speedtest transfers so hung endpoints cannot strand workers | Raj-Jagadeesh-A-P | 2.4 | 1.9 | 0.97 |
| [#13242](https://github.com/omacom/omarchy/pull/13242) | Invalidate image row cache when a file is edited in place | Raj-Jagadeesh-A-P | 2.0 | 1.0 | 0.97 |
| [#13340](https://github.com/omacom/omarchy/pull/13340) | Encode plugin scan records as JSONL | AFOliveira | 2.1 | 2.3 | 0.73 |
| [#13360](https://github.com/omacom/omarchy/pull/13360) | Encode transcode clipboard file URIs | HerrStolzier | 2.2 | 1.0 | 0.96 |
| [#13498](https://github.com/omacom/omarchy/pull/13498) | Fix: omarchy plugin clone can generate a colliding plugin id | baron-hines | 2.4 | 1.1 | 0.98 |
| [#13509](https://github.com/omacom/omarchy/pull/13509) | Check a clone's source before reporting it restored | yeomanse | 2.3 | 1.0 | 0.96 |
| [#13529](https://github.com/omacom/omarchy/pull/13529) | Show physical uplink in network panel with TUN proxies | LIghtJUNction | 2.6 | 1.9 | 0.93 |
| [#13557](https://github.com/omacom/omarchy/pull/13557) | Run the ShellIpc registration check without a shell | manuaudio | 2.6 | 1.0 | 0.96 |
| [#13561](https://github.com/omacom/omarchy/pull/13561) | Run the browser launcher test against the checkout's helpers | manuaudio | 2.3 | 0.9 | 0.93 |
| [#13681](https://github.com/omacom/omarchy/pull/13681) | Parse menu JSONC with string-aware comments and object roots | AnPod | 2.2 | 2.0 | 0.92 |
| [#13714](https://github.com/omacom/omarchy/pull/13714) | menu-input/menu-select: reject unknown flags | kvnloo | 2.5 | 1.2 | 0.93 |
| [#13730](https://github.com/omacom/omarchy/pull/13730) | Preserve notification images from localhost file URLs | Inference1 | 2.5 | 1.1 | 0.95 |
| [#13751](https://github.com/omacom/omarchy/pull/13751) | Walk the calendar grid at noon so a midnight DST start can't repeat a day | dhiasalhiQ | 2.7 | 1.1 | 0.97 |
| [#13769](https://github.com/omacom/omarchy/pull/13769) | Stop mise wrappers recursing when mise's activation variables are missing | andrew-boyd | 2.5 | 1.1 | 0.97 |

## Review candidates: hardware-drivers — 76 PRs

| PR | Title | Author | Model finished | Model effort | Model fix |
|---|---|---|---|---|---|
| [#6388](https://github.com/omacom/omarchy/pull/6388) | Fix ASUS ExpertBook B9406 touchpad quirk never being applied | dhh | 2.0 | 1.5 | 0.96 |
| [#6548](https://github.com/omacom/omarchy/pull/6548) | Fix audio device labels and guard seamless output switching | HANCORE-linux | 2.8 | 2.0 | 0.92 |
| [#7186](https://github.com/omacom/omarchy/pull/7186) | Report combined dual-battery status in the power panel | unleashed-nick | 2.4 | 2.2 | 0.90 |
| [#7308](https://github.com/omacom/omarchy/pull/7308) | Keep jack names on multi-port audio devices | sunblot | 2.7 | 1.1 | 0.91 |
| [#7336](https://github.com/omacom/omarchy/pull/7336) | Re-detect Apple display when cached hiddev node stops responding | 0xApotheosis | 2.2 | 1.2 | 0.96 |
| [#7459](https://github.com/omacom/omarchy/pull/7459) | Initialize the analog playback path for any ASUS ROG Realtek codec | nitine | 2.4 | 2.0 | 0.92 |
| [#7745](https://github.com/omacom/omarchy/pull/7745) | Keep Spotify volume across track changes | sdye1337 | 2.9 | 1.3 | 0.96 |
| [#7779](https://github.com/omacom/omarchy/pull/7779) | Hide Hibernate when the kernel will not accept the request | omarchybot | 2.5 | 1.1 | 0.94 |
| [#7880](https://github.com/omacom/omarchy/pull/7880) | Don't treat Bluetooth Trusted as a completed pairing | reinierbutot | 2.5 | 1.7 | 0.97 |
| [#7948](https://github.com/omacom/omarchy/pull/7948) | Stop the DMI chassis fallback in omarchy-hw-laptop reading an empty string | chubuntuarc | 2.2 | 1.0 | 0.96 |
| [#8017](https://github.com/omacom/omarchy/pull/8017) | Hibernate with shutdown mode on ThinkBook X IMH so the machine powers off | tuthan | 2.0 | 1.1 | 0.89 |
| [#8205](https://github.com/omacom/omarchy/pull/8205) | Read actual gmux display brightness | piotrsynowiec | 2.9 | 1.3 | 0.93 |
| [#8284](https://github.com/omacom/omarchy/pull/8284) | Delay the first low-battery check until UPower settles | thecdrz | 1.9 | 1.0 | 0.96 |
| [#8317](https://github.com/omacom/omarchy/pull/8317) | Show UPower device batteries in Bluetooth panel | erbmicha | 2.7 | 2.0 | 0.71 |
| [#8329](https://github.com/omacom/omarchy/pull/8329) | Detect ROG machines reporting sys_vendor as "ASUS" | ianleon | 2.6 | 0.9 | 0.96 |
| [#8712](https://github.com/omacom/omarchy/pull/8712) | Skip powerprofilesctl when daemon is down | Elshayib | 2.3 | 1.9 | 0.95 |
| [#8713](https://github.com/omacom/omarchy/pull/8713) | Resolve through EasyEffects to its configured output device | tzssangglass | 1.9 | 2.0 | 0.95 |
| [#8947](https://github.com/omacom/omarchy/pull/8947) | Set GDK_GL=gles on NVIDIA so GTK3 video playback works | danielgccr | 2.3 | 0.9 | 0.96 |
| [#9131](https://github.com/omacom/omarchy/pull/9131) | Wait for Bluetooth before starting its agent | yashranaway | 1.8 | 1.1 | 0.96 |
| [#9132](https://github.com/omacom/omarchy/pull/9132) | Resolve native EasyEffects output chains | yashranaway | 2.1 | 2.0 | 0.95 |
| [#9218](https://github.com/omacom/omarchy/pull/9218) | Detect Apple bcm5974 trackpads in omarchy-hw-touchpad | DeanWahle | 1.9 | 0.6 | 0.96 |
| [#9400](https://github.com/omacom/omarchy/pull/9400) | Keep discovery from moving a Bluetooth row out from under the pointer | VykosMolt | 2.7 | 1.8 | 0.95 |
| [#9482](https://github.com/omacom/omarchy/pull/9482) | Count GPUs without waking the one that is asleep | VykosMolt | 2.9 | 1.9 | 0.90 |
| [#9483](https://github.com/omacom/omarchy/pull/9483) | Only point the session at NVIDIA when NVIDIA is driving the screen | VykosMolt | 2.0 | 1.5 | 0.80 |
| [#9524](https://github.com/omacom/omarchy/pull/9524) | Detect Broadcom ControlVault 3 fingerprint readers | qybaihe | 2.1 | 1.2 | 0.76 |
| [#9553](https://github.com/omacom/omarchy/pull/9553) | Fix per-app stream sliders ignoring pointer input | shaynhornik | 2.3 | 1.0 | 0.98 |
| [#9612](https://github.com/omacom/omarchy/pull/9612) | omarchy #9586 sysfs battery thresholds | kvnloo | 2.5 | 1.6 | 0.87 |
| [#9638](https://github.com/omacom/omarchy/pull/9638) | Switch Bluetooth headsets to HFP when selecting their input | fresh3nough | 1.9 | 1.6 | 0.94 |
| [#9716](https://github.com/omacom/omarchy/pull/9716) | Disable WebKitGTK DMA-BUF renderer on NVIDIA | vltic | 2.5 | 1.1 | 0.89 |
| [#9755](https://github.com/omacom/omarchy/pull/9755) | Refresh monitor brightness state every second | iccodes | 2.2 | 0.9 | 0.91 |
| [#9883](https://github.com/omacom/omarchy/pull/9883) | Keep low-battery latch across AC online flaps | fresh3nough | 2.6 | 1.1 | 0.98 |
| [#9997](https://github.com/omacom/omarchy/pull/9997) | bluetooth: surface passkey prompt during device pairing | Johann-S | 1.9 | 1.1 | 0.88 |
| [#10003](https://github.com/omacom/omarchy/pull/10003) | Keep bluetooth panel visible after user powers it off | fresh3nough | 2.6 | 1.3 | 0.94 |
| [#10071](https://github.com/omacom/omarchy/pull/10071) | Dedupe sound menu output and input entries | fresh3nough | 1.8 | 1.9 | 0.88 |
| [#10076](https://github.com/omacom/omarchy/pull/10076) | Prefer kernel charge registers for battery percentage | ludagoo | 2.5 | 2.1 | 0.75 |
| [#10125](https://github.com/omacom/omarchy/pull/10125) | Avoid Baffin GPU hangs during screen recording | andrewrbrady | 2.5 | 1.8 | 0.96 |
| [#10148](https://github.com/omacom/omarchy/pull/10148) | Use software volume for Audient USB audio interfaces | kmpeeduwee | 2.0 | 1.6 | 0.85 |
| [#10191](https://github.com/omacom/omarchy/pull/10191) | Prefer the live device name when labeling Bluetooth devices | njos-444-navelin | 2.3 | 1.0 | 0.93 |
| [#10364](https://github.com/omacom/omarchy/pull/10364) | Preserve keyboard backlight across repeated blanks | catlee | 2.0 | 1.4 | 0.96 |
| [#10366](https://github.com/omacom/omarchy/pull/10366) | Fix keyboard backlight restore after screensaver dismiss | marcindyguda | 1.9 | 1.7 | 0.97 |
| [#10455](https://github.com/omacom/omarchy/pull/10455) | Wait out an in-flight sleep operation before inhibiting | codemonkey76 | 2.5 | 1.2 | 0.94 |
| [#10458](https://github.com/omacom/omarchy/pull/10458) | Enable speakers on Late 2015 21.5-inch iMacs | inspiretelapps | 2.8 | 2.0 | 0.79 |
| [#10844](https://github.com/omacom/omarchy/pull/10844) | Close Bluetooth panel after connecting | sergedoub | 2.8 | 1.0 | 0.84 |
| [#11228](https://github.com/omacom/omarchy/pull/11228) | Document Dell XPS 13 silent speaker recovery | Jdelg718 | 2.4 | 2.0 | 0.70 |
| [#11260](https://github.com/omacom/omarchy/pull/11260) | Pause Bluetooth discovery during pairing | itsMattGuenther | 2.4 | 1.9 | 0.94 |
| [#11312](https://github.com/omacom/omarchy/pull/11312) | Software brightness fallback when DRM backlight is missing | Infringer13 | 2.0 | 2.3 | 0.69 |
| [#11415](https://github.com/omacom/omarchy/pull/11415) | Dismiss stale low battery warnings | gaburn | 2.1 | 1.4 | 0.95 |
| [#11516](https://github.com/omacom/omarchy/pull/11516) | Ignore USB Touch Bar DRM when detecting external displays | hanscnelson | 2.6 | 1.1 | 0.94 |
| [#11675](https://github.com/omacom/omarchy/pull/11675) | Keep Activity from waking a runtime-suspended NVIDIA GPU | anant1811 | 2.6 | 1.9 | 0.93 |
| [#11785](https://github.com/omacom/omarchy/pull/11785) | Serialize repeating volume adjustments | Yiteng-CHEN | 2.3 | 1.9 | 0.89 |
| [#11835](https://github.com/omacom/omarchy/pull/11835) | fix: toggle every touchscreen digitizer | Per0-1 | 2.4 | 1.9 | 0.97 |
| [#11836](https://github.com/omacom/omarchy/pull/11836) | Skip screen digitizers when detecting the touchpad | Per0-1 | 2.8 | 1.1 | 0.93 |
| [#11937](https://github.com/omacom/omarchy/pull/11937) | Restart Bluetooth agent when BlueZ is replaced | n0mahd | 2.2 | 2.1 | 0.92 |
| [#12175](https://github.com/omacom/omarchy/pull/12175) | Move only application streams when switching the audio input | HazAT | 2.4 | 1.0 | 0.95 |
| [#12231](https://github.com/omacom/omarchy/pull/12231) | List local audio outputs before network ones in the audio panel | mike-echo-oscar-whiskey | 2.0 | 1.8 | 0.62 |
| [#12241](https://github.com/omacom/omarchy/pull/12241) | Keep bluetooth bar icon visible after adapter disappears | RushiChaganti | 2.1 | 1.1 | 0.88 |
| [#12300](https://github.com/omacom/omarchy/pull/12300) | Fix fronted sink detection for community speaker tunings | shmlkv | 2.6 | 1.8 | 0.97 |
| [#12387](https://github.com/omacom/omarchy/pull/12387) | Detect the Chipsailing CS9711 USB reader | yashranaway | 2.8 | 1.0 | 0.92 |
| [#12504](https://github.com/omacom/omarchy/pull/12504) | Skip force-igpu Vfio dance when no NVIDIA GPU is present | paulogeyer | 2.4 | 1.0 | 0.95 |
| [#12634](https://github.com/omacom/omarchy/pull/12634) | Wake displays before restoring keyboard and clamshell state | RenanBezerraGuima | 2.7 | 1.6 | 0.76 |
| [#12769](https://github.com/omacom/omarchy/pull/12769) | Handle low-resolution brightness deltas safely | sonique6784 | 2.1 | 1.9 | 0.94 |
| [#12785](https://github.com/omacom/omarchy/pull/12785) | fix: correct Khadas Mind Graphics Speaker volume mapping | hyf4053 | 2.6 | 1.1 | 0.97 |
| [#12842](https://github.com/omacom/omarchy/pull/12842) | fix(audio): resolve the fronted sink from the running graph, not only from a shi | sneemgp | 1.9 | 1.2 | 0.97 |
| [#12863](https://github.com/omacom/omarchy/pull/12863) | Retry Bluetooth pairing once on failure | nixfred | 2.5 | 1.0 | 0.93 |
| [#12950](https://github.com/omacom/omarchy/pull/12950) | Keep Bluetooth USB controllers awake when TLP manages USB power | s-gato | 2.0 | 1.3 | 0.90 |
| [#12953](https://github.com/omacom/omarchy/pull/12953) | Detect Realtek USB Finger Print readers (2541) | Chessing234 | 1.9 | 1.4 | 0.93 |
| [#13016](https://github.com/omacom/omarchy/pull/13016) | Derive power panel charge direction from settled battery state | jaderfeijo | 2.3 | 1.8 | 0.96 |
| [#13099](https://github.com/omacom/omarchy/pull/13099) | Write output volume through pactl, not the node-bound setter | surim0n | 2.0 | 1.1 | 0.96 |
| [#13111](https://github.com/omacom/omarchy/pull/13111) | Fall back to UPower when the sysfs battery rate is implausible | surim0n | 2.6 | 1.2 | 0.96 |
| [#13189](https://github.com/omacom/omarchy/pull/13189) | Force software video decode in Chromium on NVIDIA GPUs with GSP firmware | jampick | 2.3 | 1.3 | 0.95 |
| [#13373](https://github.com/omacom/omarchy/pull/13373) | Keep UVC webcams at a fixed frame rate | phil-bowens | 2.8 | 1.5 | 0.88 |
| [#13396](https://github.com/omacom/omarchy/pull/13396) | Resolve the audio output sink through EasyEffects 8 | stefanoverna | 2.1 | 1.8 | 0.96 |
| [#13600](https://github.com/omacom/omarchy/pull/13600) | Reset elan_i2c trackpads and fail clearly when none match | AnPod | 1.9 | 1.4 | 0.96 |
| [#13711](https://github.com/omacom/omarchy/pull/13711) | Require the pattern argument in omarchy-hw-match | kvnloo | 2.8 | 1.0 | 0.95 |
| [#13715](https://github.com/omacom/omarchy/pull/13715) | brightness-keyboard: reject unknown directions before touching hardware | kvnloo | 1.8 | 1.1 | 0.95 |
| [#13744](https://github.com/omacom/omarchy/pull/13744) | Detect NEXT Biometrics readers as fingerprint hardware | lovecamera68-ai | 2.9 | 0.7 | 0.93 |

## Review candidates: shell-cli — 44 PRs

| PR | Title | Author | Model finished | Model effort | Model fix |
|---|---|---|---|---|---|
| [#6761](https://github.com/omacom/omarchy/pull/6761) | Keep tmux clipboard copies working over mosh | yashranaway | 2.0 | 2.3 | 0.94 |
| [#6839](https://github.com/omacom/omarchy/pull/6839) | Show errors from the open helper | yashranaway | 1.9 | 1.0 | 0.91 |
| [#7235](https://github.com/omacom/omarchy/pull/7235) | Don't let a failed self-update abort a working mise-wrapped tool | pedrosekine | 2.4 | 1.0 | 0.91 |
| [#7338](https://github.com/omacom/omarchy/pull/7338) | Remove redundant tmux escape-time setting | thomasdoan | 2.2 | 0.3 | 0.68 |
| [#7365](https://github.com/omacom/omarchy/pull/7365) | Stop advertising empty command groups in omarchy --help | 686f6c61 | 2.9 | 1.1 | 0.95 |
| [#7366](https://github.com/omacom/omarchy/pull/7366) | Stop cloning plugins into the reserved omarchy.* namespace | 686f6c61 | 2.7 | 1.0 | 0.96 |
| [#7370](https://github.com/omacom/omarchy/pull/7370) | Fire the restart-terminal toast after a font change | 686f6c61 | 2.9 | 0.7 | 0.98 |
| [#7387](https://github.com/omacom/omarchy/pull/7387) | plugin cli: force LC_ALL=C so plugin ids validate under any locale | jjanis | 2.6 | 1.4 | 0.97 |
| [#7796](https://github.com/omacom/omarchy/pull/7796) | Drop stale group descriptions from CLI router | Shaivarth | 2.3 | 1.0 | 0.87 |
| [#8084](https://github.com/omacom/omarchy/pull/8084) | Leave the alternate screen only when the connection dropped | eng1n88r | 2.9 | 1.0 | 0.96 |
| [#8597](https://github.com/omacom/omarchy/pull/8597) | Preserve alacritty font styles when changing font family | ParadokS81 | 2.5 | 1.0 | 0.97 |
| [#8941](https://github.com/omacom/omarchy/pull/8941) | Add omarchy-ascii so stable matches the published branding manual | fresh3nough | 2.8 | 2.0 | 0.84 |
| [#9040](https://github.com/omacom/omarchy/pull/9040) | Hand the presentation terminal Omarchy's BROWSER default | PyRo1121 | 1.9 | 1.0 | 0.95 |
| [#9164](https://github.com/omacom/omarchy/pull/9164) | Default OMARCHY_PATH in channel-current and audio-tuning; add env-robustness tes | kfchai | 1.9 | 1.3 | 0.92 |
| [#9425](https://github.com/omacom/omarchy/pull/9425) | Keep four commands from building a path that climbs out of its directory | VykosMolt | 2.6 | 1.9 | 0.95 |
| [#9583](https://github.com/omacom/omarchy/pull/9583) | Exec mise wrappers by resolved path, not by name | mrdavidlaing | 2.6 | 1.7 | 0.96 |
| [#9977](https://github.com/omacom/omarchy/pull/9977) | Keep wttr coordinate fallbacks intact in weather location | fresh3nough | 2.7 | 1.0 | 0.96 |
| [#10259](https://github.com/omacom/omarchy/pull/10259) | Report Custom DNS when public resolvers are only secondary | fresh3nough | 2.2 | 1.1 | 0.96 |
| [#10716](https://github.com/omacom/omarchy/pull/10716) | Keep drive selector arguments on separate rows | yashranaway | 2.0 | 1.0 | 0.91 |
| [#10847](https://github.com/omacom/omarchy/pull/10847) | fix: clamp omarchy commands table to terminal width | harlanljones | 2.0 | 1.0 | 0.92 |
| [#11117](https://github.com/omacom/omarchy/pull/11117) | Make the closing plugin rescan best-effort | Mario-Mohar | 2.1 | 1.3 | 0.95 |
| [#11205](https://github.com/omacom/omarchy/pull/11205) | Fix default tmux splits to preserve the current directory | SamRoehrich | 2.5 | 1.0 | 0.71 |
| [#11482](https://github.com/omacom/omarchy/pull/11482) | Preserve presentation command exit status | yashranaway | 2.3 | 1.1 | 0.93 |
| [#11670](https://github.com/omacom/omarchy/pull/11670) | Render git ahead/behind counts in the starship prompt | anant1811 | 2.8 | 1.0 | 0.94 |
| [#11742](https://github.com/omacom/omarchy/pull/11742) | Coerce omarchy-show-done exit code to numeric before arithmetic test | foxxmo51 | 2.7 | 1.0 | 0.97 |
| [#11853](https://github.com/omacom/omarchy/pull/11853) | Cover omarchy debug dispatch in CLI tests | rishabhiskawai | 2.0 | 1.0 | 0.79 |
| [#11962](https://github.com/omacom/omarchy/pull/11962) | Keep alias and id separators searchable in the menu | a-kar | 2.1 | 1.1 | 0.96 |
| [#12138](https://github.com/omacom/omarchy/pull/12138) | Keep both coordinates when wttr.in auto-detects a location as lat,lon | SirJul1337 | 3.0 | 1.0 | 0.97 |
| [#12364](https://github.com/omacom/omarchy/pull/12364) | Only restart the shell after Voxtype configure if the config changed | Yacl222 | 2.8 | 1.0 | 0.87 |
| [#12456](https://github.com/omacom/omarchy/pull/12456) | Quote OMARCHY_PATH in the function loader glob | cYoren | 2.5 | 0.9 | 0.97 |
| [#12600](https://github.com/omacom/omarchy/pull/12600) | font-set: actually show the terminal restart notification | llkkk | 2.3 | 1.6 | 0.98 |
| [#12670](https://github.com/omacom/omarchy/pull/12670) | omarchy-font-set: fire terminal-restart notifications and stop leaking PIDs (#12 | juan-LARRAYA | 2.3 | 1.7 | 0.97 |
| [#12837](https://github.com/omacom/omarchy/pull/12837) | Fix tab completion for typed omarchy-* commands | Zelmari | 2.6 | 1.0 | 0.96 |
| [#12841](https://github.com/omacom/omarchy/pull/12841) | Fix omarchy-launch-browser crashing Chrome when man-db is absent | AyanMulla09 | 2.9 | 1.0 | 0.98 |
| [#12992](https://github.com/omacom/omarchy/pull/12992) | fix(shell): keep last valid shell.json when the file truncates (#12990) | kvnloo | 2.6 | 1.1 | 0.97 |
| [#13018](https://github.com/omacom/omarchy/pull/13018) | Fix #12665: omarchy-menu-file returns 0 files when ~/Pictures/~/Videos are symli | yashbijlani | 2.0 | 1.2 | 0.97 |
| [#13116](https://github.com/omacom/omarchy/pull/13116) | Only leave the alternate screen after SSH when it is still on | fbritoferreira | 1.8 | 1.4 | 0.96 |
| [#13345](https://github.com/omacom/omarchy/pull/13345) | Show plugin update diffs without git's pager | elberacasa | 1.9 | 0.6 | 0.93 |
| [#13446](https://github.com/omacom/omarchy/pull/13446) | Add the Ctrl+Shift clipboard chords to older foot configs | stevederico | 2.4 | 1.3 | 0.88 |
| [#13614](https://github.com/omacom/omarchy/pull/13614) | Guard mise stubs against PATH recursion when a tool is missing | AnPod | 2.0 | 2.0 | 0.95 |
| [#13706](https://github.com/omacom/omarchy/pull/13706) | Avoid sentence-ending periods in clipboard links | Inference1 | 2.4 | 1.0 | 0.93 |
| [#13712](https://github.com/omacom/omarchy/pull/13712) | dev font add: require --codepoint in the private-use range | kvnloo | 2.5 | 1.1 | 0.95 |
| [#13716](https://github.com/omacom/omarchy/pull/13716) | restart-app: require the application name | kvnloo | 1.9 | 1.0 | 0.91 |
| [#13720](https://github.com/omacom/omarchy/pull/13720) | group listing: describe the visible share/show/upgrade groups | kvnloo | 2.3 | 0.9 | 0.76 |

## Review candidates: apps-integrations — 42 PRs

| PR | Title | Author | Model finished | Model effort | Model fix |
|---|---|---|---|---|---|
| [#5934](https://github.com/omacom/omarchy/pull/5934) | omarchy-webapp-install: set StartupWMClass so app switchers find the icon | andyjeffries | 2.6 | 0.9 | 0.93 |
| [#6333](https://github.com/omacom/omarchy/pull/6333) | Prevent Chromium Vulkan crashes on Wayland | a-b | 1.9 | 1.9 | 0.87 |
| [#7356](https://github.com/omacom/omarchy/pull/7356) | Detect the tailscale CLI without the which package | anupanup2001 | 2.9 | 1.0 | 0.96 |
| [#7599](https://github.com/omacom/omarchy/pull/7599) | Convert downloaded web app icons to PNG | pjgeutjens | 2.3 | 2.0 | 0.89 |
| [#7778](https://github.com/omacom/omarchy/pull/7778) | Remove GeForce NOW launcher leftovers on uninstall | husamemadH | 2.9 | 1.2 | 0.97 |
| [#7797](https://github.com/omacom/omarchy/pull/7797) | Add Remove > 1Password to the shell menu | Shaivarth | 2.2 | 0.9 | 0.66 |
| [#8153](https://github.com/omacom/omarchy/pull/8153) | Repair Copy URL after install-time migration stamping | Chessing234 | 1.9 | 2.1 | 0.96 |
| [#8299](https://github.com/omacom/omarchy/pull/8299) | Launch Opera webapps as a tab URL instead of --app= | Ojisan1 | 2.4 | 1.1 | 0.95 |
| [#8343](https://github.com/omacom/omarchy/pull/8343) | Fix omarchy share clipboard sending an empty file for image clipboard content | dima-engineer | 2.3 | 1.7 | 0.97 |
| [#8379](https://github.com/omacom/omarchy/pull/8379) | Use the real game title for RetroArch launchers installed from arcade ROMs | axelfontaine | 2.8 | 1.8 | 0.74 |
| [#8533](https://github.com/omacom/omarchy/pull/8533) | fix(tailscale): isolate claim path argument | ketpatil77 | 2.3 | 1.0 | 0.95 |
| [#8761](https://github.com/omacom/omarchy/pull/8761) | Keep mailto parameters out of HEY's recipient | tony-roslund | 1.9 | 1.0 | 0.97 |
| [#8874](https://github.com/omacom/omarchy/pull/8874) | Make the Dropbox and Tailscale service removers executable | Maero47 | 2.4 | 1.0 | 0.96 |
| [#8879](https://github.com/omacom/omarchy/pull/8879) | Use Sunshine's packaged systemd unit | yashranaway | 2.1 | 1.1 | 0.96 |
| [#8932](https://github.com/omacom/omarchy/pull/8932) | Tile the Battle.net client instead of floating it | michielvandermeer | 2.1 | 2.1 | 0.88 |
| [#9128](https://github.com/omacom/omarchy/pull/9128) | Detect browser families without launching them | yashranaway | 1.9 | 1.4 | 0.94 |
| [#9364](https://github.com/omacom/omarchy/pull/9364) | Label Tailscale profiles by tailnet, not nickname | fresh3nough | 2.8 | 1.0 | 0.96 |
| [#9365](https://github.com/omacom/omarchy/pull/9365) | Fail terminal install before rewriting the default | fresh3nough | 2.8 | 1.4 | 0.98 |
| [#9431](https://github.com/omacom/omarchy/pull/9431) | Read the default browser once, and recognise one that registered itself | VykosMolt | 2.7 | 1.9 | 0.86 |
| [#9449](https://github.com/omacom/omarchy/pull/9449) | Read the default terminal back from the file that sets it | VykosMolt | 2.5 | 1.8 | 0.91 |
| [#9621](https://github.com/omacom/omarchy/pull/9621) | Set StartupWMClass on Chromium web app launchers | seanpk | 1.9 | 1.4 | 0.79 |
| [#9927](https://github.com/omacom/omarchy/pull/9927) | Avoid focusing Quickshell plugin windows | imzihuailin | 2.2 | 1.9 | 0.91 |
| [#10513](https://github.com/omacom/omarchy/pull/10513) | Drop browser codec preloads from yt-dlp host | Drecullith | 2.3 | 1.0 | 0.96 |
| [#10567](https://github.com/omacom/omarchy/pull/10567) | Match the class the standalone Battle.net install produces | pmbemax | 2.3 | 0.9 | 0.93 |
| [#11344](https://github.com/omacom/omarchy/pull/11344) | Support both zed and zeditor editor binaries | rand0mdud3 | 2.7 | 2.0 | 0.74 |
| [#11393](https://github.com/omacom/omarchy/pull/11393) | Use a generic icon when webapp favicon lookup fails | nicknack5050 | 2.1 | 1.9 | 0.61 |
| [#11631](https://github.com/omacom/omarchy/pull/11631) | Open web app links in the default browser | tumbleweedlabs | 2.1 | 2.1 | 0.73 |
| [#11758](https://github.com/omacom/omarchy/pull/11758) | Enable native Wayland rendering for Spotify | RVPick | 2.4 | 1.9 | 0.76 |
| [#11955](https://github.com/omacom/omarchy/pull/11955) | Keep the Dropbox panel polling until the account link completes | procrypto | 2.6 | 2.0 | 0.90 |
| [#11998](https://github.com/omacom/omarchy/pull/11998) | fix: type image path when pasting clipboard images into terminals | HIMANSHU11827 | 2.5 | 1.1 | 0.96 |
| [#12256](https://github.com/omacom/omarchy/pull/12256) | Probe Tailscale with omarchy-cmd-present instead of which | z23 | 2.0 | 1.0 | 0.96 |
| [#12533](https://github.com/omacom/omarchy/pull/12533) | Resolve wrapped desktop Exec= in browser and webapp launchers | paulogeyer | 2.7 | 1.5 | 0.97 |
| [#12781](https://github.com/omacom/omarchy/pull/12781) | Let the Dropbox widget take an explicit storage quota | ihoka | 2.1 | 1.6 | 0.61 |
| [#12801](https://github.com/omacom/omarchy/pull/12801) | Explicitly set text/plain UTF-8 MIME type in omarchy-clipboard-paste-text | sanjyay | 2.6 | 1.0 | 0.96 |
| [#12974](https://github.com/omacom/omarchy/pull/12974) | Stop Dropbox panel inventing quota from plan name | kvnloo | 2.0 | 1.3 | 0.95 |
| [#12988](https://github.com/omacom/omarchy/pull/12988) | Stop dropbox-cli status polling while Dropbox is unlinked | surim0n | 2.5 | 1.2 | 0.97 |
| [#13123](https://github.com/omacom/omarchy/pull/13123) | Default image opens to imv-dir for folder navigation | anandude | 2.9 | 1.2 | 0.77 |
| [#13685](https://github.com/omacom/omarchy/pull/13685) | Fix Obsidian Electron flags and float Mullvad VPN | AnPod | 1.9 | 1.7 | 0.88 |
| [#13710](https://github.com/omacom/omarchy/pull/13710) | Refuse to launch when no default browser is configured | kvnloo | 2.7 | 1.1 | 0.96 |
| [#13830](https://github.com/omacom/omarchy/pull/13830) | Read the default browser without xdg-settings | hegjon | 1.9 | 1.9 | 0.85 |
| [#13843](https://github.com/omacom/omarchy/pull/13843) | Provision Helix theme links for existing installations | Susensio | 2.1 | 1.7 | 0.85 |
| [#13858](https://github.com/omacom/omarchy/pull/13858) | Hide Hermes' renamed CLI launcher from Apps | manuaudio | 2.5 | 0.6 | 0.96 |

## Review candidates: agents-ai — 30 PRs

| PR | Title | Author | Model finished | Model effort | Model fix |
|---|---|---|---|---|---|
| [#6478](https://github.com/omacom/omarchy/pull/6478) | Attribute Codex sessions to their model from thread settings | dalmasluca | 2.2 | 1.6 | 0.96 |
| [#7298](https://github.com/omacom/omarchy/pull/7298) | Stop the agents panel scrolling by a few pixels | YehudaGurovich | 2.2 | 1.0 | 0.67 |
| [#7924](https://github.com/omacom/omarchy/pull/7924) | Fix Codex usage collector's stale --ask-for-approval value | iaikanshb | 2.8 | 0.3 | 0.97 |
| [#8004](https://github.com/omacom/omarchy/pull/8004) | Stop killing running opencode sessions when changing themes | ADIBAINS | 2.2 | 1.0 | 0.95 |
| [#8073](https://github.com/omacom/omarchy/pull/8073) | fix: detect early Codex app-server exits | dcalliari | 1.9 | 1.9 | 0.96 |
| [#8254](https://github.com/omacom/omarchy/pull/8254) | Defeat mise's release cooldown when selecting the default agent | yashksaini-coder | 2.6 | 0.6 | 0.96 |
| [#8257](https://github.com/omacom/omarchy/pull/8257) | Warn the agent skill off pulling graphical-session.target | kkoontz | 2.1 | 2.0 | 0.73 |
| [#9550](https://github.com/omacom/omarchy/pull/9550) | fix(polkit) Attribute polkit prompts to coding agents | tcballard | 2.1 | 1.7 | 0.62 |
| [#9697](https://github.com/omacom/omarchy/pull/9697) | Report unreadable Claude transcripts once per scan | shaynhornik | 1.8 | 1.0 | 0.96 |
| [#10067](https://github.com/omacom/omarchy/pull/10067) | Add fallback reload Timer for agent usage records | fresh3nough | 2.2 | 1.1 | 0.94 |
| [#10330](https://github.com/omacom/omarchy/pull/10330) | Add a dedicated pi agent usage collector | surim0n | 1.9 | 3.0 | 0.65 |
| [#10531](https://github.com/omacom/omarchy/pull/10531) | Skip unchanged native Codex token snapshots | Brams-s | 1.9 | 1.7 | 0.91 |
| [#10606](https://github.com/omacom/omarchy/pull/10606) | Count streamed Claude messages by their highest-output usage line | st-eez | 2.5 | 1.3 | 0.96 |
| [#11267](https://github.com/omacom/omarchy/pull/11267) | Silence Claude auth nag when local API usage exists | barrydeen | 2.5 | 1.9 | 0.91 |
| [#11360](https://github.com/omacom/omarchy/pull/11360) | Fix debuginfod initialization in diagnose-crash skill | LouisDeconinck | 2.3 | 1.1 | 0.96 |
| [#11466](https://github.com/omacom/omarchy/pull/11466) | Tell the agent skill to use omarchy pkg and omarchy update, not pacman | daja77 | 1.9 | 2.0 | 0.78 |
| [#12547](https://github.com/omacom/omarchy/pull/12547) | Activate the Omarchy theme for Claude Code when it's set as the agent | prusso | 2.1 | 1.6 | 0.70 |
| [#12979](https://github.com/omacom/omarchy/pull/12979) | Fix Codex usage timeouts on batched replies | orienw | 2.9 | 2.1 | 0.97 |
| [#12986](https://github.com/omacom/omarchy/pull/12986) | fix(agents): surface stale usage from record updatedAt (#12849) | kvnloo | 2.2 | 1.9 | 0.93 |
| [#13059](https://github.com/omacom/omarchy/pull/13059) | Describe Codex rate-limit RPC timeouts instead of the method name | Bartok9 | 2.5 | 1.0 | 0.92 |
| [#13102](https://github.com/omacom/omarchy/pull/13102) | Read codex app-server replies unbuffered in the usage collector | surim0n | 2.5 | 1.9 | 0.96 |
| [#13209](https://github.com/omacom/omarchy/pull/13209) | fix(agents): count pi sessions when HOME is a git checkout | kvnloo | 2.7 | 0.8 | 0.98 |
| [#13339](https://github.com/omacom/omarchy/pull/13339) | Guard synced agent snapshot aggregation | AFOliveira | 2.1 | 2.2 | 0.90 |
| [#13458](https://github.com/omacom/omarchy/pull/13458) | Raise Codex usage RPC timeout from 4s to 10s | AnPod | 2.8 | 0.4 | 0.93 |
| [#13464](https://github.com/omacom/omarchy/pull/13464) | Make Codex account/read optional in the usage collector | AnPod | 2.8 | 1.2 | 0.94 |
| [#13611](https://github.com/omacom/omarchy/pull/13611) | Give default agents explicit mise packages including Copilot npm | AnPod | 1.8 | 1.6 | 0.92 |
| [#13621](https://github.com/omacom/omarchy/pull/13621) | Scan Codex pi sessions with rg --no-ignore | AnPod | 2.1 | 1.0 | 0.95 |
| [#13693](https://github.com/omacom/omarchy/pull/13693) | Sync the Pi theme into PI_CODING_AGENT_DIR when it is set | manuaudio | 2.3 | 1.1 | 0.94 |
| [#13703](https://github.com/omacom/omarchy/pull/13703) | Fix Codex limits timing out on buffered app-server replies | tossbaws | 2.0 | 1.4 | 0.96 |
| [#13740](https://github.com/omacom/omarchy/pull/13740) | Keep RPC method names out of the Codex limits help text | alanw707 | 2.4 | 1.3 | 0.92 |

## Review candidates: update-release — 23 PRs

| PR | Title | Author | Model finished | Model effort | Model fix |
|---|---|---|---|---|---|
| [#6972](https://github.com/omacom/omarchy/pull/6972) | Restore leftover app-menu icons after the Quattro upgrade | calledtoconstruct | 2.3 | 1.9 | 0.96 |
| [#7398](https://github.com/omacom/omarchy/pull/7398) | Resolve package-backed OMARCHY_PATH symlinks | mdenesfe | 2.4 | 1.9 | 0.97 |
| [#7400](https://github.com/omacom/omarchy/pull/7400) | Prevent duplicate agents widget during migration | mdenesfe | 2.3 | 1.4 | 0.98 |
| [#8042](https://github.com/omacom/omarchy/pull/8042) | Regenerate mise wrappers that still print mise's output to stdout (backport of # | dhh | 2.1 | 1.2 | 0.96 |
| [#8081](https://github.com/omacom/omarchy/pull/8081) | Stop AUR daemons from keeping the omarchy-update lock | kdriedger | 2.9 | 1.2 | 0.97 |
| [#8399](https://github.com/omacom/omarchy/pull/8399) | Migrate invitation hooks to notification argv | salemsayed | 2.1 | 2.1 | 0.87 |
| [#8992](https://github.com/omacom/omarchy/pull/8992) | Skip reboot prompts in unattended updates | maxcroy1 | 2.5 | 1.9 | 0.88 |
| [#9286](https://github.com/omacom/omarchy/pull/9286) | Skip tmux.conf migration when the file is not writable | fresh3nough | 2.9 | 1.1 | 0.97 |
| [#9423](https://github.com/omacom/omarchy/pull/9423) | Bound the browser policy refresh so a wedged browser can't stall an update | VykosMolt | 2.4 | 1.6 | 0.94 |
| [#9568](https://github.com/omacom/omarchy/pull/9568) | Defer XCompose reloads from migrations | rookepoole | 2.1 | 1.3 | 0.89 |
| [#10066](https://github.com/omacom/omarchy/pull/10066) | Distinguish checkupdates failure from up to date in update widget | fresh3nough | 2.6 | 1.3 | 0.96 |
| [#10232](https://github.com/omacom/omarchy/pull/10232) | fix(update): detect aarch64 kernels without vmlinuz | kvnloo | 1.8 | 1.1 | 0.96 |
| [#10524](https://github.com/omacom/omarchy/pull/10524) | Avoid reboot prompts after identical Hyprland reinstalls | Brams-s | 2.4 | 1.9 | 0.95 |
| [#11217](https://github.com/omacom/omarchy/pull/11217) | Exit cleanly when the update log is missing | Bartok9 | 2.1 | 1.0 | 0.95 |
| [#11480](https://github.com/omacom/omarchy/pull/11480) | Serialize package availability checks across callers | yashranaway | 2.3 | 1.8 | 0.95 |
| [#12174](https://github.com/omacom/omarchy/pull/12174) | Give the Mise PATH cleanup a collision-free migration id | ekollof | 2.2 | 0.8 | 0.95 |
| [#12421](https://github.com/omacom/omarchy/pull/12421) | Route Chromium notifications through the system center without joining flags | sprajs | 2.1 | 1.2 | 0.75 |
| [#12503](https://github.com/omacom/omarchy/pull/12503) | Skip CUPS discovery cleanup when the scheduler is stopped | paulogeyer | 2.5 | 1.0 | 0.96 |
| [#12797](https://github.com/omacom/omarchy/pull/12797) | Retry omarchy-bar put when omarchy-shell times out while busy | sanjyay | 2.1 | 1.0 | 0.97 |
| [#12860](https://github.com/omacom/omarchy/pull/12860) | Default OMARCHY_PATH in update-dev and channel-current | anandude | 2.7 | 1.5 | 0.95 |
| [#13538](https://github.com/omacom/omarchy/pull/13538) | Say which files block an upgrade the conflict recovery won't clear | stevederico | 2.4 | 1.1 | 0.75 |
| [#13556](https://github.com/omacom/omarchy/pull/13556) | Keep the Elsewhen migration test out of the real cache | manuaudio | 2.9 | 1.0 | 0.96 |
| [#13617](https://github.com/omacom/omarchy/pull/13617) | Skip orphan gum confirm when omarchy-update runs unattended | AnPod | 2.1 | 1.1 | 0.95 |

## Review candidates: install-setup — 17 PRs

| PR | Title | Author | Model finished | Model effort | Model fix |
|---|---|---|---|---|---|
| [#7473](https://github.com/omacom/omarchy/pull/7473) | Preserve XCompose customizations on setup rerun | nsumbadze | 2.5 | 1.0 | 0.95 |
| [#8091](https://github.com/omacom/omarchy/pull/8091) | Keep provisioning inside the user's configured XDG directories | samirpokharel | 2.5 | 1.4 | 0.95 |
| [#8141](https://github.com/omacom/omarchy/pull/8141) | Fix install-and-launch done prompt race | CooperSheroy | 1.9 | 1.3 | 0.95 |
| [#8486](https://github.com/omacom/omarchy/pull/8486) | Detect Broadcom fingerprint readers by vendor ID | gbillium143 | 2.7 | 0.9 | 0.96 |
| [#9420](https://github.com/omacom/omarchy/pull/9420) | Escape the values written into retro game desktop files | Adolanium | 1.9 | 1.2 | 0.95 |
| [#9563](https://github.com/omacom/omarchy/pull/9563) | fix: keep XDG desktop out of home | motodriver | 2.4 | 2.1 | 0.76 |
| [#11694](https://github.com/omacom/omarchy/pull/11694) | Keep the fcitx5 unit inert when fcitx5 isn't installed | therk | 2.2 | 0.9 | 0.94 |
| [#11842](https://github.com/omacom/omarchy/pull/11842) | Give a clear diagnosis when libfprint has no driver for the detected fingerprint | busbyjon | 2.4 | 1.3 | 0.94 |
| [#11973](https://github.com/omacom/omarchy/pull/11973) | Regenerate mise wrappers that still print mise's output on every run | jayrascodes | 1.8 | 2.0 | 0.96 |
| [#12384](https://github.com/omacom/omarchy/pull/12384) | Encode browser native-host paths as JSON | yashranaway | 2.8 | 1.8 | 0.97 |
| [#12545](https://github.com/omacom/omarchy/pull/12545) | Reject usernames that collide with system groups | paulogeyer | 2.4 | 1.9 | 0.93 |
| [#12971](https://github.com/omacom/omarchy/pull/12971) | Omit --load-extension from Google Chrome browser flags | kvnloo | 1.9 | 1.7 | 0.93 |
| [#13079](https://github.com/omacom/omarchy/pull/13079) | Remove the hey, basecamp, and cf stubs with preinstalls | yamz8 | 2.6 | 1.3 | 0.95 |
| [#13470](https://github.com/omacom/omarchy/pull/13470) | Add recursion guard to omarchy-mise-install wrappers | AnPod | 2.6 | 1.2 | 0.96 |
| [#13719](https://github.com/omacom/omarchy/pull/13719) | install-xcompose: stop blanking ~/.XCompose on refresh with empty inputs | kvnloo | 1.9 | 1.1 | 0.95 |
| [#13721](https://github.com/omacom/omarchy/pull/13721) | setup-form: reject usernames longer than 32 characters | kvnloo | 2.9 | 1.1 | 0.96 |
| [#13765](https://github.com/omacom/omarchy/pull/13765) | Write GTK bookmarks atomically instead of check-then-act | SorenHJohansen | 2.0 | 1.6 | 0.96 |

## Review candidates: docs — 6 PRs

| PR | Title | Author | Model finished | Model effort | Model fix |
|---|---|---|---|---|---|
| [#8585](https://github.com/omacom/omarchy/pull/8585) | Add the 2020 Intel MacBook Air to the T2 device list | equivalent | 2.6 | 0.8 | 0.63 |
| [#10017](https://github.com/omacom/omarchy/pull/10017) | Note that service-plugin constants need a shell restart | hudsonwa | 2.8 | 0.8 | 0.60 |
| [#10499](https://github.com/omacom/omarchy/pull/10499) | Point the plugin manual at plugins.omarchy.org | kkoontz | 2.3 | 0.4 | 0.73 |
| [#11026](https://github.com/omacom/omarchy/pull/11026) | Document that resize Super+Minus/Equal are physical AE11/AE12 | kvnloo | 2.5 | 1.0 | 0.74 |
| [#11284](https://github.com/omacom/omarchy/pull/11284) | Fix Bash learning link | hussainanjar | 2.9 | 0.4 | 0.96 |
| [#11708](https://github.com/omacom/omarchy/pull/11708) | Fix the speaker tuning service documentation link | matthewkrausse | 2.5 | 0.1 | 0.94 |

## Model-consistent candidate groups — verify fix coverage; no survivor selected

- #12074, #12090, #12680
- #12649, #12755, #13009
- #13165, #13477, #13645
- #13459, #13463, #13613
- #4928, #7700
- #5099, #11008
- #5332, #13055
- #5600, #11294
- #6019, #7945
- #6058, #10867
- #6098, #6802
- #6105, #9679
- #6587, #13137
- #6847, #13699
- #6924, #12851
- #6951, #12548
- #7040, #11612
- #7074, #12759
- #7075, #8012
- #7087, #12582
- #7102, #13637
- #7180, #7333
- #7373, #13029
- #7568, #12446
- #7783, #12658
- #7833, #11338
- #7894, #12142
- #8005, #13233
- #8429, #12957
- #8685, #11056
- #8872, #8881
- #8875, #12569
- #8884, #13568
- #8952, #13848
- #9071, #9073
- #9127, #12424
- #9189, #12423
- #9429, #13756
- #9735, #12685
- #9871, #13505
- #9885, #12425
- #9958, #13548
- #10007, #12255
- #10138, #13347
- #10231, #12956
- #10413, #13214
- #10430, #12337
- #10463, #10920
- #10476, #13186
- #10530, #12667
- #10586, #13749
- #10587, #13517
- #10610, #12048
- #10789, #13545
- #11022, #12955
- #11033, #11652
- #11069, #11470
- #11364, #12089
- #11565, #12831
- #11669, #13729
- #11751, #13648
- #11933, #12870
- #11976, #13369
- #12024, #12445
- #12150, #13670
- #12177, #13205
- #12184, #12646
- #12505, #13331
- #12585, #13204
- #12939, #13109
- #12972, #13019
- #13041, #13673
- #13044, #13094
- #13090, #13677
- #13101, #13668
- #13258, #13620
- #13314, #13651
- #13377, #13660
- #13444, #13544
- #13462, #13602
- #13466, #13543
- #13471, #13633
- #13474, #13646
- #13476, #13643
- #13478, #13641
- #13480, #13640
- #13540, #13610
- #13626, #13656

## Candidate groups needing relationship review

- #9605, #10411, #12019, #12323, #13154, #13213, #13750
  - missing_pairs: [[9605, 12019], [9605, 12323], [9605, 13154], [10411, 12019], [10411, 12323], [10411, 13154], [13154, 13213], [13154, 13750]]
- #5774, #9430, #12754
  - missing_pairs: [[5774, 12754]]
- #6485, #12352, #13219
  - missing_pairs: [[6485, 13219]]
- #6572, #8955, #13359
  - missing_pairs: [[8955, 13359]]
- #7577, #9803, #13024
  - uncertain_pairs: [{"a": 7577, "b": 9803, "verdict": "same_change", "p_same": 0.64, "classification": "uncertain"}]
- #7659, #8023, #12574
  - missing_pairs: [[7659, 12574]]
- #8065, #12635, #12651
  - missing_pairs: [[12635, 12651]]
- #10194, #11112, #13223
  - missing_pairs: [[10194, 13223]]
- #11023, #11025, #12932
  - missing_pairs: [[11023, 11025]]
- #13467, #13542, #13612
  - missing_pairs: [[13467, 13612]]

## Uncertain pairs — human comparison needed

- #9130 ↔ #13007: P(same)=0.64; verdict=same_change; uncertain
- #9490 ↔ #12800: P(same)=0.64; verdict=same_change; uncertain
- #12264 ↔ #12323: P(same)=0.64; verdict=same_change; uncertain
- #7577 ↔ #9803: P(same)=0.64; verdict=same_change; uncertain
- #7023 ↔ #12022: P(same)=0.64; verdict=same_change; uncertain
- #7765 ↔ #12635: P(same)=0.63; verdict=same_change; uncertain
- #11021 ↔ #12955: P(same)=0.62; verdict=same_change; uncertain
- #11055 ↔ #11080: P(same)=0.62; verdict=same_change; uncertain
- #10660 ↔ #10677: P(same)=0.61; verdict=same_change; uncertain
- #7345 ↔ #7737: P(same)=0.61; verdict=same_change; uncertain
- #5431 ↔ #6897: P(same)=0.6; verdict=same_change; uncertain
- #8537 ↔ #10294: P(same)=0.59; verdict=same_change; uncertain
- #6907 ↔ #13378: P(same)=0.58; verdict=same_change; uncertain
- #11381 ↔ #12686: P(same)=0.58; verdict=same_change; uncertain
- #12067 ↔ #12686: P(same)=0.56; verdict=same_change; uncertain
- #7528 ↔ #8048: P(same)=0.56; verdict=same_change; uncertain
- #8414 ↔ #12936: P(same)=0.56; verdict=same_change; uncertain
- #6834 ↔ #12679: P(same)=0.55; verdict=same_change; uncertain
- #7471 ↔ #7592: P(same)=0.55; verdict=same_change; uncertain
- #12350 ↔ #12679: P(same)=0.54; verdict=same_change; uncertain
- #11918 ↔ #12461: P(same)=0.54; verdict=same_change; uncertain
- #10232 ↔ #12956: P(same)=0.53; verdict=same_change; uncertain
- #7877 ↔ #8955: P(same)=0.53; verdict=same_change; uncertain
- #8609 ↔ #9095: P(same)=0.52; verdict=same_change; uncertain
- #5317 ↔ #8820: P(same)=0.52; verdict=same_change; uncertain
- #13444 ↔ #13616: P(same)=0.52; verdict=same_change; uncertain
- #12020 ↔ #12189: P(same)=0.51; verdict=same_change; uncertain
- #8210 ↔ #8720: P(same)=0.51; verdict=same_change; uncertain
- #6849 ↔ #11076: P(same)=0.5; verdict=same_change; uncertain
- #10198 ↔ #12683: P(same)=0.49; verdict=related_but_different; uncertain
- #8581 ↔ #10130: P(same)=0.48; verdict=related_but_different; uncertain
- #11792 ↔ #13205: P(same)=0.48; verdict=related_but_different; uncertain
- #9880 ↔ #12684: P(same)=0.47; verdict=related_but_different; uncertain
- #10989 ↔ #12955: P(same)=0.46; verdict=related_but_different; uncertain
- #5975 ↔ #12337: P(same)=0.46; verdict=related_but_different; uncertain
- #7449 ↔ #8573: P(same)=0.45; verdict=related_but_different; uncertain
- #9296 ↔ #12471: P(same)=0.44; verdict=related_but_different; uncertain
- #10330 ↔ #10824: P(same)=0.44; verdict=related_but_different; uncertain
- #7158 ↔ #8531: P(same)=0.44; verdict=related_but_different; uncertain
- #12253 ↔ #12857: P(same)=0.43; verdict=related_but_different; uncertain
- #8709 ↔ #9461: P(same)=0.43; verdict=related_but_different; uncertain
- #12248 ↔ #13568: P(same)=0.41; verdict=related_but_different; uncertain
- #7187 ↔ #13070: P(same)=0.41; verdict=related_but_different; uncertain
- #10713 ↔ #12682: P(same)=0.41; verdict=related_but_different; uncertain
- #7179 ↔ #12420: P(same)=0.41; verdict=related_but_different; uncertain
- #8169 ↔ #9465: P(same)=0.4; verdict=related_but_different; uncertain
- #5343 ↔ #7363: P(same)=0.39; verdict=related_but_different; uncertain
- #5975 ↔ #10430: P(same)=0.39; verdict=related_but_different; uncertain
- #9632 ↔ #11746: P(same)=0.38; verdict=related_but_different; uncertain
- #10845 ↔ #11121: P(same)=0.38; verdict=related_but_different; uncertain
- #9725 ↔ #13138: P(same)=0.37; verdict=related_but_different; uncertain
- #10393 ↔ #12461: P(same)=0.37; verdict=related_but_different; uncertain
- #8771 ↔ #9164: P(same)=0.37; verdict=related_but_different; uncertain
- #13240 ↔ #13241: P(same)=0.37; verdict=related_but_different; uncertain
- #13544 ↔ #13616: P(same)=0.37; verdict=related_but_different; uncertain
- #11904 ↔ #12692: P(same)=0.36; verdict=related_but_different; uncertain
- #9546 ↔ #10330: P(same)=0.36; verdict=related_but_different; uncertain
- #11477 ↔ #13768: P(same)=0.36; verdict=related_but_different; uncertain
- #10877 ↔ #12687: P(same)=0.35; verdict=related_but_different; uncertain
- #10293 ↔ #10301: P(same)=0.35; verdict=related_but_different; uncertain
- #5686 ↔ #10185: P(same)=0.35; verdict=related_but_different; uncertain
- #6892 ↔ #8573: P(same)=0.35; verdict=related_but_different; uncertain

## Escalate for risk/security review

- #4997 Add NetBird as optional VPN service
- #5035 Prevent empty passwords in omarchy-drive-set-password
- #5136 Add auto power profile switching for T2 MacBooks
- #5139 Add Orca screen reader with Piper TTS
- #5177 Add NPU support to voxtype install and migration
- #5279 Add per-network DNS configuration for WiFi
- #5284 Add NuPhy Air75 V3 keyboard support
- #5431 feat(hardware): sync ThinkBook mute LEDs with WirePlumber state
- #5545 Stop package install flows after aborts or failures
- #5562 fix(network): add default iwd config to prevent micro drops
- #5654 Add Install -> Editor -> Jetbrains menu
- #5744 feat: Add installer for official Obsidian CLI
- #5818 Add Affinity Suite installer with DPI scaling for Hyprland
- #6474 Add Android development environment
- #6513 Enable DNS-over-TLS for custom DNS providers
- #6515 Support hardware, fingerprint, and password Polkit flows
- #6532 Abort pkg-install when the package transaction fails or is interrupted
- #6557 feature(editor) add Doom Emacs installer, uninstaller, and theming integration
- #6647 Add local and remote Hermes usage sources to Agents panel
- #6664 Fix fingerprint setup script to detect non-libfprint-git providers
- #6697 Adding Atuin be default for better shell search / history
- #6719 when installing Bitwarden, ask user if it should be used as SSH agent
- #6736 Docker multi-arch build with sudo support
- #6807 Detect captive portals and offer to sign in
- #6844 Add Amp as a default coding agent
- #6847 Preserve shared boot entries through factory reset
- #6912 Fix FIDO2 setup on keys that require user verification
- #6929 Add low-power Intel rendering mode for hybrid T2 MacBooks
- #6965 Add git-based backup and restore
- #6980 Add agent security scans for untrusted software
- #7040 feat(security): Add face authentication setup and removal commands
- #7051 Add Synthetic Labs quotas to the agents panel
- #7062 Support DoT endpoints in `omarchy dns Custom`
- #7071 Migrate Brave Origin Beta profile data to stable
- #7087 Add Cursor usage collector to the agents panel
- #7158 Keep the lock screen fingerprint working across suspend, and show when the reader is unavailable
- #7169 Fix stranded session-lock recovery after plugin reload
- #7258 Restore early Thunderbolt authorization for LUKS unlock
- #7272 Switch between subscription accounts
- #7274 Add a Kimi usage collector to the agents panel
- #7417 Add NetBird mesh VPN integration
- #7435 Add Wi-Fi hotspot hosting to the network panel
- #7455 Read Fireworks credentials from pi's auth.json
- #7485 Add Firebase CLI development environment via mise
- #7501 Apply session monitor scale to the SDDM greeter
- #7537 Show limits for OpenCode's OpenAI account
- #7554 Add bb to the AI install menu
- #7566 Add Z.ai GLM Coding Plan agent usage collector
- #7598 Fix orphaned network speed test workers
- #7609 Suppress keyring "reinstalling" warning in any locale
- #7622 Add an omarchy:// link handler for installing plugins from a web page
- #7680 Add a reveal toggle to the lock screen password field
- #7731 Show Windows PCs and admin shares in Files
- #7799 Show banked rate limit resets on the Codex tab
- #7814 Add encrypted, versioned, off-site backups
- #7828 Add "Join hidden network" to the Wi-Fi panel
- #7831 Reload a wedged Wi-Fi radio without waiting for the user
- #7857 feat(surface-touch): add touchscreen support for Surface devices via linux-surface kernel as boot option
- #7871 Stop the lid gate logging a PAM failure on every open-lid sudo
- #7882 Add native Syncthing integration
- #7890 Reject Voxtype on CPUs without AVX2
- #7913 Add maker install group with ESP32/ESP-IDF toolchain setup
- #7971 Let the compositor and audio graph take the realtime priority they ask for
- #7990 Clear passwordless sudo grants at boot
- #7995 Stage diagnostics logs privately instead of at fixed /tmp paths
- #8001 Fix GitHub credential helpers after mise gh upgrades
- #8014 Keep Wi-Fi password entry stable during scans
- #8019 Eye toggle to show/hide the Wi-Fi password
- #8035 Add VPN section to the network panel
- #8051 Add Junie as a selectable default coding agent
- #8065 Add OpenCode Go usage collector for the agents panel
- #8093 Call a lapsed Claude access token paused, not signed out
- #8130 Stop NordVPN installation after setup failure
- #8169 Stop apply-system reruns leaving the install log world-writable
- #8188 Add and remove tailnets from the Tailscale panel
- #8204 Stop probing the internal T2 network interface
- #8251 Add a copy action for the revealed wifi password
- #8294 Add Wi-Fi QR code scanning
- #8315 Network panel: show External IP in connection details
- #8326 Read Claude limits with a sibling CLI's token when the saved one lapsed
- #8336 Add face authentication (howdy) to the lock screen
- #8377 Browse and install any mise tool from the menu
- #8413 Add Scanner support
- #8441 Pin Cursor password store to gnome-libsecret so GitHub login can use the OS keyring
- #8472 Omarchy v4.0.2
- #8487 Add openzoo as a coding agent option: claude code, no api key, pays per call
- #8532 Constrain the asdcontrol sudoers rule to hiddev detect/get/set
- #8534 Take privileged usernames from id -un, not USER
- #8537 Add Alfred/Raycast-style live query plugins to the menu
- #8578 Update installed themes in parallel
- #8639 Allow forgetting the connected Wi-Fi network
- #8662 Sanitize legacy Windows VM usernames
- #8704 Enable docker.service for Docker DBs
- #8707 Set Tailscale operator for Taildrop
- #8709 fix: arm signature verification for the T2 repo and close the quattro override window
- #8715 Add agent diagnostics, MCP inspection, and safe launch mode
- #8796 windows-vm: negotiate RDP with /sec:tls by default
- #8801 Add Helium and Ungoogled Chromium browser support
- #8831 Allow IGMP so multicast group queries stop flooding the firewall log
- #8889 Apply uinput permissions through tmpfiles
- #8908 Switch DNS providers without DHCP churn or profile rewrites
- #8910 Avoid redundant lock after encrypted hibernate
- #8930 Harden lock lifecycle, recovery, and keyboard wake
- #8952 Replace Gemini coding agent with Antigravity (backport of #6900)
- #8994 Isolate /var/lib/docker on a top-level Btrfs subvolume
- #9009 Document re-enabling BitLocker after dual-boot installation
- #9024 Auto-create /etc/1password/custom_allowed_browsers on install
- #9043 Authorize SSH keys into the invoking user's home
- #9044 Keep SDDM auto-login off encrypted roots in the quattro upgrade
- #9221 Add AirPlay audio output
- #9227 Require interactive confirmation for AUR installs and updates
- #9239 Sync the GNOME keyring on user password changes
- #9248 Add managed account website allowlists
- #9288 Set kernel.kptr_restrict=1 in the shipped sysctl drop-in
- #9307 Clarify that "grab key from github" in sshd setup authorizes EVERY machine that publishes public key on your github a/c
- #9319 Give the Secret portal a provider so Chromium can open its password store
- #9320 Add Oma, voice control for the desktop, as an optional service
- #9381 Show what PAM asked for in the polkit dialog
- #9398 Discover LUKS drives via lsblk, not blkid
- #9459 [codex] OM-SEC-03: Remove public Windows VM default credentials
- #9460 [codex] OM-SEC-04: Require package authenticity during Quattro
- #9461 [codex] OM-SEC-05: Remove the unsigned Apple T2 package source
- #9463 [codex] OM-SEC-08: Publish SSH only after proving key-only access
- #9464 [codex] OM-SEC-09: Generate private credentials for development databases
- #9465 [codex] OM-SEC-10: Replace the world-writable installer log
- #9470 [codex] OM-SEC-15: Keep mixed-trust installers outside sudo lifetime
- #9474 [codex] OM-SEC-19: Protect migration and SSH setup authorization
- #9475 [codex] OM-SEC-21: Authenticate only after package picker code exits
- #9477 [codex] OM-SEC-23: Keep debug collectors outside dmesg authorization
- #9500 Give visudo an editor that Omarchy actually installs
- #9506 Keep SSH setup from disabling passwords on a writable home
- #9511 Support non-interactive updates with --yes
- #9531 Wait for the Windows VM RDP service before connecting
- #9539 Add cursor theme selection to the Style menu
- #9557 Allow plugins to specify package dependencies (optional + required)
- #9571 Resolve the invoking user's home in removal cleanup scripts
- #9573 Judge the invoking user's authorized keys when removing SSH access
- #9594 Fix XDG Secret portal keyring access
- #9596 feat(mise): install default CLI tools through native lazy shims
- #9597 Add MiniMax Token Plan support
- #9605 Clear set-ID bits when securing the Windows VM mount sources
- #9692 Use DKMS for Broadcom wl across kernel updates
- #9695 Add a Setup > Region toggle with Chinese language and input method
- #9700 Seed Chromium's first-run preferences with a mode the browser can read
- #9723 Add an embedded dev-env for ESP32 and Arduino boards
- #9729 Add Setup Wizard for NVIDIA DisplayPort 1.4 EDID Fix
- #9750 Kids mode: child installs with a kid password and a parent password
- #9777 Add DeepSeek Harness to the agent roster and Install > AI
- #9783 Fix Windows VM helper rejecting setgid source directories
- #9830 Fix T2 Mac suspend: s2idle, d3cold, and brcmfmac
- #9834 Refuse to run the shell suite as root
- #9873 Defer to system-auth in the polkit stack written by fingerprint/FIDO2 setup
- #9875 Probe sudo non-interactively so unattended updates cannot hang
- #9878 Re-apply hardware pacman repos after a refresh restore
- #9894 Fix Tailscale plugin failing to reconnect when accept-routes is enabled
- #9909 Track AppImages from GitHub releases and update them daily
- #9946 Reach the forwarded SSH agent from Herdr panes
- #9965 Show Bluetooth pairing codes in the Omarchy panel
- #9995 Pin Helium password store to libsecret
- #10018 Pin Signal to gnome-libsecret like the browsers
- #10022 Do not let a migration inherit its path overrides from the caller
- #10058 Add an Ethernet toggle to the network panel
- #10065 Hibernation: keep native GPU drivers out of the initramfs so resume runs before any GPU driver touches the hardware
- #10080 Agents panel: every signed-in Claude account, and an opt-in Columns layout
- #10082 Bound lock authentication resource use
- #10088 Add omarchy-install-blesh for opt-in ble.sh autocompletion
- #10109 Add a disposable Omarchy lab VM
- #10110 Add DaVinci Resolve and DaVinci Resolve Studio installers
- #10113 fix(windows-vm): accept dockur 2777 shared mount mode on launch
- #10141 Stabilize MacBookPro13,3 hardware support
- #10172 Add Ollama Cloud usage collector to the agents panel
- #10185 Add speech-dispatcher so Brave Web Speech has voices
- #10219 security: add a disk-unlock duress password that factory-resets
- #10248 Add Update Plugin to Setup > Plugins menu
- #10257 Redact network identifiers from debug output
- #10262 Snapshot BASHPID before /proc fd walks in windows-vm mounts
- #10288 feat(network): add wired NIC DHCP/static IPv4 settings to the panel
- #10306 Install Apple Broadcom Wi-Fi firmware on every Mac brcmfmac drives, not just T2
- #10338 Fix the Windows VM refusing to start after its first launch
- #10346 Pin Electron password store to gnome-libsecret
- #10347 Add optional Ponte Android remote service commands
- #10393 Cap lock fingerprint retries; skip closed-lid fingerprint; silence sudo/polkit PAM
- #10396 Strip password keyring auth from sddm-autologin too
- #10411 Clear setgid before setting the Windows VM mount modes
- #10428 Distinguish sudo failure from missing Snapper configs
- #10435 Add VSCodium as a default editor and installer option
- #10473 network speedtest: use tokenless Cloudflare endpoints
- #10530 Map keypad digits in the polkit dialog when Qt ignores NumLock
- #10594 Add optional Agent Desktops app for background agent work
- #10602 Fix Wi-Fi password recovery after authentication failure
- #10610 Add Muse usage collector to the agents panel
- #10644 Guide an offline first login through terminal network setup
- #10655 Harden linux-modules-cleanup.service with a systemd drop-in
- #10683 Add a DeepSeek usage collector for the agents panel
- #10689 Fingerprint setup and enrolment as a shell overlay
- #10717 Report SSH service disable failures before cleanup
- #10730 Add Command Code as a coding agent choice
- #10738 Require auth to change system NetworkManager connections
- #10756 Add Ubuntu Cloud Agent environment for CLI and shell tests
- #10769 Restrict clipboard history file modes
- #10802 Keep web app and browser launches on http(s)
- #10824 Add OpenRouter usage collector to the agents panel
- #10944 Keep lock password field focused
- #10952 Start Omarchy Server edition predicates and menu
- #10962 Unattended domain join and domain logon for the Windows VM
- #10974 Rust-first sandboxed Quickshell plugins
- #10977 Add `omarchy vm`, a disposable Omarchy in QEMU/KVM
- #11017 Install missing BCM43602 board NVRAM on MacBookPro13,3
- #11032 Make Podman native with optional Docker compatibility
- #11037 Harden FIDO2 setup against cached sudo reuse
- #11067 Add Qwen Code as a default coding agent
- #11097 Keep the powerprofilesctl shebang fix applied across daemon upgrades (#11031)
- #11129 Add Kilo AI
- #11144 Add Axon as a default coding agent
- #11172 Add opt-in sudo authentication policy
- #11196 Screen time for the child profile, with two modes
- #11197 Make network speed test resilient with dynamic token fetch and Cloudflare fallback (#11166)
- #11198 Make the adapter pairable while pairing a Bluetooth device
- #11216 Integrate NetClaw into Omarchy with Light and Full setup
- #11242 Install the marketplace-verified snapshot by default in plugin add
- #11286 Configure persistent Wi-Fi Direct PC identity
- #11289 Add the headless server edition
- #11314 System security hardening
- #11322 Recreate lock screen fingerprint PAM file for pre-quattro setups
- #11367 Add MiniMax Code (mcode) to the agents panel and default agent switch
- #11379 Add TPM2-backed PIN authentication for login, sudo, polkit, and lock screen
- #11381 Install the pre-T2 FaceTime HD camera driver and firmware
- #11386 Run development containers with rootless Docker
- #11388 Sync the pacman databases before the first package install
- #11398 feat(install): accept owner/repo shorthand in plugin add and theme install
- #11423 Install OpenCode V2 through mise's npm backend
- #11428 Add ZeroTier as an installable service
- #11438 Support mounting and unlocking internal and LVM-backed storage in UDisks
- #11444 Add GitLab Duo CLI as a default coding agent
- #11461 Keep the caller's editor across sudo for vipw and vigr
- #11470 Run declared plugin cleanup before removal
- #11471 Open Steam Remote Play ports when installing Steam
- #11479 Reject root-run updates before changing user state
- #11565 Scope LocalSend firewall rules to private and local subnets (#11560)
- #11574 Add expandable hourly rain tables to the weather panel
- #11612 feat(security): Facelock face unlock for lock screen, sudo, and polkit
- #11652 Make the Intel IPU6 webcam behind an IVSC work
- #11697 Repair a broken passwordless default keyring before session apps use it
- #11720 Add eye toggle to reveal the Wi-Fi passphrase
- #11722 Add llmman to Install > AI and Remove > AI
- #11725 feat(config): configure gnome-libsecret password store for VS Code
- #11731 Add iPhone cable support via usbmuxd and gvfs-afc
- #11768 Keep the Windows VM boundary probe off the host's mounts
- #11786 Reclaim pre-4.0 user-owned Plymouth and SDDM theme directories
- #11795 Show the command being authorized at the top of the polkit prompt
- #11804 Tell agents to retry with pkexec when sudo needs a password
- #11839 feat: add commandcode, qwen audio agent, and colibri to AI installs
- #11858 Clear and swallow the lock-screen wake key so it is not typed as a password character
- #11874 Require approval for new USB and Thunderbolt devices by default
- #11907 Stop Chromium Google OAuth workaround that causes SIGTRAP crashes
- #11956 Upgrade existing Sunshine installations to the security release
- #11966 Fix captive portal sign-in URL (#11961)
- #11967 Agents: user collectors + Go connection settings card
- #11983 Show which processes asked for a polkit password
- #11984 Explain polkit commands with the default coding agent on request
- #11989 Add Google Antigravity usage collector and panel integration
- #12001 Pass Download Video extension tab cookies to yt-dlp
- #12015 Restore the input group for Voxtype evdev hotkey users
- #12019 Clear special bits when hardening Windows VM dirs
- #12055 Run the ThinkPad T14 Gen 2a (AMD) touchpad over RMI4/SMBus
- #12059 Run the default agent on another machine
- #12070 Answer ARP only from the interface that owns the address
- #12078 Import saved iwd Wi-Fi networks into NetworkManager
- #12090 Install matching kernel headers before broadcom-wl-dkms
- #12099 Harden sshd: localhost bind, key before listen
- #12103 Strip dangerous caps from gsr-kms-server and btop
- #12105 Intelligently fallback to available agent when default agent has exhausted usage
- #12109 Keep update/runtime/diagnostics out of world-writable /tmp
- #12110 Fingerprint setup: keep working forks; silent lid-open PAM gate
- #12111 Harden notification image copies, exec tokens, and hint reads
- #12114 Bar status: Steam idle-inhibit, Wi-Fi/SSID, Bluetooth alias/pairable
- #12155 Fix six reported bugs: bar toggle, hibernation, weather, VM mounts, keybindings menu, group binds
- #12159 Harden kernel and network sysctl parameters
- #12160 Disable core dump generation to prevent memory exposure
- #12161 Blacklist uncommon network protocols and legacy filesystem modules
- #12162 Harden SSH client and daemon cryptographic defaults
- #12164 Apply sudo session isolation and security flags
- #12165 Tighten system and authentication file permissions
- #12167 Add audit rules for sensitive files and privilege changes
- #12169 Configure default deny firewall rules with UFW
- #12170 Apply systemd sandboxing drop-ins for core system services
- #12176 fix(hibernate): create top-level @swap subvolume so btrfs hibernation works
- #12177 Add 80% battery charge cap toggle
- #12196 Stop speed test workers outliving a killed parent
- #12244 Chromium: overrideable OAuth env and CVE security-floor upgrade
- #12245 Lock/sleep: fail-closed, clamshell, auth UI, lid focus, logind
- #12246 Boot: ESP free space, Limine prune, /boot perms, signed upgrade, SDDM keyring
- #12260 Give third-party plugins their own entry settings and auth service
- #12264 Windows VM: create launcher after start; clear setgid on harden
- #12265 Agent usage: config-dir cache key and owner-only modes
- #12266 Security: id -un sudo grants, TUI desktop escape, Docker DB secrets
- #12279 Clear the eight-second enterprise Wi-Fi auth timeout
- #12287 Add the theme marketplace: browse, install and update community themes
- #12323 Clear setgid when hardening Windows VM directories
- #12329 Add Remove menu for coding agents
- #12394 hw: cover all Framework 16 input-module product IDs in qmk_hid udev rule
- #12459 Add an optional installer for the asciipaper live wallpaper
- #12475 network: keep passphrase prompt focused through scan reorders
- #12542 Sort passwd_tries sudoers before user overrides
- #12582 Add a Cursor collector to the agents panel
- #12583 Let the Wi-Fi passphrase be read back while typing it
- #12605 Add Devin collector to the agents panel
- #12651 feat(agents): add OpenCode Go usage with V2 support
- #12698 Add omarchy menu secret for masked secret entry
- #12715 Finish 1Password install: local polkit owners and MCP setgid
- #12717 Drive: disk parent, mmcblk/loop names, password lsblk/cancel
- #12718 Security: refresh-config path, password sync, input names, plugin USER, ldisc, first-run sudoers
- #12766 Add Bluetooth file receiving to the Bluetooth panel
- #12788 Add optional AirPods bar integration
- #12796 Fix omarchy update under sudo: unset OMARCHY_PATH and yay-as-root
- #12815 Refuse to run the tailscale and sshd setup commands as root
- #12817 Face authentication: lock screen, sudo and polkit by IR camera
- #12831 Scope the LocalSend firewall rule to private networks
- #12836 Install Hermes as the self-updating runtime in every flow
- #12883 Scope the dev-link secure_path drop-in to the linking user
- #12888 Abort Tailscale remove when sudo is cancelled
- #12889 Reuse existing enterprise Wi-Fi profiles on reconnect
- #12891 Add show/hide toggle to the Wi-Fi passphrase field
- #12895 Don't add controller users to the input group
- #12896 Persist XKBLAYOUT for LUKS so non-US layouts stay typeable
- #12897 Accept device-initiated Bluetooth Just Works pairing
- #12901 Enable Voxtype GPU backend through sudo
- #12925 Add a reveal toggle to masked TextFields, wired up for the Wi-Fi passphrase
- #12957 Keep the update transcript out of world-writable /tmp
- #12972 Add a camera bar widget that turns every USB camera off
- #13036 Add Local AI: run the model validated for your GPU and open a coding agent on it
- #13047 Pin factory-reset elevation to the packaged command
- #13052 Add a LiteLLM collector for the agents usage panel
- #13075 Add Cloudflare to Install > Service
- #13085 Restart bluetoothd and reload btusb when the adapter is wedged
- #13088 Fix network panel Forget centering, add Cancel for in-flight connects
- #13098 Default dictation to verified Cohere Vulkan, paste and Atreyu visuals
- #13101 Actually restart bluetooth.service in omarchy-restart-bluetooth
- #13106 Skip the Codex app-server probe when there are no credentials
- #13107 Fall back to Cloudflare endpoints when api.fast.com is unreachable
- #13110 Ship a managed Chromium privacy policy alongside the theme color
- #13112 Stop broadcasting hostname and permanent MAC on every network
- #13154 Strip stray special mode bits when hardening Windows VM directories
- #13183 Add password visibility toggle to lock screen
- #13187 Setup fingerprint for Validity/Synaptics readers via python-validity
- #13192 fix: enable FaceTime HD cameras on Intel Macs
- #13200 Sign in to captive portals in a dropdown instead of the browser
- #13213 Clear setgid when hardening Windows VM mount sources
- #13215 Sync root when updating the user password from the menu
- #13280 Draft: bound the hotspot to a participant limit
- #13283 Tell the user when pam_faillock has locked the account
- #13296 Install OpenClaw as a self-updating copy under ~/.openclaw
- #13312 Require a per-session token for notification click-exec
- #13316 Preserve GUM environment records during factory-reset elevation
- #13362 Converge omarchy-mac and omarchy-mx-mac into upstream Omarchy
- #13377 Refuse omarchy-update when invoked as root
- #13432 Keep a legacy Windows VM password with $$ working after the Quattro migration
- #13467 Let fingerprint setup adopt an already-enrolled print
- #13474 Soften yay go-mod caches and warn on AUR update failure
- #13479 Authorize omarchy-channel-set once for the whole switch
- #13481 Add opt-in default-browser links for web apps
- #13513 Run a lock hook when the screen locks
- #13533 Join a self-hosted Tailscale coordination server
- #13542 Finish fingerprint setup when a print is already enrolled
- #13548 Add an OpenCode agent usage collector
- #13563 Add animated installer presentation with embedded interactive controls
- #13575 Bound the package-install sudo keepalive and revoke it on exit
- #13612 Configure fingerprint PAM when prints are already enrolled
- #13616 Keep sudo alive and offer reboot after channel switch
- #13625 Do not block SDDM autologin on pam_gnome_keyring
- #13630 Prefer IPP Everywhere when adding network printers
- #13646 Soften yay go-mod caches and warn on AUR update failure
- #13652 Drop pam_faillock preauth silent so lockouts are visible
- #13660 Refuse to run omarchy-update as root
- #13664 Give each webapp its own Chromium profile
- #13690 Add region profiles, starting with China's package repositories
- #13699 Keep other systems' boot entries through a factory reset
- #13734 Add a sign-in button to the agents panel's auth card
- #13742 Test passwordless sudo revoke hook packaging
- #13745 Open the captive portal sign-in page on detection when asked to
- #13750 Clear setgid when hardening Windows VM mount sources
- #13763 Add Cloudmail to Install > Service
- #13770 Switch between several Claude and Codex subscriptions, and build apps the Omarchy way
- #13796 Keep an early polkit Enter and submit it when PAM asks
- #13800 Strip setgid and setuid bits from Windows VM mount directories (#13558)
- #13811 fix(bluetooth): recover incomplete pairing
- #13829 Resync Wi-Fi rows when a listed network's saved profile attaches
- #13836 Link Pi agent skills into PI_CODING_AGENT_DIR
- #13845 Add omp (Oh My Pi) usage collector to the agents panel
- #13848 [4.0.4/4.0.5] Replace deprecated Gemini CLI with Google Antigravity (#6900)
- #13856 Launch Claude with a real permission bypass

## Possible author follow-up — verify before requesting changes

- #3507 Support theming for multiple Chromium Profiles
- #4990 Add support for Code OSS
- #5049 feat: support tmux in terminal cwd detection
- #5055 Add imv keybind to copy current image to clipboard
- #5069 Add single instance option for webapp installs
- #5112 Add Android Studio in dev install and remove menus
- #5223 Add zsh support with aliases and shell config
- #5224 Add tmux extended-keys on for complex key bindings
- #5262 add i2c_hid modules to initramfs for laptops with I2C HID keyboards
- #5968 Install ghostty-nautilus for the 'Open in Ghostty' Nautilus extension…
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
- #7170 Add a manual reader to the Omarchy shell
- #7297 Correctly name grok and add docs link
- #7463 Fix typo on 04_navigation.md
- #7995 Stage diagnostics logs privately instead of at fixed /tmp paths
- #8421 omarchy-windows-vm: enable windows activation via system firmware by …
- #8472 Omarchy v4.0.2
- #8481 Add OpenCode agent setup: default config, AGENTS.md, and installer
- #8783 Update 44-mac-support.md to add t2linux wiki link
- #8791 fix(update): guard against missing TMPDIR and support native ChatGPT …
- #8805 Fix grammar in security documentation
- #8829 Add PTL kernel in installation script for all Intel Panther Lake systems
- #8995 Fix additional assorted typos in navigation
- #9424 Replace Em Dash with Arrow
- #9461 [codex] OM-SEC-05: Remove the unsigned Apple T2 package source
- #9492 #9489 Use correct language code for Norwegian keyboard layout
- #9557 Allow plugins to specify package dependencies (optional + required)
- #9739 Add hyfetch installer and menu entry
- #9860 Hibernation: fail when unsupported; refuse empty resume= device
- #9865 feat: cycle battery percentage placement
- #10082 Bound lock authentication resource use
- #10373 Add SpaceBeach visual time machine and desktop-history game
- #10491 [fix] Sorting packages
- #10560 Theme Sublime Text from the Omarchy palette
- #10747 Release v4.0.3
- #10893 Add @kalomarchy as code owner for protected branches
- #10934 menu: navigate with Ctrl+N/Ctrl+P like Up/Down
- #10966 Add lock screen blur settings to shell.json
- #11032 Make Podman native with optional Docker compatibility
- #11070 Add LM Studio Bionic to AI menu
- #11314 System security hardening
- #11514 Mise: no forced release-age 0; SSE4.2 agent skip; keep OpenClaw CLI
- #11580 feat(menu): improve launcher with flat search, fuzzy matching, quicklinks, and frecency
- #11945 Align spacing in xcompose emoji
- #12104 Validate omarchy-hook names on run and install
- #12114 Bar status: Steam idle-inhibit, Wi-Fi/SSID, Bluetooth alias/pairable
- #12115 Bar panel: audio/OSD/battery/weather/night light, cloned-bar Loader props
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
- #12264 Windows VM: create launcher after start; clear setgid on harden
- #12266 Security: id -un sudo grants, TUI desktop escape, Docker DB secrets
- #12267 Backlight: AIO kernel route and apple-panel-bl priority
- #12268 Terminal logos: theme-colored ascii and fitted fastfetch
- #12269 Workspace layout by name; failing Lua assertions fail the test
- #12271 Sunshine: canonical unit enable and security-floor bump
- #12465 Exit screensaver on keyboard or mouse input
- #12485 feat: sync Starship prompt with active theme
- #12486 feat: sync Herdr multiplexer with active theme
- #12507 Add interactive stepped background alignment and slideshow transition controls to image-picker
- #12679 [Intel Mac P01] Keep keyboard layout tracking on typing devices
- #12682 [Intel Mac P04] Consolidate lid handling and display classification
- #12683 [Intel Mac P05] Handle ghost internal displays
- #12684 [Intel Mac P06] Retire the legacy SPI package alongside T1Bridge
- #12686 [Intel Mac P08] Consolidate FaceTime PCIe camera support
- #12688 [Intel Mac P10] Consolidate Broadcom calibration and sleep recovery
- #12691 [Intel Mac P13] Consolidate the Intel Mac kernel migration policy
- #12717 Drive: disk parent, mmcblk/loop names, password lsblk/cancel
- #12718 Security: refresh-config path, password sync, input names, plugin USER, ldisc, first-run sudoers
- #12730 Share QR, presentation mode, multi-monitor screensaver
- #12817 Face authentication: lock screen, sudo and polkit by IR camera
- #12823 Add configurable short-term menu navigation memory
- #13003 Document Dell power recovery configuration
- #13309 Add LibreWolf as supported browser
- #13366 Fix typo in navigation section of the manual
- #13391 Prototype native shortcut picker with ranked, underlined search
- #13605 Persist monitor scale to the focused output rule
- #13608 Make Elsewhen migration bar put best-effort on shell timeouts
- #13609 Keep connected Bluetooth devices with address-like names
- #13770 Switch between several Claude and Codex subscriptions, and build apps the Omarchy way

# Suggested pre-release batches (issue #4)

Deterministic classification of the review candidates above: security first, then
low/core/danger/unknown model-risk bands, chunked into S (≤ 8), M (≤ 24), L (≤ 48) tiers ranked lowest
risk first. Cumulative: each batch contains every earlier batch of its group. These
are the source for the cumulative PRs that are the final deliverable — model-suggested,
not verified safe to merge.

## agents-ai

| Batch | Group | Tier | Size | Cumulative | Members |
|---|---|---|---|---|---|
| agents-ai-B1 | security | S | 8 | 8 | #8093 #8715 #7537 #9320 #7566 #13106 #7051 #10683 |
| agents-ai-B2 | security | M | 24 | 32 | #10824 #12105 #7799 #10172 #10756 #11722 #13845 #13734 #10610 #13548 #7455 #11144 #7087 #11067 #12582 #8051 #10080 #12329 #8487 #10730 #7554 #8065 #13052 #11367 |
| agents-ai-B3 | security | L | 28 | 60 | #11129 #8326 #11967 #13770 #9597 #6844 #7274 #12605 #7272 #11444 #12059 #11989 #9777 #6647 #8952 #13848 #11839 #12651 #11423 #11984 #13036 #10594 #13836 #12836 #13296 #13856 #6980 #12265 |
| agents-ai-B4 | low | S | 8 | 68 | #13735 #7297 #11131 #6718 #5925 #7322 #11360 #8893 |
| agents-ai-B5 | low | M | 24 | 92 | #11466 #10040 #10068 #10060 #11892 #13780 #13870 #10845 #6542 #8497 #13059 #12527 #13740 #6570 #7298 #12278 #10175 #8892 #12986 #8093 #12414 #7861 #8448 #11070 |
| agents-ai-B6 | low | L | 48 | 140 | #11121 #8450 #8715 #8862 #10067 #11109 #11124 #12483 #6478 #7225 #7547 #7686 #7924 #8345 #8479 #8755 #8958 #9208 #9546 #9697 #9885 #10606 #10633 #11188 #11267 #11896 #12803 #13198 #13209 #13458 #13553 #13621 #13837 #6860 #7537 #7725 #8602 #8977 #9320 #9869 #9900 #9956 #10675 #11488 #12032 #12352 #12939 #13109 |
| agents-ai-B7 | core | S | 8 | 148 | #12605 #7272 #7261 #13607 #11444 #12059 #11989 #9777 |
| agents-ai-B8 | core | M | 19 | 167 | #6647 #8124 #8952 #13848 #11839 #12651 #11423 #11984 #11342 #13036 #10079 #10594 #13836 #6982 #12836 #13296 #11250 #13856 #10911 |
| agents-ai-B9 | danger | S | 2 | 169 | #6980 #12265 |

## apps-integrations

| Batch | Group | Tier | Size | Cumulative | Members |
|---|---|---|---|---|---|
| apps-integrations-B1 | security | S | 8 | 8 | #13075 #11725 #12001 #5744 #10346 #13763 #5818 #8441 |
| apps-integrations-B2 | security | M | 24 | 32 | #6557 #13098 #10435 #11907 #10347 #13481 #9995 #13664 #4997 #5654 #7882 #7622 #10110 #10802 #11216 #13110 #7731 #8801 #9024 #9894 #8188 #12244 #10018 #11196 |
| apps-integrations-B3 | security | L | 5 | 37 | #12888 #11428 #7417 #9723 #12715 |
| apps-integrations-B4 | low | S | 8 | 45 | #11493 #7797 #13309 #10654 #12368 #13234 #11706 #9364 |
| apps-integrations-B5 | low | M | 24 | 69 | #7450 #10367 #12870 #7170 #9578 #5968 #11294 #13858 #5934 #9035 #13272 #6802 #9430 #10567 #6098 #8400 #7337 #13000 #13412 #5600 #5774 #9233 #12256 #12780 |
| apps-integrations-B6 | low | L | 48 | 117 | #12974 #13248 #4985 #6698 #7267 #7356 #7494 #8343 #8499 #8525 #8700 #8932 #9191 #9206 #9806 #9927 #11164 #11436 #11998 #12781 #12801 #13195 #13619 #13685 #13710 #13830 #5954 #7039 #8299 #8383 #8761 #9172 #9431 #9449 #10538 #12137 #12432 #12988 #13039 #13075 #13354 #13772 #8575 #9891 #9906 #11454 #11728 #11955 |
| apps-integrations-B7 | core | S | 8 | 125 | #12139 #9995 #11571 #6454 #5553 #7715 #12089 #12834 |
| apps-integrations-B8 | core | M | 24 | 149 | #10370 #13664 #4997 #11364 #9011 #9124 #11978 #5654 #9037 #12754 #7882 #13262 #10573 #7622 #13588 #10110 #7444 #10802 #12148 #11216 #13110 #10446 #11053 #7731 |
| apps-integrations-B9 | core | L | 5 | 154 | #10884 #8801 #9024 #9894 #8188 |
| apps-integrations-B10 | danger | S | 8 | 162 | #12244 #7817 #10018 #11196 #12888 #11428 #7417 #9723 |
| apps-integrations-B11 | danger | M | 1 | 163 | #12715 |

## desktop-config

| Batch | Group | Tier | Size | Cumulative | Members |
|---|---|---|---|---|---|
| desktop-config-B1 | security | S | 8 | 8 | #12925 #7680 #8019 #12891 #9594 #8315 #12459 #13183 |
| desktop-config-B2 | security | M | 23 | 31 | #8578 #11858 #10944 #12287 #9319 #8537 #13200 #11574 #9539 #6515 #13625 #12111 #10058 #12015 #10288 #8035 #13312 #12155 #11786 #7501 #12972 #8336 #12245 |
| desktop-config-B3 | low | S | 8 | 39 | #9691 #12488 #12783 #10560 #6696 #13267 #7240 #8437 |
| desktop-config-B4 | low | M | 24 | 63 | #12694 #7302 #9313 #10571 #12091 #10517 #8846 #13497 #10470 #12826 #7219 #9223 #10341 #11906 #13065 #13603 #8569 #13232 #13190 #11491 #7296 #8830 #13133 #7560 |
| desktop-config-B5 | low | L | 48 | 111 | #8857 #10540 #8654 #13126 #13580 #12431 #12794 #13565 #13810 #9345 #10867 #8214 #9986 #10776 #6467 #8907 #10751 #13613 #7836 #6920 #7075 #9492 #8980 #13255 #7653 #8815 #9000 #9690 #11042 #12486 #4990 #8407 #10115 #13191 #13641 #7088 #9535 #12255 #13653 #10697 #12795 #7490 #9742 #10345 #12613 #13120 #13461 #13463 |
| desktop-config-B6 | core | S | 8 | 119 | #11827 #9520 #11545 #9919 #13460 #5282 #9312 #10713 |
| desktop-config-B7 | core | M | 24 | 143 | #12051 #9523 #7651 #11574 #13490 #13313 #7992 #8811 #13359 #9493 #13480 #6403 #8025 #9539 #12277 #6515 #9436 #9170 #12913 #6865 #10722 #7945 #4593 #11420 |
| desktop-config-B8 | core | L | 18 | 161 | #7193 #12956 #6019 #13625 #10027 #10719 #8733 #12616 #10663 #7486 #10653 #8087 #9632 #12111 #10015 #10058 #12015 #11912 |
| desktop-config-B9 | danger | S | 8 | 169 | #10288 #8035 #11746 #13312 #12155 #11786 #7501 #12972 |
| desktop-config-B10 | danger | M | 3 | 172 | #8336 #7169 #12245 |

## docs

| Batch | Group | Tier | Size | Cumulative | Members |
|---|---|---|---|---|---|
| docs-B1 | security | S | 2 | 2 | #9009 #11804 |
| docs-B2 | low | S | 8 | 10 | #7063 #7463 #7631 #7654 #7787 #7792 #8005 #8006 |
| docs-B3 | low | M | 24 | 34 | #8287 #8609 #8699 #8783 #8805 #8974 #9062 #9722 #9867 #9993 #10017 #10167 #10499 #10580 #10708 #10783 #10866 #10942 #11045 #11290 #11677 #12006 #12284 #12390 |
| docs-B4 | low | L | 36 | 70 | #12543 #12577 #13228 #13233 #13366 #13389 #13472 #13723 #7318 #7601 #8585 #9009 #11087 #11179 #11464 #13817 #7095 #9095 #7931 #11026 #11296 #13056 #11803 #8064 #13003 #11804 #11284 #7428 #10123 #11530 #13717 #9486 #10237 #6959 #11708 #7690 |

## fix-misc

| Batch | Group | Tier | Size | Cumulative | Members |
|---|---|---|---|---|---|
| fix-misc-B1 | security | S | 8 | 8 | #11795 #9398 #13088 #9531 #13796 #7598 #10530 #12196 |
| fix-misc-B2 | security | M | 24 | 32 | #10428 #13742 #9834 #13513 #12260 #8662 #6965 #11983 #10262 #10257 #13047 #10411 #11768 #8910 #5545 #7062 #13213 #10769 #12070 #10338 #7995 #10113 #11470 #13800 |
| fix-misc-B3 | security | L | 37 | 69 | #13283 #9500 #13154 #13750 #12019 #10717 #12109 #9571 #12883 #13112 #9605 #12323 #9288 #10738 #9475 #6736 #9783 #12160 #10393 #12542 #13652 #8908 #11461 #12159 #11438 #12103 #12717 #9477 #10655 #10082 #12170 #9573 #12165 #12162 #8930 #11314 #10219 |
| fix-misc-B4 | low | S | 8 | 77 | #12344 #8741 #10557 #8165 #9973 #11022 #7661 #13766 |
| fix-misc-B5 | low | M | 24 | 101 | #12867 #7216 #8787 #12809 #7332 #10510 #7402 #11483 #10181 #11795 #9903 #10632 #13574 #13842 #11010 #8653 #11579 #13681 #12452 #12575 #11606 #7491 #11747 #6725 |
| fix-misc-B6 | low | L | 48 | 149 | #8959 #11287 #13212 #13557 #8016 #8269 #8640 #9514 #10007 #13096 #10457 #11057 #11156 #11667 #12828 #12943 #13305 #13469 #13561 #7074 #7406 #8765 #10070 #11577 #11847 #11963 #12866 #13824 #7517 #8076 #8570 #8664 #8828 #9006 #9426 #10228 #10476 #11421 #11568 #11730 #11860 #12098 #12223 #12776 #12966 #13043 #13390 #13751 |
| fix-misc-B7 | core | S | 8 | 157 | #9807 #13651 #12260 #12937 #12023 #13819 #8662 #9847 |
| fix-misc-B8 | core | M | 24 | 181 | #7155 #9033 #8644 #9001 #12071 #13282 #10497 #10083 #6965 #6906 #9429 #11983 #10235 #8531 #10262 #11554 #6813 #10257 #13047 #10236 #12291 #9575 #12220 #6494 |
| fix-misc-B9 | core | L | 16 | 197 | #7673 #11069 #12106 #8793 #11273 #10411 #11768 #12461 #8910 #5241 #5545 #7062 #13213 #10769 #7572 #12070 |
| fix-misc-B10 | danger | S | 8 | 205 | #10338 #7995 #10113 #11470 #13800 #12046 #11920 #5761 |
| fix-misc-B11 | danger | M | 24 | 229 | #13283 #9500 #13154 #13750 #11476 #13055 #12019 #10717 #12109 #9571 #8199 #12883 #13112 #11948 #9605 #12323 #9288 #11759 #10738 #9475 #6736 #9783 #12160 #13311 |
| fix-misc-B12 | danger | L | 19 | 248 | #10393 #12542 #13652 #8908 #11461 #12159 #11438 #12103 #12717 #9477 #10655 #10082 #12170 #9573 #12165 #12162 #8930 #11314 #10219 |

## hardware-drivers

| Batch | Group | Tier | Size | Cumulative | Members |
|---|---|---|---|---|---|
| hardware-drivers-B1 | security | S | 8 | 8 | #8251 #11720 #13829 #11197 #12583 #13745 #8014 #11286 |
| hardware-drivers-B2 | security | M | 24 | 32 | #11198 #10602 #12475 #13101 #8639 #7828 #13811 #9878 #12114 #11731 #8413 #11097 #5279 #12279 #12766 #5136 #8294 #11966 #12394 #12788 #6807 #13085 #5562 #9965 |
| hardware-drivers-B3 | security | L | 18 | 50 | #13280 #8204 #5431 #12897 #7435 #9729 #7857 #12161 #9221 #12177 #5284 #11017 #12889 #11381 #7831 #8532 #11874 #7258 |
| hardware-drivers-B4 | low | S | 8 | 58 | #8330 #11228 #12200 #9763 #13761 #9553 #6829 #7308 |
| hardware-drivers-B5 | low | M | 24 | 82 | #10377 #13245 #13009 #10196 #13759 #13775 #7037 #8663 #12231 #13016 #5716 #7373 #7915 #8096 #9063 #9218 #9348 #9435 #9495 #10191 #11001 #12024 #12445 #12484 |
| hardware-drivers-B6 | low | L | 48 | 130 | #12568 #12755 #13292 #7475 #7745 #8284 #8317 #8713 #8871 #9400 #9612 #9755 #9883 #10071 #11785 #11837 #12649 #12960 #13029 #5317 #7186 #7812 #7948 #8251 #8737 #10844 #11720 #12489 #12842 #6548 #7336 #9160 #10076 #10222 #10364 #10392 #12552 #12634 #13111 #13405 #13711 #13715 #13744 #7681 #7837 #8712 #9132 #9997 |
| hardware-drivers-B7 | core | S | 8 | 138 | #8875 #8929 #10926 #12367 #13861 #8014 #9409 #11592 |
| hardware-drivers-B8 | core | M | 24 | 162 | #5020 #11286 #8476 #11198 #7951 #11387 #10602 #12683 #7177 #13076 #9230 #5130 #5193 #7329 #12185 #12475 #7353 #8221 #13260 #12692 #11315 #13668 #5445 #7965 |
| hardware-drivers-B9 | core | L | 48 | 210 | #13540 #12691 #9850 #12216 #11880 #12420 #13284 #10320 #12590 #12210 #10313 #11840 #12977 #13834 #8750 #11624 #13101 #13667 #13005 #13671 #13115 #6149 #11432 #13539 #9860 #13610 #8371 #12682 #6928 #10592 #12636 #7594 #8639 #9105 #10920 #12936 #12125 #13728 #11831 #11870 #13778 #11033 #12569 #13148 #7828 #13811 #8464 #11843 |
| hardware-drivers-B10 | danger | S | 8 | 218 | #11966 #13082 #11072 #12394 #5335 #11911 #12788 #13615 |
| hardware-drivers-B11 | danger | M | 24 | 242 | #6807 #12286 #8295 #9202 #9210 #8421 #12685 #9276 #13085 #5430 #9899 #11616 #8151 #9815 #5562 #13238 #13663 #9816 #5194 #8546 #10184 #10936 #13298 #9965 |
| hardware-drivers-B12 | danger | L | 48 | 290 | #10139 #11570 #13024 #7644 #7993 #11548 #5951 #12076 #7004 #12680 #13280 #10332 #11536 #12687 #8187 #12267 #8204 #13623 #12007 #5431 #7343 #13129 #5262 #12897 #5140 #11076 #7577 #7671 #12074 #6596 #7435 #9729 #13820 #7950 #8090 #12003 #13532 #9803 #7180 #8812 #10910 #7857 #10758 #12161 #12314 #12968 #7333 #9221 |

## install-setup

| Batch | Group | Tier | Size | Cumulative | Members |
|---|---|---|---|---|---|
| install-setup-B1 | security | S | 8 | 8 | #8377 #10248 #7485 #10952 #6532 #6719 #7890 #10644 |
| install-setup-B2 | security | M | 24 | 32 | #12815 #9381 #9557 #13563 #10109 #13630 #11289 #5035 #8704 #11388 #9695 #8130 #5139 #13690 #10185 #6664 #5177 #10977 #9307 #13215 #6513 #10962 #12901 #7871 |
| install-setup-B3 | security | L | 48 | 80 | #12167 #13612 #13533 #13542 #11322 #6474 #7158 #12896 #10396 #13316 #13467 #12831 #7040 #8169 #9506 #7990 #9043 #11697 #12895 #7971 #11471 #13187 #8831 #11032 #7913 #9873 #9700 #8709 #9750 #10689 #9470 #11565 #12110 #6912 #8534 #12169 #11172 #11037 #9248 #11386 #11612 #9465 #12718 #9461 #11379 #12817 #9459 #9463 |
| install-setup-B4 | low | S | 8 | 88 | #7161 #7740 #9192 #9163 #10147 #5112 #7763 #13013 |
| install-setup-B5 | low | M | 24 | 112 | #11691 #6777 #13028 #12965 #11025 #10805 #8377 #11000 #11047 #12581 #10248 #7485 #8117 #8631 #9739 #12415 #12521 #7729 #12752 #12890 #11694 #11842 #7473 #13585 |
| install-setup-B6 | low | L | 48 | 160 | #13470 #5031 #9741 #9273 #9432 #13719 #8486 #5999 #9680 #11973 #9175 #13079 #13441 #10353 #10828 #13765 #9634 #10582 #6932 #10823 #12480 #9420 #10952 #12701 #6532 #6719 #7890 #12695 #5343 #9626 #10472 #10548 #11435 #13547 #8116 #13721 #12384 #12971 #11719 #8091 #10599 #11125 #11288 #10644 #12312 #6967 #12104 #12633 |
| install-setup-B7 | core | S | 8 | 168 | #11953 #13071 #12037 #12358 #7667 #12004 #12505 #8682 |
| install-setup-B8 | core | M | 24 | 192 | #11484 #12056 #9244 #8186 #11056 #13331 #11259 #12723 #9358 #9381 #12598 #8670 #10949 #12932 #7583 #9150 #12923 #8442 #9282 #9557 #9633 #5148 #8430 #13563 |
| install-setup-B9 | core | L | 39 | 231 | #9299 #12816 #10109 #13630 #5686 #10707 #11289 #13644 #5035 #8704 #13243 #10293 #11388 #13508 #6730 #9695 #11418 #8130 #8133 #5139 #11538 #6753 #13705 #5890 #11523 #11477 #13690 #8316 #11481 #9228 #10185 #13768 #6664 #5177 #6553 #10977 #12271 #9307 #9686 |
| install-setup-B10 | danger | S | 8 | 239 | #13215 #6513 #10962 #12901 #8829 #7871 #12167 #13612 |
| install-setup-B11 | danger | M | 24 | 263 | #13533 #13542 #5938 #11322 #6474 #7158 #11401 #12896 #10396 #13316 #13467 #12833 #12831 #7040 #8169 #8756 #9506 #7990 #9043 #11697 #12895 #7971 #9454 #11471 |
| install-setup-B12 | danger | L | 32 | 295 | #13187 #8831 #11032 #7913 #9873 #9700 #8709 #9750 #10689 #9470 #11565 #12110 #6912 #8534 #12169 #11172 #11037 #9248 #11386 #11612 #12176 #9465 #12718 #9461 #11379 #12817 #9459 #8994 #9463 #12099 #9464 #13362 |

## shell-cli

| Batch | Group | Tier | Size | Cumulative | Members |
|---|---|---|---|---|---|
| shell-cli-B1 | security | S | 8 | 8 | #12698 #10473 #8796 #8001 #10088 #13107 #11398 #11242 |
| shell-cli-B2 | security | M | 7 | 15 | #9227 #6697 #7814 #9596 #9946 #13575 #12164 |
| shell-cli-B3 | low | S | 8 | 23 | #12268 #11853 #13720 #12653 #7365 #11670 #13237 #7796 |
| shell-cli-B4 | low | M | 24 | 47 | #12485 #10847 #5564 #4936 #6481 #11962 #10180 #11150 #5195 #10667 #11120 #11872 #9022 #10259 #11098 #11371 #11468 #12837 #7541 #12081 #5224 #6042 #6078 #6839 |
| shell-cli-B5 | low | L | 48 | 95 | #7338 #7370 #8034 #8466 #8556 #8630 #8880 #9014 #9039 #9040 #9126 #9487 #9977 #10536 #11205 #12135 #12138 #12171 #12363 #12364 #12600 #12644 #12670 #12841 #13018 #13197 #13386 #13568 #13674 #13678 #13706 #13712 #13724 #13801 #5049 #7434 #8033 #8084 #8179 #8406 #9038 #11210 #11482 #12063 #12283 #12416 #12465 #12698 |
| shell-cli-B6 | core | S | 7 | 102 | #6697 #9503 #11240 #12872 #7814 #9596 #9946 |
| shell-cli-B7 | danger | S | 2 | 104 | #13575 #12164 |

## unclear

| Batch | Group | Tier | Size | Cumulative | Members |
|---|---|---|---|---|---|
| unclear-B1 | security | S | 3 | 3 | #10974 #12264 #12266 |
| unclear-B2 | low | S | 8 | 11 | #8995 #11945 #9424 #10491 #10893 #10511 #8522 #6930 |
| unclear-B3 | low | M | 8 | 19 | #7372 #10919 #11661 #12269 #6966 #10558 #4962 #13217 |
| unclear-B4 | danger | S | 3 | 22 | #10974 #12264 #12266 |

## update-release

| Batch | Group | Tier | Size | Cumulative | Members |
|---|---|---|---|---|---|
| update-release-B1 | security | S | 8 | 8 | #11479 #13660 #9909 #13377 #12796 #7609 #9044 #9511 |
| update-release-B2 | security | M | 20 | 28 | #13699 #13432 #11956 #10022 #13646 #7071 #9875 #13616 #12957 #13474 #8707 #9239 #13479 #8889 #12078 #8472 #9460 #9474 #6847 #12246 |
| update-release-B3 | low | S | 8 | 36 | #10747 #9893 #13365 #7398 #10326 #5902 #10066 #13061 |
| update-release-B4 | low | M | 24 | 60 | #13626 #11217 #12835 #9343 #12094 #13656 #13799 #11023 #11480 #13538 #7136 #13556 #8708 #12421 #12797 #6907 #8042 #10308 #13468 #13500 #11692 #12503 #8399 #12359 |
| update-release-B5 | low | L | 30 | 90 | #12174 #10398 #10742 #7130 #8163 #9286 #11151 #7400 #10865 #12860 #10232 #12920 #13617 #9703 #10205 #12778 #6872 #8081 #11558 #13444 #8493 #8992 #6884 #6972 #9568 #6767 #10183 #10524 #8724 #9423 |
| update-release-B6 | core | S | 8 | 98 | #7256 #8771 #7474 #11479 #12101 #12419 #12905 #13371 |
| update-release-B7 | core | M | 24 | 122 | #8590 #8854 #13660 #10878 #13352 #13608 #12250 #12722 #12532 #12535 #12906 #10710 #8824 #5866 #13781 #7998 #8791 #13544 #9139 #9909 #7396 #12871 #13377 #12796 |
| update-release-B8 | core | L | 33 | 155 | #13602 #10711 #7609 #10812 #8781 #11207 #10301 #11805 #12328 #13426 #12548 #13584 #9044 #11478 #6951 #10886 #13601 #13526 #13462 #10165 #12186 #9511 #11528 #11222 #10166 #13699 #13432 #9472 #11956 #6840 #10022 #13397 #13646 |
| update-release-B9 | danger | S | 8 | 163 | #5332 #6758 #7071 #8429 #9875 #13616 #9070 #12957 |
| update-release-B10 | danger | M | 18 | 181 | #13474 #8707 #9071 #9239 #12909 #7223 #9285 #9073 #7410 #8175 #13479 #8889 #12078 #8472 #9460 #9474 #6847 #12246 |
