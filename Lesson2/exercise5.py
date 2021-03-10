#!/usr/bin/env python

"""
5. Read the 'show_ip_bgp_summ.txt' file into your program. From this BGP output obtain the first and last lines of the output.

From the first line use the string .split() method to obtain the local AS number.

From the last line use the string .split() method to obtain the BGP peer IP address.

Print both local AS number and the BGP peer IP address to the screen.
"""
banner = "*" * 80

with open("show_ip_bgp_summ.txt") as f:
    bgp_summ = f.readlines()

print(banner)
print(bgp_summ)
bgp_summ_first = bgp_summ[0].strip()
print(banner)
print(bgp_summ_first)
bgp_summ_last = bgp_summ[-1].strip()
print(banner)
print(bgp_summ_last)
local_as = bgp_summ_first.split()[-1]
print(banner)
print(f"Local AS Number: {local_as}")
bgp_peer_ip = bgp_summ_last.split()[0]
print(banner)
print(f"BGP Peer IP: {bgp_peer_ip}")
