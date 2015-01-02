
#/bin/python
import os

again = 'y'
while again == 'y':
    
    scpTarget = raw_input("Enter The SSH stuff(who@where): ")
    
    portQ = raw_input("Do you need an alt port?: ")

    portQ = portQ.lower()
    if portQ == 'y' or portQ == "yes":
        port = raw_input("Okay, which port?: ")
    
    needShell = raw_input("Do you need a shell to look around?: ")
    needShell = needShell.lower()

    if needShell == 'y' or needShell == "yes":
        if portQ == 'y' or portQ == "yes":
            os.system("ssh -p" + port + " " + scpTarget)
        else:
            os.system("ssh " + scpTarget)

    fileNeeded = raw_input("Enter the file you want: ")

    whereGo = raw_input("Where should I put it?: ")

    if portQ == "y" or portQ == "yes":
        os.system("scp -p" + port + " " + scpTarget + ":" + fileNeeded + " " + whereGo)

    else:
        os.system("scp " + scpTarget + ":" + fileNeeded + " "  + whereGo)
    again = raw_input("Need to go again?(y/n): ")
    again = again.lower()
    print "Bye"
