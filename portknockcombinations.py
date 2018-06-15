import sys
from itertools import permutations
import socket
import os

def main(args):
    paramcheck(args)

    ip_address = str(args[0])
    args.pop(0)
    paramcheck(args)

    knocklist =  list(permutations(args))
    doscan(ip_address, knocklist)
    execute_final_scan(ip_address)


def paramcheck(params):
    if len(params) < 2:
        print('Not enough ports passed')
        exit()

def doscan(ip_address, knocklist):
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    for knock in knocklist:
        for port in knock:
            if 'u' in port:
                port = port.replace('u','')
                try:
                    udp.connect((ip_address, int(port)))
                except:
                    pass
            else:
                try:
                    tcp.connect((ip_address, int(port)))
                except:
                    pass

def execute_final_scan(ip_address):
    os.system('nmap '+ip_address)

if __name__ == "__main__":
   main(sys.argv[1:])
