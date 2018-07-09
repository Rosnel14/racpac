#Actualizado Lunes,28 de mayo dos mil diez y ocho
#Autor: Rosnel Alejandro Leyva-Cortes#
import os
import re
import sys
import struct
import socket


#initial ping
#for the hostname

def ping ():
    welcome = str = raw_input('''\nIn order to perform a test, we must determine if the host is up.''')
    hostname = str1 = raw_input("\nInput Hostname: ")
    response = os.system("ping -c 10 " + hostname)

    #and then check the response...
    if response == 0:
        print (hostname + ' is up! ') #End result is self explanatory
        mainMenu()
def Cloudflare():
     print('Not ready yet')
     mainMenu()
def traceroute():
    print '''Usage: %s host port
    Tries to connect to host at TCP port with increasing TTL (Time to live).
    If /etc/services exists (on most Unix systems), you can give the protocol
    name for the port. Example 'ssh' instead of 22.
    ''' % os.path.basename(sys.argv[0])
    print 'run as root!'
    val = str3 = raw_input("\nBegin tracert? Y/N:")
    if val is 'Y':
        tracert();
    elif val is 'Yes':
        tracert();
    elif val is 'yes':
        tracert();
    elif val is 'No':
        mainMenu();
    elif val is 'no':
        mainMenu();
    elif val is 'N':
        mainMenu();
    else:
        print('That is not a valid option.')
        traceroute();


def q():
    print(''' You are a horrible ''')
    exit()

def mainMenu():
        print (''' 
     _______    ______   _______  
    /       \  /      \ /       \ 
    $$$$$$$  |/$$$$$$  |$$$$$$$  |
    $$ |__$$ |$$ |  $$/ $$ |__$$ |
    $$    $$< $$ |      $$    $$/ 
    $$$$$$$  |$$ |   __ $$$$$$$/  
    $$ |  $$ |$$ \__/  |$$ |      
    $$ |  $$ |$$    $$/ $$ |      
    $$/   $$/  $$$$$$/  $$/       

    https://sourceforge.net/projects/foxnukepy/
    https://twitter.com/PotatoSkins16
    Choose one
                              ''')
        print('1. Ping host')
        print('2. Cloudflare check')
        print('3. tracert')
        print('4 Quit')
        sel=int(input("\nEnter choice: "))
        if sel==1:
            ping()
        elif sel==2:
            Cloudflare()
        elif sel==3:
            traceroute()
        elif sel==4:
            q()
        else:
            print('That is not a valid choice!!!')
            mainMenu()




mainMenu()
