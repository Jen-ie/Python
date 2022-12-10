# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 13:25:48 2022

@author: Jen
"""

"""" 
FTP file downloader Tested with Python >=3.6 
By: JOR v0.1 20AUG20 
""" 
import ftplib 
import settings.ftp as settings 
# Make the connection 
ftp = ftplib.FTP(settings.FTP['URL']) 
# Anonymous login 
ftp.login() 
# Change to the correct directory 
ftp.cwd(settings.FTP["PATH"]) 
# Retrieve the file 
ftp.retrbinary("RETR " + settings.FTP["FILENAME"], open(settings.FTP["FILENAME"], 'wb').write) 
ftp.quit()