#!/usr/bin/python3
import socket
import sys

def scanHost(ip, start, end):
	print("[+] Starting TCP port scan on host %s" % ip)

	for port in range (start, end + 1):
		#Create TCP socket
		tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

		#TCP connection returns an exception (aka != 0)
		if tcp.connect_ex((ip, port)):
			pass
		#TCP connection returns no exceptions (0)
		else:
			print("[+] %s:%d/TCP Open" % (ip, port))
			#Close TCP connection
			tcp.close()

	print("[+] TCP scan on host %s complete" % ip)

def scanRange(network, start, end):
	#Wait time for offline hosts in seconds
	socket.setdefaulttimeout(0.01)
	print("[+] Starting TCP port scan on network %s.0" % network)

	for host in range (1, 255):
		#Iterate range of host IP addresses and concatenate to network string
		ip = network + "." + str(host)

		for port in range (start, end + 1):
			tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

			if tcp.connect_ex((ip, port)):
				pass
			else:
				print("[+] %s:%d/TCP Open" % (ip, port))
				tcp.close()

	print("[+] TCP scan on network %s.0 complete" % network)

if __name__ == "__main__":
	if len(sys.argv) == 4:
		ip		= str(sys.argv[1])
		start 	= int(sys.argv[2])
		end 	= int(sys.argv[3])
		scanHost(ip, start, end)

	elif len(sys.argv) == 5 and sys.argv[4] == "-n":
		network	= str(sys.argv[1])
		start	= int(sys.argv[2])
		end		= int(sys.argv[3])
		scanRange(network, start, end)

	else:
		print("Usage: ./portscanner.py [IP address] [start port] [end port]")
		print("Example: ./portscanner.py 192.168.1.10 1 65535\n")
		print("Usage: ./portscanner.py [network] [start port] [end port] -n")
		print("Example: ./portscanner.py 192.168.1 1 65535 -n")
