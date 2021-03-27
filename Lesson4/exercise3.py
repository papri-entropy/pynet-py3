#!/usr/bin/env python

"""
 3.  Read in the 'show_version.txt' file. From this file, 
 
 use regular expressions to extract the OS version, serial number, and configuration register values.

Your output should look as follows:

OS Version: 15.4(2)T1      
Serial Number: FTX0000038X    
​Config Register: 0x2102 
"""

import re
from pprint import pprint

with open('show_version.txt') as f:
    output = f.read()

os_version = re.search(r"^Cisco.*Version (.+),.*", output).group(1)
print(f"OS Version: {os_version}") 

ser_number = re.search(r"^\*0\s+(\S+)\s+(.*)", output, flags=re.M).group(2)
print(f"Serial Number: {ser_number}")

conf_register = re.search(r"^Configuration register is (.*)$", output, flags=re.M).group(1)
print(f"Config Register: {conf_register}")



