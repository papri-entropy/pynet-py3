#!/usr/bin/env python

"""
3.  Read the 'show_lldp_neighbors_detail.txt' file. Loop over the lines of this file. 

Keep reading the lines until you have encountered the remote "System Name" and remote "Port id". 

Save these two items into variables and print them to the screen. 
 
You should extract only the system name and port id from the lines (i.e. your variables should only have 'twb-sf-hpsw1' and '15'). 
 
Break out of your loop once you have retrieved these two items.
"""

from pprint import pprint

with open("show_lldp_neighbors_detail.txt") as f:
    neigh_lldp_data = f.readlines()

#pprint(neigh_lldp_data)

system_found = None
port_id_found = None

for line in neigh_lldp_data:
    if "System Name" in line:
        system_name = line.split()[2]
        #print(system_name)
        system_found = True
    elif "Port id" in line:
        port_id = line.split()[2]
        #print(port_id)
        port_id_found = True
    if system_found and port_id_found:
        break
    #print(system_found, port_id_found)

print(f"System name: {system_name}")
print(f"Port ID: {port_id}")