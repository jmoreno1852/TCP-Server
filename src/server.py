import socket

def tcp_server(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(2)
    print(f"TPC Server up at {host}:{port}")
    while True:
        c, c_address = s.accept()
        data = c.recv(1024)

def udp_server(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
    s.bind((host.port))
    print(f"UDP Server up at {host}:{port}")
    while True:
        data, c_address = s.recvfrom(1024)



