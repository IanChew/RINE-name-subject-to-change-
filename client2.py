#!/usr/bin/env python3

import socket
import time, sys
import threading

# Blocks on input from the server.
def input_thread(mySocket):
	while True:
#		print("Waiting for message from server...")
		data = mySocket.recv(1024).decode()
		print('Received from server:', data)


def Main():
	host = input("what is the host ip?\n")
	port = 5000
	
	with socket.socket() as mySocket:
		mySocket.connect((host,port))
		print("Connected to the server at", host)

		# Start input_thread in a new thread.
		ithread = threading.Thread(target=input_thread, args=(mySocket,))
		# Our thread dies when the main thread exits.
		ithread.daemon = True
		# Start the input thread.
		ithread.start()
	
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
			send = message.upper()
			print("sending:", str(send))
			mySocket.send(send.encode())


		
if __name__ == '__main__':
	Main()
