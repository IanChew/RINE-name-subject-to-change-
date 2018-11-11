#!/usr/bin/env python3

import socket
import time, sys
import threading

# Blocks on input from the server.
def input_thread(mySocket):
	while True:
#		print("Waiting for message from server...")
		data = mySocket.recv(1024).decode()
		print(data)
#		print('Received from server:', data)


def Main():
	host = input("What is the host ip?\n")
	port = 25505
	
	with socket.socket() as mySocket:
		mySocket.connect((host,port))
		print("Connected to the server at", host)

		# Start input_thread in a new thread.
		ithread = threading.Thread(target=input_thread, args=(mySocket,))
		# Our thread dies when the main thread exits.
		ithread.daemon = True
		# Start the input thread.
		ithread.start()
	
		username = ""
		# Make sure we don't send an empty username.
		while not username:
			username = input("What is your username?\n")

		# If the first byte is 0x01, we're sending a username login.
		command = b'\x01'
		to_send = command + username.encode()

		# Send the login command.
		mySocket.send(to_send)


#		message = ""
		while True:
#			try:
#				while True:
#					print("Waiting for message from server. Press Ctrl + c to send message")
#					data = mySocket.recv(1024).decode()
#					print ('Received from server: ' + data)
#			except KeyboardInterrupt:
#				pass
			message = input() #"message (q to quit)\n")
			if message == 'q':
				break
			send = message
#			print("sending:", str(send))
			# If the first byte is 0x02, we're sending a message.
			command = b'\x02'
			to_send = command + send.encode()
			mySocket.send(to_send)


		
if __name__ == '__main__':
	Main()
