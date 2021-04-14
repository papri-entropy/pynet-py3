#!/usr/bin/env python

"""
Take the YAML file and corresponding data structure that you defined in exercise3b:
{'interfaces': {
    'Ethernet1': {'mode': 'access', 'vlan': 10},
    'Ethernet2': {'mode': 'access', 'vlan': 20},
    'Ethernet3': {'mode': 'trunk',
                  'native_vlan': 1,
                  'trunk_vlans': 'all'}
    }
}
From this YAML data input source, use Jinja templating to generate the following configuration
output:
----
interface Ethernet1
  switchport mode access
  switchport access vlan 10
interface Ethernet2
  switchport mode access
  switchport access vlan 20
interface Ethernet3
  switchport mode trunk
  switchport trunk native vlan 1
  switchport trunk allowed vlan all
----
The following should all be variables in your Jinja template (the names may be different than
below, but they should be variabilized and not be hard-coded in your template).
----
interface_name
switchport_mode
access_vlan
native_vlan
trunk_vlans
----
All your Jinja2 variables should be retrieved from your YAML file.
This exercise might be challenging.
"""

from pprint import pprint
import yaml
import jinja2

interfaces_yaml = "exercise3b.yaml"
interfaces_template = "interfaces.j2"

with open(interfaces_yaml) as f:
    intf_vars_output = yaml.safe_load(f)
#pprint(intf_vars_output)

with open(interfaces_template) as f:
    intf_temp_output = f.read()

template = jinja2.Template(intf_temp_output)
interfaces_config = template.render(intf_vars_output)

print(interfaces_config.strip())