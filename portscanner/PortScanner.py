#!/usr/bin/env python3

import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.settimeout(10)

host = input('Please enter a ip to scan: ')
port = input('Enter the port: ')

def portScanner(port):
    if s.connect_ex((host,int(port))):
        print('The port is closed')
    else:
        print('The port is open')
        
portScanner(port)