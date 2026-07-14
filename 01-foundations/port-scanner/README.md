# Port Scanner

A threaded TCP port scanner with service identification.

## What it does
Scans a target host across a range of TCP ports, reports which are open, and
identifies the well-known service likely running on each.

## Usage
```bash
python scanner.py 127.0.0.1 -p 1-1024
python scanner.py 127.0.0.1 -p 22 -t 1.0 -w 200
```

| Flag | Description | Default |
|------|-------------|---------|
| `host` | Target host (positional) | required |
| `-p, --ports` | Port or range (`80` or `1-1024`) | `1-1024` |
| `-w, --workers` | Concurrent worker threads | `100` |
| `-t, --timeout` | Timeout per port, seconds | `0.5` |

## How it works
A TCP port scan is an attempt at the **three-way handshake**. The scanner sends
a SYN; an open port replies SYN-ACK, a closed port replies RST, and a firewalled
port replies with nothing at all. `socket.connect_ex()` performs this handshake
and returns `0` on success, which is how "open" is detected.

The silent case is what makes naive scanners unusable: with no reply, the socket
waits out the OS default timeout, which can be minutes per port. Setting an
explicit `settimeout()` bounds that wait.

Because the work is **I/O-bound** — the CPU is idle while waiting on the network —
a `ThreadPoolExecutor` overlaps those waits across many ports at once. Python
releases the GIL during blocking I/O, so threading is the correct tool here
(as opposed to `multiprocessing`, which would suit a CPU-bound workload).
Scanning 30 firewalled ports drops from ~30s to ~1s.

## Why it matters
Port scanning is the first step of any security assessment: you cannot secure a
service you don't know is exposed. Building the scanner rather than running
`nmap` means understanding *why* a filtered port behaves differently from a
closed one — which is the knowledge that makes scan output actionable.

## Ethics
Scan only hosts you own or have written authorization to test.
