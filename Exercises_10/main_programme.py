# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 13:06:08 2022

@author: Jen
"""

from file_utilities import path_name, log_file_name 

from os_utilities import detect_os 

# Check the OS in use, and figure out a log file name and path 

this_os = detect_os() 
log_path = path_name() 
filename = log_file_name(".log") 
print(log_path + filename )