#!/usr/bin/env python

"""
Use Jinja2 templating to render the following:
vlan {{ vlan_id }}
   name {{ vlan_name }}
Your template should be inside of your Python program for simplicity.
The output from processing your template should be as follows. This should be printed to stdout.
vlan 400
   name red400
"""

from pprint import pprint
import jinja2

vlan_template = """
vlan {{ vlan_id }}
   name {{ vlan_name }}
"""

vlan_vars = {
    "vlan_id": 400,
    "vlan_name": "red400"
}

"""
#from jinja2 import Template
#t = Template(vlan_template)
"""

t = jinja2.Template(vlan_template)
output_config = t.render(vlan_vars)

print(output_config.strip())
