import sys
import socket
from datetime import datetime
import pyfiglet

BANNER = pyfiglet.figlet_format("My Port Scanner", font="slant")
print(BANNER)

print("_"*50)

if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])
else :
    print("Invalid number of Arguments")
    
print("Scanning the IP address : "+ target+" at " + str(datetime.now()))
print("_"*50)

#REAL PORT SCANNER CODE STARTS HERE
print("Scanning for port numbers between 1 and 100.....")
print("_"*50)
try:
    for port in range(1,100):
        s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        
        result = s.connect_ex((target,port))
        
        if(result == 0):
            print("The port {} is open".format(port)) 
        else:
            print("The port {} is NOT OPEN".format(port))
        s.close()
            
except KeyboardInterrupt:
    print("KEYBOARD INTERRUPT HAS OCCURED. EXITING THE PROGRAM....")
    sys.exit()

except socket.gaierror :
    print("Hostname Could not be resolved")
    sys.exit()
    
except socket.error:
    print("SERVER NOT RESPONDING....")
    sys.exit()
    
print("_"*50)

print("\n Scanning ended at "+ str(datetime.now()))

print("_"*50)
        