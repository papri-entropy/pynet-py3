#!/usr/bin/env python

"""
 2. Create three separate lists of IP addresses. 
 
 The first list should be the IP addresses of the Houston data center routers, 
 
 and it should have over ten RFC1918 IP addresses in it (including some duplicate IP addresses).

The second list should be the IP addresses of the Atlanta data center routers, and it should have 

at least eight RFC1918 IP addresses (including some addresses that overlap with the Houston data center).

The third list should be the IP addresses of the Chicago data center routers, and it should have 

at least eight RFC1918 IP addresses. The Chicago IP addresses should have some overlap with both the IP addresses in Houston and Atlanta.

Convert each of these three lists to a set.

Using a set operation, find the IP addresses that are duplicated between Houston and Atlanta.

Using set operations, find the IP addresses that are duplicated in all three sites.

Using set operations, find the IP addresses that are entirely unique in Chicago.
"""

from pprint import pprint

houston_dc = [
'192.168.1.1', 
'192.168.1.2', 
'192.168.1.3', 
'192.168.1.4', 
'10.10.10.1', 
'10.10.10.2', 
'10.10.10.3', 
'10.10.10.4',
'192.168.1.4',
'10.10.10.4',
'172.16.1.1',
'172.16.1.2'
]

atlanta_dc = [
'192.168.11.1', 
'192.168.11.2', 
'192.168.11.3', 
'192.168.11.4', 
'10.10.10.1', 
'10.10.10.2', 
'10.10.10.3', 
'10.10.100.4',
'172.16.11.1',
'172.16.11.2'
]

chicago_dc = [
'10.10.10.1', 
'10.10.10.2', 
'10.4.4.1',
'10.4.4.2',
'10.4.4.3',
'10.4.4.4',
'172.16.11.1',
'172.16.11.2',
'192.168.44.44',
'192.168.44.45',
'192.168.44.46'
]

houston_dc_set = set(houston_dc)
atlanta_dc_set = set(atlanta_dc)
chicago_dc_set = set(chicago_dc)

#print(dir(houston_dc_set))

hous_atl_intersection = houston_dc_set.intersection(atlanta_dc_set)
print(f"""
Houston and Atlanta IP duplicates:
{hous_atl_intersection}
""")
print('*' * 80)

hous_atl_chi_intersection = hous_atl_intersection.intersection(chicago_dc_set)
print(f"""
Houston, Atlanta and Chicago IP duplicates: 
{hous_atl_chi_intersection}
""")
print('*' * 80)

chi_unique = chicago_dc_set.difference(houston_dc_set, atlanta_dc_set)
print(f"""
Chicago IP uniques: 
{chi_unique}
""")
print('*' * 80)