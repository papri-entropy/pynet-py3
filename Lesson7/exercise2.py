#!/usr/bin/env python

"""
Using Python and Jinja2 templating generate the following OSPF configuration:
----
interface vlan 1
   ip ospf priority 100
router ospf 10
   passive-interface default
   no passive-interface Vlan1
   no passive-interface Vlan2
   network 10.10.10.0/24 area 0.0.0.0
   network 10.10.20.0/24 area 0.0.0.0
   network 10.10.30.0/24 area 0.0.0.0
   max-lsa 12000
----
The following items should be variables in your Jinja2 template:
----
ospf_process_id
ospf_priority
ospf_active_interfaces (i.e. the non-passive interfaces)
ospf_area0_networks (the three networks that are specified as belonging to area0)
----
Your template should be in an external file.
Your template should also use a conditional to control whether this is output or not:
----
interface vlan 1
   ip ospf priority 100
----
If the 'ospf_priority variable is defined', then include that section. If 'ospf_priority' is not
defined then only include the 'router ospf 10' section.
"""

import jinja2

ospf_template = "ospf_template.j2"
ospf_vars = {
        "ospf_priority": 100,
        "ospf_process_id": 10,
        "ospf_active_interfaces": ["Vlan1", "Vlan2"],
        "ospf_area0_networks": ["10.10.10.0/24", "10.10.20.0/24", "10.10.30.0/24"]
}

with open(ospf_template) as f:
    ospf = f.read()

template = jinja2.Template(ospf)
ospf_config = template.render(ospf_vars)

print(ospf_config.strip())