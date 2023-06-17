import os
import sys
import socket
from datetime import datetime

 # Execute the ping command
def ping_ip(ip_address):
    response = os.system("ping -c 4 " + ip_address)
    if response == 0:
        print("Ping successful!")
    else:
        print("Ping failed!")
        
# Prompt the user to enter an IP address
ip_address = input("Enter an IP address: ")

if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])
else:
    print("Invalid amount of arguments.")
    print("Syntax : python3 scanner.py <ip>")
    sys.exit()

print("-" * 50)
print("Scanning target " + target)
print("Time started: " + str(datetime.now()))
print("-" * 50)

try:
    ping_ip(target)  # Ping the target IP address
    for port in range(50,85):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port)) # Attempt to connect to the port
        if result == 0:
            print(f"Port {port} is open")
        s.close()

except KeyboardInterrupt:
    print("\nExiting program.")
    sys.exit()

except socket.gaierror:
    print("Hostname could not be resolved.")

except socket.error:
    print("Could not connect to the server.")
    sys.exit()