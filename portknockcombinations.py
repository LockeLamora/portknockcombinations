import sys
from itertools import permutations
from pprint import pprint as pp
import os

def main(args):
    paramcheck(args)

    ip_address = str(args[0])
    args.pop(0)
    paramcheck(args)

    knocklist =  list(permutations(args, len(args)))
    command = generate_commands(ip_address, knocklist)
    command = execute_final_scan(command, ip_address)
    execute_command(command)

def paramcheck(params):
    if len(params) < 2:
        print('Not enough ports passed')
        exit()

def generate_commands(ip_address, knocklist):
    command = ''
    for knock in knocklist:
        for port in knock:
            if 'u' in port:
                port = port.replace('u','')
                command += 'nmap -sU -Pn -p '+str(port)+' '+ip_address+' && '
            else:
                command += 'nmap -Pn -p '+str(port)+' '+ip_address+' && '
    return command

def execute_final_scan(command, ip_address):
    return command+'nmap '+ip_address

def execute_command(command):
    os.system(command)


if __name__ == "__main__":
   main(sys.argv[1:])