import socket

def port_scan(target_host, target_ports):
    for port in target_ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2)
            result = sock.connect_ex((target_host, port))
            if result == 0:
                print(f"Port {port} is open")
            else:
                print(f"Port {port} is closed")
                sock.close()
        
        except socket.error:
            print(f"Could not connect to port {port}")

# Specify the target host and port range
target_host = "localhost"
target_ports = range(1, 10000)

# Call the port_scan function
port_scan(target_host, target_ports)
