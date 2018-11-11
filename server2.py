#!/usr/bin/env python3

import socket
import time, sys
from threading import Thread
import urllib.request
import select


def main():
	# Non-reserved port.
	port = 5000
	# Bind to all available interfaces.
	host = 'localhost'
	
	print("Starting server on port", port)

	print('Your ip is :' , urllib.request.urlopen('https://ident.me/').read().decode('utf8'))

	with socket.socket() as mySocket:
		
		# Set the socket to non-blocking
		mySocket.setblocking(0)

		# This lets us reuse the reuse a socket quickly in case we're debugging
		# and the socket doesn't get closed on a crash or something.
		mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

		# Bind the socket to our address and port.
		mySocket.bind((host,port))

		max_connections = 100
#		max_connections = int(input("How many people are watching with you?"))

		# Set the maximum number of clients that can connect.
		mySocket.listen(max_connections)

		# The set of input sockets we block on with select in
		# the input thread.
		inputs = [mySocket]

		# Dict mapping connections to users.
		userdict = {}

		# In reality we would launch another thread but
		# let's just call the function for now.
		input_thread(mySocket, inputs, userdict)

"""
		
	

		
	peers = []
	try:
		while connections > 0:
			conn, addr = mySocket.accept()
			peers.append(user(conn, addr))
			print ("Connection from: " , str(addr))
			connections -= 1
	except KeyboardInterrupt:
		pass
	
	
	print("All clients have connected. You may now proceed")
	
	for peer in peers:
		t = Thread(target=listen, args = (peer,peers,))
		t.start()
	
	while True:
		data = input(" -> ")
		for client in peers:
			client.get_connection().send(data.encode())
		if data.upper() == 'PLAY' or data.upper() == 'STOP':
			time.sleep(0.1)
				

	mySocket.close()
"""

# This thread will handle inputs from clients.
# mySocket is the server's socket object.
# inputs is all the sockets (including mySocket)
# userdict maps sockets to users.
def input_thread(mySocket, inputs, userdict):
	while True:
		# select.select blocks on all the sockets in inputs, and returns
		# lists of sockets you can read from and write to.
		readable, writable, exceptional = select.select(inputs, [], inputs)

		# Since this is the input thread, we check readable sockets.
		for s in readable:
			# If the server socket is readable, we have a new connection.
			if s is mySocket:
				# Accept the new connection.
				conn, addr = s.accept()

				print("New connection from", addr)

				# The new user's socket needs to also be
				# non-blocking to work with select.
				conn.setblocking(0)

				userdict[conn] = user(conn, addr)

				# Put the new user's socket inside the input list.
				inputs.append(conn)

			# s is a client that's already connected.
			else:
				# First byte is the command byte.
				# Commands:
				# 1 - Username login
				# 2 - Send message
				data = s.recv(1)
				if not data:
					# If data is empty, the socket is closed.
					print("Closing connection", s)

					# We need to clean up our variables.
					inputs.remove(s)
					del userdict[s]
					s.close()
					continue
				if data[0] == 1:
					# Get the username.
					username = s.recv(1024).decode()
					print("Connection", s, "assigned username", username)
					# Set the user's name.
					userdict[s].set_name(username)
				else:
					# Get the message
					data = s.recv(4096)
					# Look up the user's name.
					username = userdict[s].get_name()
					print("Received", data.decode(), "from", username + ".")
					# Send username: data
					to_send = (username + ": " + data.decode()).encode()
					s.send(to_send)



"""
def listen(peer, peers):
	while True:
		
		print("Waiting for message from clients.")
		data = peer.get_connection().recv(1024).decode()
		print ('Received from client: ' + data)
		for client in peers:
			client.get_connection().send(data.encode())
		if data.upper() == 'PLAY' or data.upper() == 'STOP':
			time.sleep(0.1)
"""
					
		  
			
class user:
	
	def __init__(self, conn, addr):
		self.connection = conn
		self.address = addr
		self.name = ""
	
	def set_name(self, name):
		self.name = name

	def get_name(self):
		return self.name

	def get_connection(self):
		return self.connection
		
	def get_address(self):
		return self.address
		
		
if __name__ == '__main__':
	main()
