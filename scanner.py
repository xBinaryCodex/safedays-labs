import socket
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed

def port_scan(host, port, timeout=0.5):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout)
    result = s.connect_ex((host, port))
    s.close()
    return port, result == 0

def service_name(port):
    try:
        return socket.getservbyport(port, "tcp")
    
    except OSError:
        return "unknown"

def scan_range(host, start, end, workers=500, timeout=0.5):
    print(f"Scanning {host} ports {start}-{end} with {workers} workers...\n")
    open_ports = []
    with ThreadPoolExecutor(max_workers=workers) as pool:
        futures = [pool.submit(port_scan, host, port, timeout) for port in range(start, end + 1)]
        for future in as_completed(futures):
            port, is_open = future.result()
            if is_open:
                print(f" [+] Port {port:5d} is OPEN ({service_name(port)})")
                open_ports.append(port)
    open_ports.sort()
    print(f"\nDone. {len(open_ports)} open port(s): {sorted(open_ports)}")
    return open_ports

def parse_ports(port_arg):
    if "-" in port_arg:
        start, end = port_arg.split("-")
        return int(start), int(end)
    p = int(port_arg)
    return p, p

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A simple threaded TCP port scanner.")
    parser.add_argument("host", help="Target host to scan, e.g. 127.0.0.1")
    parser.add_argument("-p", "--ports", default="1-1024", help="Port or range, e.g. 80 or 1-1024 (default: 1-1024)")
    parser.add_argument("-w", "--workers" , type=int, default=100, help="Concurrent workers (default: 100)")
    parser.add_argument("-t", "--timeout", type=float, default=0.5, help="Timeout per port in seconds (deafult:0.5)")
    args = parser.parse_args()

    start, end = parse_ports(args.ports)
    scan_range(args.host, start, end, args.workers, args.timeout)
