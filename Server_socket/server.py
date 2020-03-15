#!/usr/bin/env python3

import socket

"""
- AF_INET: ipv4
- SOCK_STREAM: is a TCP socket, if it has been UDP it would has been SOCK_DGRAM
"""
server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#retrieve the IP 
host = socket.gethostbyname()
port = 8888

server_sock.bind((host,port))
#backlog= number of connection acceppted
server_sock.listen(backlog=3)

while True:
    client_sock, address = server_sock.accept()
    print('connection established from ' + str(address))
    message = 'Thank you for connecting'
    client_sock.close()

