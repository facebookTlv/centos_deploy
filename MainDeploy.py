#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- author: Alex -*-

from Centos6_Bit64 import *
from SystemUtils import *

# Checking version of OS should happened before menu appears
# Check version of CentOS
SystemUtils.check_centos_version()

# Clear screen before to show menu
os.system('clear')

answer = True
while answer:
    print ("""
    LAMP Deploy Script V: 0.1 for CentOS 6.5/6.6 64Bit:
    ---------------------------------------------------

    1. Check version of your CentOS
    2. Check Internet connection
    3. Show me my local IP address
    4. Open port 80 to Web
    5. Show me my localhost name

    ------- LAMP for CentOS 6.x -----------
    6. Install EPEL & IUS repository
    7. Install Web Server - Apache
    8. Install Database - MySQL
    9. Install Language - PHP
    10. Install LAMP in "One Click" - CentOS 6.x
    11. Exit/Quit
    """)

    answer = input("Please make your choice: ")
    if answer == 1:
        os.system('clear')
        print ('\nChecking version of the system: ')
        SystemUtils.check_centos_version()
    elif answer == 2:
        os.system('clear')
        print ('\nChecking if you connected to the Internet')
        SystemUtils.check_internet_connection()
    elif answer == 3:
        os.system('clear')
        print ('\nYour local IP address is: ' + SystemUtils.check_local_ip())
    elif answer == 4:
        os.system('clear')
        print('\nChecking firewall')
        Centos6Deploy.iptables_port()
    elif answer == 5:
        print "Checking local hostname..."
        SystemUtils.check_host_name()
    elif answer == 6:
        print ('\nInstalling EPEL and IUS repository to the system...')
        Centos6Deploy.add_repository()
    elif answer == 7:
        print ('\nInstalling Web Server Apache...')
        Centos6Deploy.install_apache()
    elif answer == 8:
        print ('\nInstalling database MySQL...')
        Centos6Deploy.install_mysql()
    elif answer == 9:
        print('\nInstalling PHP...')
        Centos6Deploy.install_php()
    elif answer == 10:
        print ('Install LAMP in "One Click" - CentOS 6.x')
        Centos6Deploy.iptables_port()
        Centos6Deploy.add_repository()
        Centos6Deploy.install_mysql()
        Centos6Deploy.install_php()
    elif answer == 11:
        print("\nGoodbye...\n")
        answer = None
    else:
        print ('\nNot valid Choice, Try Again')
        answer = True
