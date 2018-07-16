import argparse
import socket
import os
import sys

def logo():
	print('''
 _____   _____   _____        _____   _____       ___   __   _  
/  ___/ |  _  \ /  ___/      /  ___/ /  ___|     /   | |  \ | | 
| |___  | |_| | | |___       | |___  | |        / /| | |   \| | 
\___  \ |  ___/ \___  \      \___  \ | |       / / | | | |\   | 
 ___| | | |      ___| |       ___| | | |___   / /  | | | | \  | 
/_____/ |_|     /_____/      /_____/ \_____| /_/   |_| |_|  \_| 
''')

def main():
	logo()
	parameters()
	connect()

def parameters():
	global args
	print ("\n[+] Simple Port Scan. SPS is a simple program to scan a port of any host\n")
	parser = argparse.ArgumentParser()
	parser.add_argument("--host", dest="host", action="store", help="Use --host to set the site. ex: sps.py --host www.google.com -p 80")
	parser.add_argument("-p", dest="port", action="store", help="Use -p to scan a specific port. ex: sps.py --host www.google.com -p 80")
	parser.add_argument('-v', dest="version", action='version', version='%(prog)s 1.0')
	args = parser.parse_args()


def connect():
	if (args.host and args.port):
		print ("[+] Target Host: ",args.host)
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(2)
		con = sock.connect_ex((str(args.host),int(args.port)))
		if con == 0:
			print ("[+] Port ",args.port,": open\n")
		else:
			print ("[+] Port ",args.port,": closed\n")
	else:
		print ("[+] Type  sps.py --help to read the manual\n")
		quit()
		
if __name__ == "__main__":
	main()
