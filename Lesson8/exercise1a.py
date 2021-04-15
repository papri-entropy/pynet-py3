#!/usr/bin/env python

"""
Import the 'datetime' library. Print out the module that is being imported by datetime (the
__file__ attribute)
Import the Python ipaddress library. Print out the module that is being imported by ipaddress (the
__file__ attribte).
Import sys and use pprint to pretty print the sys.path.
"""

import datetime
import ipaddress
import sys
from pprint import pprint

print(datetime.__file__)
print(ipaddress.__file__)
pprint(sys.path)
