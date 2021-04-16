#!/usr/bin/python3
import os
import re
import ipaddress

sshlog = open("/home/marco/os_scripting/Block_ssh_brute_force/sshdlog", "r")
#print(sshlog.readlines())

bad_ip = set() # creating a set for unique ip-adresses

for line in sshlog.readlines():
    #print("test" + line)
    if "Invalid user" in line: 
       #print(line)  # will show login attempts from invalid users
       ip = str(re.findall("[0-9]*[0-9][.][0-9]*[0-9][.][0-9]*[0-9][.][0-9]*[0-9]", line))
       #remove []
       ip = ip.strip("['']")
       #print(ip)
       bad_ip.add(ip)
print(bad_ip)



sshlog.close()

