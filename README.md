# SafeDays Labs

A growing toolkit of small, focused security utilities I build to learn offensive
and defensive fundamentals from the ground up. Each tool lives in its own folder
with a README explaining **what it does, how it works, and why it matters**.

> ⚠️ **For education and authorized testing only.** Only run these tools against
> systems you own or have explicit written permission to test.

## Tools

| Tool | What it does | Status |
|------|--------------|:------:|
| [port-scanner](./port-scanner) | Threaded TCP port scanner with service detection | ✅ |
| dns-lookup | Resolve A / AAAA / MX / TXT records | 🔜 |
| encoder-decoder | Base64 / hex transforms | 🔜 |
| hash-toolkit | MD5 / SHA hashing + dictionary lookup | 🔜 |

## Stack
Python 3 — standard library first; any third-party dependencies are noted per-tool
in `requirements.txt`.

## About
Built by Jose Diaz as part of the [SafeDays Security](https://safedayssecurity.com)
learning path.
