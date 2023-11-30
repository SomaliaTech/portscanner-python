import socket


def scan(tartgets, ports):
    for port in range(1, ports):
        scaner_port(tartgets, port)



def scaner_port(target, port):
    try:
       sock = socket.socket()
       sock.connect((target, port))
       print("[+] port is Opend", str(port))
       sock.close()
    except : 
        print("[-] port closed")

targets = input('[#] Enter your ip addres split ","')
ports = int(input('[#] Enter the ports you want '))

if ',' in targets: 
    for target in targets.split(','):
        scan(target.strip(' '), ports)


else: 
    scan(targets, ports)