#!/usr/bin/env python3
import nmap


scanner = nmap.PortScanner()

print('Hi')

ip_addr = input('Please insert the ip addreso to scan: ')
print('the ip you enter is :' + ip_addr)


resp = input("1) syn ack scan 2)udp scan 3) comprehnsive scan: ")
print("you select:",resp)

if resp == '1':
    print('nmap version: ', scanner.nmap_version())
    scanner.scan(str(ip_addr), '1-1024', '-v -sS')
    print(scanner.scaninfo())
    print("ip status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print('Open ports: ' , scanner[ip_addr]['tcp'].keys())
elif resp == '2':
    print('nmap version: ', scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-v -sU')
    print(scanner.scaninfo())
    print("ip status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print('Open ports: ' , scanner[ip_addr]['udp'].keys())
elif resp == '3':
    print('nmap version: ', scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-v -sS -sV -sC -A -O')
    print(scanner.scaninfo())
    print("ip status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print('Open ports: ' , scanner[ip_addr]['tcp'].keys())
elif resp >= '4':
    print('please enter a valid option')
     