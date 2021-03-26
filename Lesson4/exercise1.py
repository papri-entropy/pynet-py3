#!/usr/bin/env python

"""
 1. Create a dictionary representing a network device. The dictionary should have key-value pairs representing the 'ip_addr', 'vendor', 'username', and 'password' fields.

Print out the 'ip_addr' key from the dictionary.

If the 'vendor' key is 'cisco', then set the 'platform' to 'ios'. If the 'vendor' key is 'juniper', then set the 'platform' to 'junos'.

Create a second dictionary named 'bgp_fields'. The 'bgp_fields' dictionary should have a keys for 'bgp_as', 'peer_as', and 'peer_ip'.

Using the .update() method add all of the 'bgp_fields' dictionary key-value pairs to the network device dictionary.

Using a for-loop, iterate over the dictionary and print out all of the dictionary keys.

Using a single for-loop, iterate over the dictionary and print out all of the dictionary keys and values.
"""

from pprint import pprint

device = {
    'ip_addr': '4.4.4.4',
    'vendor': 'cisco',
    'username': 'admin',
    'password': 'secret'
}

print("*" * 80)
print(device['ip_addr'])
print("*" * 80)

if device['vendor'].lower() == 'cisco':
    device['platform'] = 'ios'
elif device['vendor'].lower() == 'juniper':
    device['platform'] = 'junos'

print("*" * 80)
print(device['platform'])
print("*" * 80)

bgp_fields = {
    'bgp_as': 65000,
    'peer_as': 65001,
    'peer_ip': "1.1.1.2"
}

device.update(bgp_fields)

for key in device.keys():
    print(key)

print("*" * 80)

for key, value in device.items():
    print(f"{key:>15} ---> {value:>15}")