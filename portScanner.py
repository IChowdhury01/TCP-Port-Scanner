# Ivan Chowdhury - TCP Port Scanner
# This program performs the following operations:
#   - Scans port range on a set of target hosts
#       - If a specific range isn't specified, ports 0-1024 are scanned.
#   - Returns open port numbers
#   - If one of the open ports is the default port for a protocol, the protocol name will be listed


# How to run script: 
# Format: python portScanner.py
# The program will prompt you for 
#   - A remote host name/IP (eg google.com)
#   - Whether you'd like to specify a range of ports (Y or N)
#   - Starting port.
#   - Ending port

import socket
import sys
from datetime import datetime

def pScanProgress():
    sys.stdout.write("\rScanning Port %d...\t" % port)
    sys.stdout.flush()
    
# Ask for input
hostIP = input("Enter a remote host to scan: ")

# Ask for port range
ans = input("Would you like to scan a specific range of ports? Y/N: ")
if ans == "Y":
    # Ask for range of ports to scan
    portStart = int(input("Enter the starting port you wish to scan: "))
    portEnd = int(input("Enter the last port you wish to scan: ")) + 1
elif ans == "N":
    portStart = 0
    portEnd = 1024
else:
    print("Answer must be 'Y' or 'N'.")
    sys.exit()
    
# Loading Message
print ("-" * 65)
print ("Scanning remote host. Please wait.", hostIP)
print ("-" * 65)

# Record starting time of scan
t1 = datetime.now()

# Start port scan
for port in range(portStart,portEnd):  
    TCPsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    TCPsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    TCPsock.settimeout(.1)   # .1 second timeout

    try:
        pScanProgress()
        result = TCPsock.connect_ex((hostIP, port))
    except:
        print("Failed to connect to port {}".format(port))

    if result == 0: # Open ports
        if port == 21:  # Default ports for various protocols
            print ("Port {}:\t{}\tOpen".format(port, "FTP"))
        elif port == 22:
            print ("Port {}:\t{}\tOpen".format(port, "SSH"))
        elif port == 23:
            print ("Port {}:\t{}\tOpen".format(port, "Telnet"))
        elif port == 25:
            print ("Port {}:\t{}\tOpen".format(port, "SMTP"))
        elif port == 53:
            print ("Port {}:\t{}\tOpen".format(port, "DNS"))
        elif port == 143:
            print ("Port {}:\t{}\tOpen".format(port, "IMAP"))
        elif port == 110:
            print ("Port {}:\t{}\tOpen".format(port, "POP"))
        elif port == 80:
            print ("Port {}:\t{}\tOpen".format(port, "HTTP"))
        elif port == 443:
            print ("Port {}:\t{}\tOpen".format(port, "HTTPS"))
        else:
            print ("Port {}:\t\tOpen".format(port))


# Record scan end time
t2 = datetime.now()

# Calculate and print scan duration
scanTime =  t2 - t1

print ('[DONE!]\nScanning completed successfully!\nScan Duration:', scanTime)