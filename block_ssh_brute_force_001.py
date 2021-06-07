#!/usr/bin/env python3


import os
import re
import sys
import fwblock
import getopt

bad_ip = set() # create a set for unique IP-addresses, variable needs to be declared

def searchlog():
    for line in sshdlogfile:
        # shows every attempt with 'invalid user', shows 3 entries
        # shows first attempt with 'Invalid user', shows unique accounts
        if 'invalid user' in line: 
            # matches a character from 0 to 9
            # + matches previous token between 1 and unlimited times
            # (?:) group 
            # \. escape character and matches a dot
            # {3} matches the previous token 3 times
            ip = str(re.findall(r'[0-9]+(?:\.[0-9]+){3}', line)) # regex: find octets
            ip = ip.strip("['']") # remove brackets and apostrophes
            bad_ip.add(ip) # add unique IP-addresses to set

try:
    opts, argv = getopt.getopt(sys.argv[1:], "hnv") # variables for getopt
    for opt, arg in opts:
      
        if opt in '-h':
            print("This is an overview of the options you have viewing the logfiles. -h.\
                \n-h\tprint the helpfile \
                \n-n\tprint all IP-addresses that are in the logfile \
                \n-v\tprint all blocked IP-addresses in logfile and number of blocked IP-addresses")
        
        elif opt in '-v' or '-n' or '-z':
            # sshdlog is the default file
            sshdlog = open("./sshdlog", "r") # open log as read-only
            sshdlogfile = sshdlog.readlines() # read every line of log
            sshdlog.close() # close filestream
            searchlog()
            if opt in '-v':    
                for ip in bad_ip:
                    fwblock.block_ip(ip)
                    print("blocking " + ip)  
                    qty_ip = len(bad_ip)
            
            elif opt in '-n':
                print("\nReading ip-addresses from logfile:\n")
                for ip in bad_ip:
                    print(ip)

        try:
            if opt not in '-h':
                print("\n" + str(qty_ip) + " ip-addresses blocked\n")
        except:
            print("\n0 ip-addresses blocked\n")

except getopt.GetoptError as err:
    print(err)
    sys.exit(2)