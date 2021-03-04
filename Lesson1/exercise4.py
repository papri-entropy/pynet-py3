#!/usr/bin/enn python

"""
 4. Create a show_version variable that contains the following

 show_version = "*0        CISCO881-SEC-K9       FTX0000038X    " 


Remove all leading and trailing whitespace from the string.

Split the string and extract the model and serial_number from it.

Check if 'Cisco' is contained in the model string (ignore capitalization).

Check if '881' is in the model string.

Print out both the serial number and the model.
"""

show_version = "*0        CISCO881-SEC-K9       FTX0000038X    " 

show_ver_clean = show_version.strip()

#print(show_version)
#print(repr(show_ver_clean))

model = show_ver_clean.split()[1]
print(model)
serial_number = show_ver_clean.split()[2]
print(serial_number)

print("Cisco is in model: {}".format("Cisco".lower() in model.lower()))
print("881 is in model: {}".format(str(881) in model.lower()))
