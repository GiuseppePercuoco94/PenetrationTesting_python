#!/usr/bin/env python3

import socket


client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM,)
host = socket.gethostname()
port = 8888
client_sock.connect((host,port))

message = client_sock.recv(1024)
client_sock.close()

print(message.decode('utf-8'))
