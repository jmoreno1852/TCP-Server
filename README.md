# Simple TCP Server in Python

This project implements a **simple TCP server** in Python designed to receive messages from clients.  
The implementation of a **UDP server** is also available but commented out for now.  

Both modules (`tcp_server` and `udp_server`) are defined in the `server.py` file located in the `src` directory.  
These modules can be imported into `main.py` to boot up either a **TCP** or **UDP server**.

## How to Use

1. Clone this repository:
   ```bash
   git clone https://github.com/jmoreno1852/TCP-Server.git
   cd TCP_Server
2. Run script to start the server:
   ```bash     
   python main.py
3. You can customize the host and port in main.py as needed.

## File Structure

📁 project-name/

│── 📁 src/

│   │── server.py   # Contains tcp_server() and udp_server()

│── main.py                # Entry point to boot up the server

│── README.md              # Documentation

