#   Port Scanner - Written by Patzy
#   Last Update - 26/11/2022
#
#   This scanner was used to teach myself python and understand the workings
#   behind the scenes. The code has been finalized and tested for version 1.0
#   and will be the base for all further changes. 
#
#   This code was written for educational purposes only. Please do not use this code
#   on networks/hosts that you do not own or do not have written permission to use. 
#
import argparse
import socket
import subprocess
import sys
from datetime import datetime

#Variables

version = "V 1.0"
top20 = [21,22,23,25,53,80,110,111,135,139,143,443,445,993,995,1723,3306,3389,5900,8080]
top200 = [1,3,7,9,13,17,19,21,22,23,25,26,37,53,79,80,81,82,88,100,106,110,111,113,119,135,139,143,144,179,199,254,255,280,311,389,427,443,444,445,464,465,497,513,514,515,543,544,548,554,587,593,625,631,636,646,787,808,873,902,990,993,995,1000,1022,1024,1025,1026,1027,1028,1029,1030,1031,1032,1033,1035,1036,1037,1038,1039,1040,1041,1044,1048,1049,1050,1053,1054,1056,1058,1059,1064,1065,1066,1069,1071,1074,1080,1110,1234,1433,1494,1521,1720,1723,1755,1761,1801,1900,1935,1998,2000,2001,2002,2003,2005,2049,2103,2105,2107,2121,2161,2301,2383,2401,2601,2717,2869,2967,3000,3001,3128,3268,3306,3389,3689,3690,3703,3986,4000,4001,4045,4899,5000,5001,5003,5009,5050,5051,5060,5101,5120,5190,5357,5432,5555,5631,5666,5800,5900,5901,6000,6001,6002,6004,6112,6646,6666,7000,7070,7937,7938,8000,8002,8008,8009,8010,8031,8080,8081,8443,8888,9000,9001,9090,9100,9102,9999,10000,10001,10010,32768,32771,49152,49153,49154,49155,49156,49157,50000]
openPorts = []
errorPorts = []

#File Output Class

def WriteFile (outfile, openPorts, errors, time):
    outputFile = open(outfile, "a")
    for line in openPorts:
        outputFile.write(str(line) + "\n")
    outputFile.write("_" * 60)
    for line in errors:
        outputFile.write(str(line) + "\n")   
    outputFile.write("_" * 60)
    outputFile.write('Scan Completed in: ', time)
    outputFile.write("_" * 60)
    outputFile.write("Thank you for using Patzy's Port Scanner {}".format(version))
    outputFile.close()
    print ("Scan results saved in {}.".format(outfile))

#Scan Class

def Scan(address, ports):

    try:
        for port in ports:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((address, port))
            
            try:
                if result == 0:
                    print ("Port {}:    Open".format(port) + " Protocol - " + socket.getservbyport(port))
                    openPorts.append("Port {}:    Open".format(port) + " Protocol - " + socket.getservbyport(port))
                else: 
                    print ("Port {}:    Closed/Filtered".format(port))
                sock.close()
            except socket.error:    #This exception is here instead of later to continue scanning if the error occurs. 
                print ("Error connecting to port {}".format(port))
                errorPorts.append("Port {}: Error connecting".format(port))
                pass

    except KeyboardInterrupt:
        print ("Aborting Scan")
        sys.exit()

    except socket.gaierror:
        print ("Hostname could not be resolved. Exiting")
        sys.exit()



#Blank your screen
subprocess.call('clear', shell=True)

#Setting up parser for command line argument input. 
parser = argparse.ArgumentParser(prog='portscanner', 
                                description="Home grown port scanner.",
                                epilog='PortScanner {} Written by Patzy'.format(version))

#IP Address
parser.add_argument("address", help='IP address, IP range, or CIDR range to be scanned.')

#Output Flag
parser.add_argument('-o', '--output',
                    help='File path to write output to',
                    nargs=1,
                    type=str)

#Fast Scan Flag
parser.add_argument('-f', '--fast',
                    action='store_true',
                    help='Fast scan. Only scanning the top 20 common ports',
                    dest='fast')

#Selecting Port Range
parser.add_argument('-r', '--range',
                    nargs=2, 
                    default= [range(1,5000)],
                    type=int,
                    help='Define the range of ports to scan. Default is 1-5000 \n If you need to scan specific ports, see the -sp option',
                    dest='range')

#Scan Specific Ports
parser.add_argument('-sp', '--s_ports',
                    nargs='+',
                    type=int,
                    help='Choose specific ports to scan. ')                    

args = parser.parse_args()
scanServerIP = socket.gethostbyname(args.address)

#Print a nice banner with information on which host we are about to scan
print ("Welcome to Patzy's Port Scanner {}".format(version))
print ("_" * 60)
print ("Please wait, scanning remote host", scanServerIP)
print ("_" * 60)

#Check the date and time the scan was started
t1 = datetime.now()

#Scanning for Specific Ports based on input
if args.s_ports:
   Scan(scanServerIP, args.s_ports)
elif args.range == True:
    Scan(scanServerIP, range(args.range[0], args.range[1]+1))
elif args.fast == True:
    Scan(scanServerIP, top20)
else:
    Scan(scanServerIP, top200)

#Checking time again
t2 = datetime.now()

#Calculate the difference in time to know how long the scan took
total = t2 - t1

#Printing the information on the screen

print ("_" * 60)
print ("Scan Results")
print ('Scanning Completed in: ', total)
print ("_" * 60)
for line in openPorts:
    print (line)
print("_" * 60)
for line in errorPorts:
    print (line)
if args.output:
    WriteFile(args.output[0], openPorts, errorPorts, total)
