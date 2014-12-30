#/bin/python

import os

scpTarget = raw_input("Enter The SSH stuff(who@where): ")

fileNeeded = raw_input("Enter the file you want: ")

whereGo = raw_input("Where should I put it?: ")

portQ = raw_input("Do you need an alt port?: ")

portQ = portQ.lower()

if portQ == "y" or portQ == "yes":
    port = raw_input("Enter the port number")
    os.system("scp -p" + port + " " + scpTarget + ":" + fileNeeded + " " + whereGo)

else:
    os.system("scp " + scpTarget + ":" + fileNeeded + " "  + whereGo)

print "I got it! \nBye"
