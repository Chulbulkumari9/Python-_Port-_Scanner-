import socket

def port_scanner(ip, ports):
    print(f"Scanning {ip}...")
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"Port {port} is OPEN")
        sock.close()

if __name__ == "__main__":
    target_ip = input("Enter target IP: ")
    port_range = range(1, 1025)
    port_scanner(target_ip, port_range)
