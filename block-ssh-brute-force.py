#!/usr/bin/python3
import os
sshlog = open("/home/marco/os_scripting/Block_ssh_brute_force/sshdlog", "r")
print(sshlog.readlines())
sshlog.close()