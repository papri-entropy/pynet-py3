#!/usr/bin/env python

"""
Copy your solution from exercise3 to exercise4. Add an 'import pdb' and pdb.set_trace() statement
outside of your function (i.e. where you have your function calls).
Inside of pdb, experiment with:
1. Listing your code.
2. Using 'next' and 'step' to walk through your code. Make sure you understand the difference
   between the two.
3. Experiment with 'up' and 'down' to move up and down the code stack.
4. Use p <variable> to look at a variable.
5. Set a breakpoint and run your code to the breakpoint.
6. Use '!command' to change a variable (for example !new_mac = [])
"""

from pprint import pprint
import pdb

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

pdb.set_trace()
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
