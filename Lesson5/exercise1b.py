#!/usr/bin/env python

"""
Expand on the ssh_conn function from exercise1 except add a fourth parameter 'device_type' with
a default value of 'cisco_ios'. Print all four of the function variables out as part of the
function's execution.
Call the 'ssh_conn2' function both with and without specifying the device_type
Create a dictionary that maps to the function's parameters. Call this ssh_conn2 function using
the **kwargs technique.
"""

from pprint import pprint

def ssh_conn2(ip_addr, username, password, device_type='cisco_ios'):
    print(f"{'Target IP address is: ' :<25} {ip_addr:>10}")
    print(f"{'Username is: ' :<25} {username:>10}")
    print(f"{'Password is: ' :<25} {password:>10}")
    print(f"{'Device Type is: ' :<25} {device_type:>10}")

ssh_conn2('1.2.3.4', 'admin', 'arista123', 'arista_eos')
print('*' * 80)
ssh_conn2('1.2.3.4', 'admin', 'cisco123')
print('*' * 80)

device2 = {
    "ip_addr": "11.22.33.44",
    "username": "root",
    "password": "secret",
    "device_type": "juniper"
}

ssh_conn2(**device2)
print('*' * 80)

device3 = {
    "ip_addr": "4.3.2.1",
    "username": "test",
    "password": "test123",
    "device_type": "test_type"
}

def ssh_conn3(**kwargs):
    for key in kwargs:
        if key == "ip_addr":
            print(f"{'Target IP address is: ' :<25} {kwargs[key]:>10}")
        elif key == "username":
            print(f"{'Username is: ' :<25} {kwargs[key]:>10}")
        elif key == "password":
            print(f"{'Password is: ' :<25} {kwargs[key]:>10}")
        elif key == "device_type":
            print(f"{'Device Type is: ' :<25} {kwargs[key]:>10}")

ssh_conn3(**device3)
