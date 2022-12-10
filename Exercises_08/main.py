# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 15:24:25 2022

@author: Jen
"""

from devices import Firewall 
# Create a firewall instance 
firewall27 = Firewall("firewall27") 
# Configure it 
firewall27.configure_firewall() 

# Create a firewall instance 
firewall28 = Firewall("firewall28") 
# Verify a CRC 
firewall28.calculate_crc("dummy data")

# from devices import Router 
# # Create a Router instance 
# router1 = Router("router1") 
# # Configure it 
# router1.configure_router() 

# # Create a router instance 
# router2 = Router("router2") 
# # Verify a CRC 
# router2.calculate_crc("dummy data")

# from devices import Switch 
# # Create a switch instance 
# switch12 = Switch("switch12") 
# # Configure it 
# switch12.configure_switch() 

# # Create a switch instance 
# switch22 = Switch("switch22") 
# # Verify a CRC 
# switch22.calculate_crc("dummy data")


#To check fw is an object in the Firewall class###
#print(isinstance(firewall27, Firewall))