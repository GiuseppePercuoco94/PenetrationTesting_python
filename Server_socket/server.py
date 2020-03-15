#!/usr/bin/env python3

import socket

"""
- AF_INET: ipv4
- SOCK_STREAM: is a TCP socket, if it has been UDP it would has been SOCK_DGRAM
"""
server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#retrieve the IP 
host = socket.gethostname()
print('ip server: ' +str(host)) 
port = 8888

server_sock.bind((host,port))
#backlog= number of connection acceppted
server_sock.listen(3)

while True:
    client_sock, address = server_sock.accept()
    print('connection established from address' + str(address[0])+ 'and port: ' +str(address[1]))
    message = 'Thank you for connecting'
    client_sock.send(message.encode('utf-8'))
    client_sock.close()

