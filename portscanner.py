import socket
import subprocess
import sys
import getopt
import argparse
from datetime import datetime

#Blank your screen
subprocess.call('clear', shell=True)

#argumentList = sys.argv[1:]

#Options
#options = "hr:o:"

#long Options
#longOptions = ["help", "range=", "output="]

#outputFile = None

parser = argparse.ArgumentParser(prog='portscanner', description="Home grown port scanner.")

#IP Address
parser.add_argument('IP Address', 
                    metavar='IP',
                    help='IP address, IP range, or CIDR range to be scanned.',
                    nargs='+')

#Output Flag
parser.add_argument('-o', '--output',
                    help='File name to write output to',
                    nargs=1,
                    type=str,
                    dest='ofile')

#Verbosity Flag
parser.add_argument('-v', '--verbose',
                    action='count',
                    default=0,
                    help='Increases Verbosity. Max level 5.',
                    dest='verbose')

#Selecting Port Range
parser.add_argument('-r', '--range',
                    nargs=2, 
                    default=[1-5000],
                    type=int,
                    help='Define the range of ports to scan. Default is 1-5000 \n If you need to scan specific ports, see the -sp option',
                    dest='range')

#Scan Specific Ports
parser.add_argument('-sp', '--s.ports'
                    nargs='+'
                    type=int,
                    help='Choose specific ports to scan. ',
                    dest='s.port')                    




#try:
    #Parsing Arguments
 #   arguments, values = getopt.getopt(argumentList, options, longOptions)

    #checking each argument
  #  for currentArgument, currentValue in arguments:
   #     if currentArgument in ("-h", "--help"):
    #        print ("Displaying Help")
     #       sys.exit()
      #  elif currentArgument in ("-r", "--range"):
       #     print (("Port Range Selected (% s)") % currentValue)
        #elif currentArgument in ("-o", "--output"):
         #   print (("Output file set as %s") % currentValue)
          #  outputFile = currentValue

#except getopt.error as err:
 #   #output error, and return with an error code
  #  print (str(err))

#Ask for input

print ("Welcome to Patzy's Port Scanner")
scanServer = input("Enter a remote host to scan: ")

scanServerIP = socket.gethostbyname(scanServer)


#Print a nice banner with information on which host we are about to scan
print ("_" * 60)
print ("Please wait, scanning remote host", scanServerIP)
print ("_" * 60)

#Check the date and time the scan was started
t1 = datetime.now()

#Using the range function to specify portsscan
#Also we will do error handling

try:
        for port in range (1,5000):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((scanServerIP, port))
            if result == 0:
                print ("Port {}:    Open".format(port) + " Protocol - " + socket.getservbyport(port))
            sock.close()

except KeyboardInterrupt:
    print ("Aborting Scan")
    sys.exit()

except socket.gaierror:
    print ("Hostname could not be resolved. Exiting")
    sys.exit()

except socket.error:
    print ("Couldn't connect to server")
    sys.exit()

#Checking time again
t2 = datetime.now()

#Calculate the difference in time to know how long the scan took
total = t2 - t1

#Printingg the information on the screen
print ('Scanning Completed in: ', total)
     