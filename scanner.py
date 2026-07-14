import socket

def port_scan(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    result = s.connect_ex((host, port))
    s.close()
    return result == 0

def scan_range(host, start, end):
    print(f"Scanning {host} from port {start} to {end}...\n")
    open_ports = []
    for port in range(start, end + 1):
        if port_scan(host, port):
            print(f"  [+] Port {port} is OPEN")
            open_ports.append(port)
    print(f"\nDone. {len(open_ports)} open port(s) : {open_ports}")
    return open_ports

if __name__ == "__main__":
    scan_range("127.0.0.1", 1, 1024)
