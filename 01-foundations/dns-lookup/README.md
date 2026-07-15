# DNS Lookup & Email-Security Recon

A DNS reconnaissance tool that profiles a domain's infrastructure and checks its
email-security posture.

## What it does
Given a domain, it retrieves the key DNS record types (A, AAAA, MX, TXT, NS) to
reveal where the domain is hosted, who handles its email, and which DNS
providers it uses. With `--email`, it additionally reports whether the domain
publishes SPF and DMARC records — the two records that defend against email
spoofing.

## Usage
```bash
python dnslookup.py github.com
python dnslookup.py github.com --email
```

| Argument | Description |
|----------|-------------|
| `domain` | Domain to look up (positional, required) |
| `--email` | Also run the SPF/DMARC email-security check |

Requires `dnspython` (see repo-root `requirements.txt`):
```bash
pip install -r requirements.txt
```

## How it works
The Python standard library can resolve a name to an IP (an A record) but cannot
request other record types. This tool uses **dnspython** (`dns.resolver`) to
query specific types directly.

Each lookup distinguishes the three ways DNS can respond: records found, the
domain exists but has no record of that type (`NoAnswer`), or the domain does
not exist at all (`NXDOMAIN`) — handled separately so results are never
misleading.

The email check reads two things: **SPF** (a TXT record beginning `v=spf1`) and
**DMARC** (a TXT record at the special `_dmarc.<domain>` name). Their presence or
absence indicates how well the domain is protected against being impersonated in
phishing.

## Why it matters
Unlike port scanning, DNS lookups query **public records**, so this is *passive*
reconnaissance — no authorization required. It profiles a target's hosting, mail
provider, and email-security posture without ever contacting the target's own
systems. The SPF/DMARC check maps directly to a real-world finding: a domain
missing these records can be spoofed in phishing attacks against its own users.

## Known limitations
- SPF detection is basic — it matches on `v=spf1` in the domain's TXT records and
  won't catch every provider's SPF structure. A future version should parse SPF
  includes more thoroughly.