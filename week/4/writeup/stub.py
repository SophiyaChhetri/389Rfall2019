"""
    Use the same techniques such as (but not limited to):
        1) Sockets
        2) File I/O
        3) raw_input()

    from the OSINT HW to complete this assignment. Good luck!
"""

import socket

host = "157.230.179.99" # IP address here
port = 1337 # Port here

def execute_cmd(cmd):
    """
        Sockets: https://docs.python.org/3/library/socket.html
        How to use the socket s:

            # Establish socket connection
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host, port))

            Reading:

                data = s.recv(1024)     # Receives 1024 bytes from IP/Port
                print(data)             # Prints data

            Sending:

                s.send("something to send\n")   # Send a newline \n at the end of your command
    """
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, port))
	data = s.recv(1024)     # Receives 1024 bytes from IP/Port
	print(data)             # Prints data

	if(cmd == "shell")
		s.send("something to send\n") 
    	print("shell")
	elif(cmd == "pull")
		s.send("something to send\n") 
    	print("pull")

	elif(cmd == "help")
		s.send("something to send\n") 
    	print("help")
	elif(cmd == "quit")
		s.send("something to send\n") 
    	print("quit")


if __name__ == '__main__':
    execute_cmd(cmd)