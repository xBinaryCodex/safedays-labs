import socket
from concurrent.futures import ThreadPoolExecutor, as_completed

def port_scan(host, port, timeout=0.5):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout)
    result = s.connect_ex((host, port))
    s.close()
    return port, result == 0

def scan_range(host, start, end, workers=500, timeout=0.5):
    print(f"Scanning {host} ports {start}-{end} with {workers} workers...\n")
    open_ports = []
    with ThreadPoolExecutor(max_workers=workers) as pool:
        futures = [pool.submit(port_scan, host, port, timeout) for port in range(start, end + 1)]
        for future in as_completed(futures):
            port, is_open = future.result()
            if is_open:
                print(f" [+] Port {port} is OPEN")
                open_ports.append(port)
    open_ports.sort()
    print(f"\nDone. {len(open_ports)} open port(s): {sorted(open_ports)}")
    return open_ports

if __name__ == "__main__":
    scan_range("127.0.0.1", 1, 1024)
