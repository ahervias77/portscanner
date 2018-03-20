#!/usr/bin/python3
import socket
import sys


def scanHost(ip, startPort, endPort):
    """ Starts a TCP scan on a given IP address """

    print("[+] Starting TCP port scan on host %s" % ip)

    #Begin TCP scan on host
    tcp_scan(ip, startPort, endPort)

    print("[+] TCP scan on host %s complete" % ip)


def scanRange(network, startPort, endPort):
    """ Iterates a range of IP addresses given a network ID
        Starts a TCP scan on the range of IP addresses
    """

    print("[+] Starting TCP port scan on network %s.0" % network)

    for host in range (1, 255):

        #Iterate range of host IP addresses and concatenate to network string
        ip = network + "." + str(host)

        #Begin TCP scan on host
        tcp_scan(ip, startPort, endPort)

    print("[+] TCP scan on network %s.0 complete" % network)


def tcp_scan(ip, startPort, endPort):
    """ Creates a TCP socket and attempts to connect via supplied ports """

    for port in range (startPort, endPort + 1):

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


if __name__ == '__main__':

    #Timeout in seconds
    socket.setdefaulttimeout(0.01)

    if len(sys.argv) < 4:

        print("Usage: ./portscanner.py [IP address] [start port] [end port]")
        print("Example: ./portscanner.py 192.168.1.10 1 65535\n")
        print("Usage: ./portscanner.py [network] [start port] [end port] -n")
        print("Example: ./portscanner.py 192.168.1 1 65535 -n")

    elif len(sys.argv) >= 4:

        network   = sys.argv[1]
        startPort = int(sys.argv[2])
        endPort   = int(sys.argv[3])

    if len(sys.argv) == 4:

        scanHost(network, startPort, endPort)

    if len(sys.argv) == 5:

        scanRange(network, startPort, endPort)
