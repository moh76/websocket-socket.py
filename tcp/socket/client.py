
#!/usr/bin/env python3

import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 15560       # The port used by the server
flag = True
name = ""
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    clientmessage = input("enter name ")
    # clientmessage = int(clientmessage)
    s.sendall(clientmessage.encode())
    while True:
        data = s.recv(1024)
        print('Received', repr(data))

