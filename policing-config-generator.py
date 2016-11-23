# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 11:25:01 2016
 
@author: cw186026
"""
#opening input file
file = open('input.txt', 'r')
 
#iterating through input file line by line and split/save details into variables
for line in (x.rstrip ('\n') for x in file):
    current_line = line.split(",")
    
    gateway_ip = current_line[0]
    cust_number = current_line[1]
    cust_name = current_line[2]
    
    #generating & printing config for each line with above generated variables of input file
    print("ipv4 access-list QoS_100m_Police_CUST0{}".format(cust_number))
    print(" 10 remark {} VPN Gateway".format(cust_name))
    print(" 20 permit ipv4 host {} any".format(gateway_ip))
    print("!")
    print("class-map match-all CM_100m_Police_CUST0{}".format(cust_number))
    print(" match access-group ipv4 QoS_100m_Police_CUST0{}".format(cust_number))
    print("end-class-map")
    print("!")
    print("policy-map Customer_QoS_In")
    print("class CM_100m_Police_CUST0{}".format(cust_number))
    print(" police rate 100 mbps")
    print(" conform-action transmit")
    print(" violate-action drop")
    print("!")
    print("end-policy-map")
    print("!")
    print("!")
 
print("commit")
 
#closing input file
file.close()
