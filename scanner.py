import scapy.all as scapy
import re

# Regular Expression for IPv4 Address
ipv4Format = re.compile('^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}/\d*$')

while True:
    ipv4Range = input('Input a network range you would like to scan (e.g 192.168.1.0/24): ')
    if ipv4Format.search(ipv4Range):
        break

results = scapy.arping(ipv4Range)
