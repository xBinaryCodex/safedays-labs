# SafeDays Security — Portfolio Build Roadmap

**Goal:** turn 100 scattered project ideas into a sequenced curriculum that (1) builds skill in order, (2) produces a visible GitHub portfolio, and (3) doubles as SafeDays marketing + L3 brag-doc material.

**The rule for every project:** it is not "done" until there's a repo with a README covering **what it does · how it works · why it matters**, plus a screenshot or short demo GIF. If a client or hiring manager can't see it, it didn't happen.

**Ethics boundary:** offensive tools (Phase 4 and the parking lot) run *only* against systems you own — your EVE-NG lab, a local DVWA/Juice Shop box, your own machines. Never a system you don't control.

Track: `[ ]` not started · `[~]` in progress · `[x]` done + repo pushed

---

## Phase 1 — Foundations & recon
*Learn to speak the machine's language in Python. Every later phase reuses these primitives. Ship your first repos.*

- [ ] **Port scanner** (list #1) — raw sockets + the TCP handshake. Teaches how services expose themselves on a network.
- [ ] **DNS lookup tool** (#4) — a resolver that queries A / AAAA / MX / TXT. Teaches how names become addresses.
- [ ] **Base64 / hex encoder-decoder** (#16) — teaches the critical distinction: *encoding is not encryption*.
- [ ] **Caesar cipher CLI** (#3) — first taste of crypto (substitution). Sets up Phase 3.
- [ ] **Hash toolkit** (#8) — MD5/SHA hashing, then a dictionary lookup. Teaches hashing vs encryption, and why salting matters.
- [ ] **Password strength analyzer** (#75) — entropy math + attack-time estimation. Turns "use a strong password" into a number.

**Phase outcome:** fluent in Python sockets + core protocols; 3–6 small, clean, pinned repos. Momentum.

---

## Phase 2 — Network defense & monitoring
*Point those primitives at your own network. This is your home turf — move fast. These are genuinely sellable to a law firm.*

- [ ] **Packet sniffer / traffic analyzer** (#7, #81 — same tool) — `scapy` to read packets off the wire. The eyes for everything below.
- [ ] **ARP spoofing detector** (#18) — watches for MAC/IP table poisoning. Classic man-in-the-middle defense.
- [ ] **DNS spoofing detector** (#86) — flags forged DNS responses. Pairs with your Phase 1 resolver.
- [ ] **Firewall log parser + reporter** (#17) — parse noisy logs into a readable report. The gateway skill to SIEM later.
- [ ] **File integrity monitor** (#11) — hash a directory, alert on changes. *This is your hashing from Phase 1, applied.* Real product.
- [ ] **SSH brute-force detector + auto-ban** (#14) — parse auth logs, ban repeat offenders. You're rebuilding fail2ban and learning why it works.
- [ ] **Network baseline monitor** (#42) — learn "normal," alert on deviation. First real anomaly detection.

**Phase outcome:** a small blue-team detection suite. This is the core of a SafeDays "monitoring" service offering.

---

## Phase 3 — Crypto & secure systems
*Turn "detect" into "protect." Applied cryptography = the SafeDays confidentiality pitch for law firms.*

- [ ] **File encryption tool** (#80, #99 — same idea) — AES symmetric encryption of files. The foundation.
- [ ] **Secure file sharing** (#63, "0xCipherLink") — AES-256 transfer + key exchange. Teaches the hard part: getting the key to the other side safely.
- [ ] **2FA / OTP system** (#78) — TOTP, shared secrets, the math behind the 6-digit code. Demystifies MFA.
- [ ] **Digital signature verification** (#98) — asymmetric keys for integrity + authenticity. The "is this document real?" tool — very relevant to legal clients.
- [ ] **Steganography tool** (#9) — hide data in image LSBs. Fun, and teaches you what data exfiltration hiding looks like (so you can detect it).
- [ ] **Password manager** (#61) — encrypted vault. Capstone that ties this whole phase together.

**Phase outcome:** applied cryptography you can explain plainly to a non-technical client. Strong SafeDays differentiator.

---

## Phase 4 — Offensive fundamentals (LAB ONLY, eJPT-aligned)
*You can't defend what you don't understand. Everything here runs against your own EVE-NG lab or a local vulnerable app (DVWA / OWASP Juice Shop). Maps directly to eJPT prep.*

- [ ] **Vulnerability scanner** (#5) — compare detected software versions against a CVE feed. The core of every commercial scanner.
- [ ] **Web vuln scanner** (#25) — crawl your *own* test app and probe for XSS / SQLi. Teaches how these attacks actually work.
- [ ] **OSINT recon framework** (#36, #65 — same family) — aggregate public footprint data. Reconnaissance is step one of any assessment.
- [ ] **Brute-force login tester** (#64) — against your *own* lab web app. Demonstrates why rate limiting + lockouts matter.
- [ ] **WiFi scanner (monitor mode)** (#15) — passively list SSIDs + encryption types. Read-only; ties to your Aironet/ME experience.

**Phase outcome:** attacker's-eye view + eJPT-relevant hands-on. You now understand the threats your Phase 2/3 tools defend against.

---

## Phase 5 — Security platforms (the résumé centerpieces)
*Compose the scripts into full platforms. "I built a working SIEM" is a door-opener sentence.*

- [ ] **Honeypot** (#71) — a decoy that detects + logs attacker behavior. Uses your Phase 2 sniffing skills.
- [ ] **Intrusion detection system** (#33 rule-based → #72 ML-based) — start with Snort-style signatures, then add ML. Two versions = a growth story.
- [ ] **SIEM dashboard + log correlation** (#22, #23, #77 — collapse into one build) — aggregate logs, correlate events, visualize. The centerpiece. Your firewall parser (#17) feeds this.
- [ ] **Threat intelligence aggregator** (#23) — pull IOCs from public APIs to enrich the SIEM.
- [ ] **Security news dashboard** (#12) — scrape + store security news. Small, but a nice always-on demo and a reason to visit your site.

**Phase outcome:** 2–3 impressive, pinnable platforms. These anchor both the SafeDays site and the L3 conversation.

---

## Phase 6 — Cloud & advanced
*Connect everything to your WGU cloud degree + AWS cert. Most local consultants can't do this — it's your edge.*

- [ ] **Cloud asset inventory** (#35) — enumerate AWS/Azure/GCP resources. Know what exists before securing it.
- [ ] **Cloud misconfiguration scanner / CSPM** (#90, #48 — same tool) — check for insecure configs against compliance baselines. Directly billable.
- [ ] **Container / Docker security scanner** (#28, #43 — CIS checks) — audit images and configs. Relevant to your Proxmox/homelab world.
- [ ] **Software supply chain analyzer** (#60) — detect typosquatted / compromised dependencies. Modern, high-signal skill.
- [ ] **Web application firewall** (#40, #62) — reverse-proxy filtering. Ties Phase 4 (attacks) back to Phase 2/3 (defense) — a fitting capstone.

**Phase outcome:** cloud + modern-stack security credibility that pairs with your degree and AWS cert.

---

## Parking lot — advanced / do-later / skip
Valuable understanding, but low portfolio ROI for a *defensive* consultancy, and strictly lab-only:
- Exploit development framework (#45), zero-day fuzzer (#51), APT simulation (#56), reverse shell handler (#21), kernel rootkit work (#53). Deep red-team / research. Revisit after eJPT if you want OSCP-track depth.
- **CAPTCHA (#91):** reframe as studying *why CAPTCHAs fail* (defensive analysis), not building a bypass.
- **Keylogger (#2):** only ever on machines you own, clearly labeled educational.

## Redundancies I collapsed (so you don't build the same thing 3×)
- SIEM: #22 = #23 = #77 → one platform
- WiFi deauth detector: #30 = #92 · DDoS detection: #27 = #96 · Ransomware: #20 = #74
- Rootkit detection: #53 = #89 · Cloud misconfig: #35 / #48 / #90 · Password cracker: #8 + #52
- WAF: #40 = #62 · Phishing detection: #13 / #73 / #97 · Secure chat: #26 = #88
- File encryption: #63 / #80 / #99 · IDS: #33 + #72 · 2FA: #78 / #84

---

## The "make it visible" playbook (run this on every project)
1. **One repo per project**, or a `safedays-labs` monorepo with a folder each. Consistent naming.
2. **README = what / how / why** + a screenshot or 10-second GIF. This is the deliverable, not the code.
3. **Pin the 4–5 best** on your GitHub profile (SIEM, honeypot, IDS, file-integrity monitor, CSPM scanner).
4. **One post per phase** on LinkedIn / the SafeDays blog: "Built X — here's what it taught me." Markets the business.
5. **Log each into the brag doc** the day you finish it — fuel for July 20 and beyond.
6. **Cert alignment:** Phases 1–3 reinforce Security+/Network+; Phase 4 is eJPT prep; Phases 5–6 map to CCNP/cloud goals.

## Suggested cadence
One project at a time, learn-as-you-go, full depth. Realistic pace ~1 project/week around work + family + WGU. That finishes Phase 1 in ~6 weeks and gives you shippable, visible proof of competency well before the L3 conversation compounds.
