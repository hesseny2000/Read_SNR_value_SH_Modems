#!/bin/bash
#coding = UTF8
################################################
################################################
##this programe written to retrive           ###
##the SNR vlaue from different type of the   ###
##below EFM modems list                      ###
## ZyXEL P-700 series                        ###
## aethra AC2036                             ###
##that is worked with the SHDsl services #######
##EFM:Ethernet in the first mile         #######
################################################
##written by Mohamed.hosseny####################
##Email: mohamed.hosseny@outlook.com############
##Mobil: +2 01064960035  @Egypt     ############
## Python 2.7                       ############
## tested 2015                  ################
################################################

import sys
import telnetlib
import re,socket
import time
HOST = "192.168.1.1"
USER = "admin"
PASS = "password"
#the Host name of the Athera device
Aethra  = "hostname"
#the Host name of the zyxel device
Zyxel= "zyhostname"

##########################
# validate an Ip address##
##########################
"""regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
#def check(Ip):
 
    # pass the regular expression
    # and the string in search() method
 #   if(re.search(regex, Ip)):
  #      print("Valid Ip address")
         
   # else:
   #     print("Invalid Ip address")/*
"""      
#chec the local ip to avoid the ip confilct
host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
local_ip = "192.168.1."
if local_ip not in host_ip:
    print "your local ip is " + host_ip + ", so ther is a confilct IP,"+ "\n" + " change your local ip "
    sys.exit()
else:
    print "your local ip is " + host_ip
    print "Waiting..."
#Handle the Error and exit in case we found that there is no connection
try:
   tn = telnetlib.Telnet(HOST,23,5)
   frist_log = tn.read_until("d:")
except:
   print "oops! there is a connection error"
                                                                                         

   sys.exit()
   #check the modem type (Zyxel OR Athera EFM)
   #tn.read_until(":")
   #print frist_log
if Aethra in frist_log:
    me2=tn.read_until("pass:",5)
    #print me2
    tn.write(USER + "\n")
    if password:
        tn.read_until("pass",5)
        tn.write(PASS + "\n")
        tn.write("show shdsl0 shdsl0.0 status -s \n")
        tn.read_until("ATOS>",5)
        output1 = tn.read_until("ATOS>")
        print output1
        #tn.read_all()
        tn.write("exit\n")
        print tn.read_all()
        #resualt = tn.read_all()
        #READ_ALL OUTPUT_DATA FROM THE BELOW command to find the SNR 
        #print "show shdsl0 shdsl0.0 status -s \n" + "\n"
        #tn.read_from "Pair 1" to "executed "
else:
    tn.write(PASS + "\n")
    tn.read_until("Number:",2)
    #print m21
    tn.write("24"+ "\n")
    #tn.read_until("Number:",5)
    tn.write("8"+ "\n")
    tn.read_until("ras>",5)
    tn.write("xdsl pmparam 0 2" + "\n")
    #print tn.read_all()
    #print tn.write("xdsl pmparam 0 2" + "\n")
    me23=tn.read_until("Pair 1",5)
    #print me23
    #to convert from Hex to decimal
    snr = me23[220:228]
    snr = int (snr,16)
    print ("the SNR of line is : ") + str (snr)
tn.close()
