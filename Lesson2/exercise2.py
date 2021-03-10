#!/usr/bin/env python

"""
 2. Create a list of five IP addresses.

Use the .append() method to add an IP address onto the end of the list. Use the .extend() method to add two more IP addresses to the end of the list.

Use list concatenation to add two more IP addresses to the end of the list.

Print out the entire list of ip addresses. Print out the first IP address in the list. Print out the last IP address in the list.

Using the .pop() method to remove the first IP address in the list and the last IP address in the list.

Update the new first IP address in the list to be '2.2.2.2'. Print out the new first IP address in the list.
"""

ip_addr_list = ['10.10.10.10', '20.20.20.20', '30.30.30.30', '40.40.40.40', '50.50.50.50']
print(ip_addr_list)
ip_addr_list.append('60.60.60.60')
print(ip_addr_list)
ip_addr_list.extend(['70.70.70.70', '80.80.80.80'])
print(ip_addr_list)
ip_addr_list = ip_addr_list + ['90.90.90.90', '100.100.100.100']
print(ip_addr_list)
print(ip_addr_list[0], ip_addr_list[-1])
ip_addr_list.pop(0)
ip_addr_list.pop()
print(ip_addr_list)
ip_addr_list[0] = '2.2.2.2'
print(ip_addr_list)
print(ip_addr_list[0])