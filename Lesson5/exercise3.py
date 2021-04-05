#!/usr/bin/env python

"""
Similar to lesson3, exercise4 write a function that normalizes a MAC address to the following
format:
01:23:45:67:89:AB
This function should handle the lower-case to upper-case conversion.
It should also handle converting from '0000.aaaa.bbbb' and from '00-00-aa-aa-bb-bb' formats.
The function should have one parameter, the mac_address. It should return the normalized MAC address
Single digit bytes should be zero-padded to two digits. In other words, this:
a:b:c:d:e:f
should be converted to:
0A:0B:0C:0D:0E:0F
Write several test cases for your function and verify it is working properly.
"""

from pprint import pprint

def mac_converter(mac_address):
    mac_address = mac_address.upper()

    if "." in mac_address:
        mac_octets = []
        mac = mac_address.split(".")
        #print(mac)
        for block in mac:
            if len(block) != 4:
                block = block.zfill(4)
                octet1 = block[:2]
                octet2 = block[2:]
                mac_octets.append(octet1)
                mac_octets.append(octet2)
            else:
                octet1 = block[:2]
                octet2 = block[2:]
                mac_octets.append(octet1)
                mac_octets.append(octet2)

        mac_addr_normalized = ":".join(mac_octets)

    elif "-" in mac_address:
        mac_octets = []
        mac = mac_address.split("-")
        for block in mac:
            if len(block) == 2:
                octet1 = block
            else:
                octet1 = '0' + block 
            mac_octets.append(octet1)
        mac_addr_normalized = ":".join(mac_octets)

    elif ":" in mac_address:
        mac_octets = []
        mac = mac_address.split(":")
        for block in mac:
            if len(block) == 2:
                octet1 = block
            else:
                octet1 = '0' + block 
            mac_octets.append(octet1)
        mac_addr_normalized = ":".join(mac_octets)

    return mac_addr_normalized

print(mac_converter('1111.aabb.cc33'))
print(mac_converter('1-2b-4f-f-aa-bb'))
print(mac_converter('a:b:c:d:e:1f'))

# Testing

assert "01:23:02:34:04:56" == mac_converter("123.234.456")
assert "AA:BB:CC:DD:EE:FF" == mac_converter("aabb.ccdd.eeff")
assert "0A:0B:0C:0D:0E:0F" == mac_converter("a:b:c:d:e:f")
assert "01:02:0A:0B:03:44" == mac_converter("1:2:a:b:3:44")
assert "0A:0B:0C:0D:0E:0F" == mac_converter("a-b-c-d-e-f")
assert "01:02:0A:0B:03:44" == mac_converter("1-2-a-b-3-44")

print("Tests Passed")
