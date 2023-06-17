Port Scanner

This Python script is a basic port scanner that allows you to scan a range of ports on a target IP address to check for open ports. It utilizes the os, sys, and socket modules for network operations and the datetime module for displaying the current time.
Prerequisites

Before running the script, make sure you have Python 3.x installed on your system.
Usage

    Open a terminal or command prompt.

    Navigate to the directory where the script is saved.

    Run the script using the following command:

    python3 port_scanner.py
    
    The script will prompt you to enter the target IP address you want to scan. Provide a valid IP address and press Enter.

    The scanner will display a header with the target IP address and the current time.

    It will then scan a range of ports (from 50 to 85) on the target IP address.

    For each port, it will attempt to establish a connection. If the port is open, it will print a message indicating that the port is open.

    After scanning all the ports, the script will handle keyboard interruption or socket errors gracefully, displaying appropriate error messages and exiting the program if necessary.

Explanation

The script begins by importing the necessary modules: os, sys, socket, and datetime.

A function called ping_ip is defined to execute the ping command using the os.system method. It takes an IP address as an argument and checks the response code to determine if the ping was successful or not.

The user is prompted to enter an IP address to scan. The script expects a valid IP address as input.

The script checks if the IP address is provided as a command-line argument using sys.argv. If it is provided, it resolves the IP address using socket.gethostbyname() and assigns it to the target variable. Otherwise, it displays an error message and exits the program.

After printing a header with the target IP address and the current time, the script enters a try-except block. It calls the ping_ip function to ping the target IP address and prints a success or failure message.

Next, the script iterates over a range of ports (from 50 to 85) and attempts to establish a connection using socket.socket() and socket.connect_ex(). If the connection attempt returns a result of 0, it means the port is open, and a message is printed to indicate that the port is open.

The script closes the socket after each connection attempt. It also handles keyboard interruption and socket errors, printing appropriate error messages and exiting the program if necessary.
Conclusion

The port scanner script provides a basic functionality to scan a range of ports on a target IP address. You can modify the code to customize the port range or add additional features according to your requirements. Remember to use this tool responsibly and ensure you have proper authorization before scanning any network or system.
