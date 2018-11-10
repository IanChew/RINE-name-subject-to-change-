#!/usr/bin/env python3

import socket
import time, sys

def Main():
	host = input("what is the host ip?")
	port = 5000
	
	mySocket = socket.socket()
	mySocket.connect((host,port))
	print("Connected to the mainframe. Please wait.")
	
	
	message = ""
	while True:
		try:
			while True:
				print("Waiting for message from server. Press Ctrl + c to send message")
				data = mySocket.recv(1024).decode()
				print ('Received from server: ' + data)
		except KeyboardInterrupt:
			pass
		message = input("message (q to quit)")
		if message == 'q':
			break
		send = message.upper()
		print ("sending: " + str(send))
		mySocket.send(send.encode())
		mySocket.close()

		
if __name__ == '__main__':
	Main()
