#!/usr/bin/env python

"""
Create an ssh_conn function. This function should have three parameters: ip_addr, username, and
password. The function should print out each of these three variables and clearly indicate which
variable it is printing out.
Call this ssh_conn function using entirely positional arguments.
Call this ssh_conn function using entirely named arguments.
Call this ssh_conn function using a mix of positional and named arguments.
"""

from pprint import pprint

def ssh_conn(ip_addr, username, password):
    print(f"{'Target IP address is: ' :<25} {ip_addr:>10}")
    print(f"{'Username is: ' :<25} {username:>10}")
    print(f"{'Password is: ' :<25} {password:>10}")

ssh_conn('1.2.3.4', 'admin', 'arista123')
print('*' * 80)
ssh_conn(username='admin', password='arista123', ip_addr='1.2.3.4')
print('*' * 80)
ssh_conn('1.2.3.4', password='arista123', username='admin')
