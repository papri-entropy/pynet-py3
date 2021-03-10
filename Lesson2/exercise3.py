#!/usr/bin/env python

"""
 3. Read in the "show_arp.txt" file using the readlines() method. Use a list slice to remove the header line.

Use pretty print to print out the resulting list to the screen, syntax is:

from pprint import pprint
pprint(some_var)


Use the list .sort() method to sort the list based on IP addresses.

Create a new list slice that is only the first three ARP entries.

Use the .join() method to join these first three ARP entries back together as a single string using the newline character ('\n') as the separator.

Write this string containing the three ARP entries out to a file named "arp_entries.txt".
"""

from pprint import pprint

banner = "*" * 80
with open("show_arp.txt") as f:
    show_arp = f.readlines()

show_arp = show_arp[1:]
pprint(show_arp)
print(banner)
show_arp.sort()
pprint(show_arp)

arp_slice = show_arp[:3]
pprint(arp_slice)

arp_string = "\n".join(arp_slice)
print(arp_string)

f = open("arp_entries.txt", mode="w")
f.write(arp_string)
f.close

"""
alternatively

with open("arp_entries.txt", "wt") as f:
    f.write(arp_string)

wt ---> t refers to the text mode. There is no difference between r and rt or w and wt since text mode is the default.

"""