# Port Scanner

A fast, threaded TCP port scanner built from raw Python sockets.

## What it does
Checks a target host for open TCP ports and labels each with its likely service
(e.g. 22 → ssh, 80 → http).

## How it works
- **Socket + handshake:** uses Python's `socket` library to attempt a TCP
  three-way handshake on each port via `connect_ex`, which returns `0` when the
  port is open.
- **Timeouts:** sets a short per-port timeout so *filtered* ports (firewall
  silently dropping the SYN) don't hang the scan.
- **Concurrency:** uses `ThreadPoolExecutor` to scan many ports at once. Scanning
  is I/O-bound — most time is spent *waiting* on the network — so threads overlap
  all that waiting for a large speedup (Python releases the GIL during socket I/O).
- **Service names:** maps open ports to service names via the OS services database.

## Usage
```bash
python scanner.py 127.0.0.1                 # scan ports 1-1024 (default)
python scanner.py 127.0.0.1 -p 80           # single port
python scanner.py 192.168.1.10 -p 1-65535 -w 200 -t 0.3
```

| Flag | Meaning | Default |
|------|---------|---------|
| `host` | target to scan (required) | — |
| `-p, --ports` | port or range, e.g. `80` or `1-1024` | `1-1024` |
| `-w, --workers` | concurrent worker threads | `100` |
| `-t, --timeout` | seconds to wait per port | `0.5` |

## What I learned
Sockets and the TCP three-way handshake, why per-port timeouts matter,
I/O-bound concurrency and the GIL, and building a real CLI with `argparse`.

## Legal
Only scan hosts you own or are explicitly authorized to test.
