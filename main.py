from src.server import tcp_server
#from src.server import udp_server
def main():
    host = "127.0.0.1"
    port = 4444
    tcp_server(host,port)
if __name__ == "__main__":
    main()
