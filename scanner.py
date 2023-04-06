# Importing Scapy and Regex
import scapy.all as scapy
import re

# Regular Expression for IPv4 Address
ipv4Format = re.compile('^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}/\d*$')

# While Loop to Keep Asking User For a Valid Network Range
while True:
    
    # Inputting Network Range
    ipv4Range = input('Input a network range you would like to scan (e.g 192.168.1.0/24): ')
    
    # Check If Network Range Matches Correct IPv4 Regex Format
    if ipv4Format.search(ipv4Range):
        
        # Breaking Loop
        break

# Sending ARP Requests To Each IP on Network Range.
results = scapy.arping(ipv4Range)
