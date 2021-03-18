#!/usr/bin/env python

"""
5. [Optional/bonus] 

*** Note, to actually test this in your environment, change the test IP addresses to something in your environment that you can ping successfully. ***

Construct a list of 254 IP addresses. The base IP address should be equal to '10.10.100.0' or '10.10.100.'.

You should use the 'range' builtin to accomplish this.

Your list should have all of the IP addresses from 10.10.100.1 to 10.10.100.254.

Use Python's 'enumerate' to print out all of the IP addresses and their corresponding list index. The output should look similar to the following: 

0 ---> 10.10.100.1
1 ---> 10.10.100.2
2 ---> 10.10.100.3
3 ---> 10.10.100.4
4 ---> 10.10.100.5
...

Use a list slice to create a new list that goes from 10.10.100.3 to 10.10.100.6.

Using a loop and os.system("ping -c 3 10.10.100.3") try pinging all of the IP addresses in this short list. For Windows the command will probably be os.system("ping -n 3 10.10.100.3").

Put a variable at the top to define whether you are using Windows or Linux/MacOs. This should be similar to the following:

WINDOWS = False

base_cmd_linux = 'ping -c 2'
base_cmd_windows = 'ping -n 2'
# Ternary operator
base_cmd = base_cmd_windows if WINDOWS else base_cmd_linux
"""

import os
from pprint import pprint

base_ip = "10.10.100."

ip_list = []

for i in range(1,255):
    ip = base_ip + str(i)
    ip_list.append(ip)

#pprint(ip_list)

for i, ip in enumerate(ip_list):
    print(f"{i} ---> {ip}")

ping_list = ip_list[2:6]
#print(ping_list)

WINDOWS = False

base_cmd_linux = 'ping -c 2'
base_cmd_windows = 'ping -n 2'

base_cmd = base_cmd_windows if WINDOWS else base_cmd_linux

for ip in ping_list:
    command = base_cmd + " " + ip
    os.system(command)

# just testing with pingable IPs

public_dns = ['8.8.8.8', '8.8.4.4']

for ip in public_dns:
    command = base_cmd + " " + ip
    os.system(command)

"""
alternatively:

base_ip = "10.10.10.0"

ip_list = []

for i in range(1,255):
    octets = base_ip.split(".")
    octets[3] = str(i)
    new_ip = ".".join(octets)
    ip_list.append(new_ip)

pprint(ip_list)
"""

