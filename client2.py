#!/usr/bin/env python3

import socket
import time, sys
import threading
import struct
import readline

# Blocks on input from the server.
def input_thread(mySocket):
	while True:
		# First byte is the command byte.
		# 2 - Receive message
		# 3 - Receive file.
		data = mySocket.recv(1)
		if data[0] == 2:
			# Read a message.
			data = mySocket.recv(1024).decode()
			buffer = readline.get_line_buffer()
			if len(buffer) != 0:
				print("\r" + data + "\n" + buffer , end='')
			else:
				print(data)
#			print('Received from server:', data)
		elif data[0] == 3:
			# We're getting a file.
			# First we get 1 byte denoting the
			# username of the person that sent it.
			usersize = mySocket.recv(1)[0]
			# Then we get usersize bytes containing the username.
			username = mySocket.recv(usersize).decode()

			# First we get 2 bytes denoting the
			# file name size.
			fname_size_bytes = mySocket.recv(2)
			# , unpacks the 1-tuple
			fname_size, = struct.unpack("H", fname_size_bytes)
			fname = mySocket.recv(fname_size).decode()
			
			# Next we get 8 bytes denoting the
			# file size.
			file_size_bytes = mySocket.recv(8)
			file_size, = struct.unpack("Q", file_size_bytes)
			# Call recvall because the file might be big.
			file_bytes = recvall(mySocket, file_size)

			print("Received file", fname, "of size", file_size, "from",
			      username)

			# Write out the file to save it (dangerous,
			# should prompt the user in the future).
			# "xb" means open the file in binary mode
			# and fail if the file already exists.
			# This should make it slightly safer.
			try:
				with open(fname, "xb") as fp:
					fp.write(file_bytes)
			except FileExistsError as e:
				print("Error: File", fname, "already exists")
				print("No file written.")



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

		while True:
			print("To enter messaging mode, enter m.")
			print("To attach a file, enter a")
			print("To quit, hit q")
			mode = input()
			if mode == 'm':
				messaging_mode(mySocket)
			elif mode == 'a':
				attach_file(mySocket)
			elif mode == 'q':
				# End the program.
				break;

# While in messaging mode, the output thread executes here.
def messaging_mode(mySocket):
	try:
		print("Messaging mode entered.")
		print("To exit messaging mode, press CRTL + C.")
		print("To send messages, simply type and hit enter.")
		while True:
			message = input() #"message (q to quit)\n")
#			if message == 'q':
#				break
#			print("sending:", str(message))
			# If the first byte is 0x02, we're sending a message.
			command = b'\x02'
			to_send = command + message.encode()
			mySocket.send(to_send)
	except KeyboardInterrupt:
		pass
	
# Called when the user tries to send (attach) a file.
def attach_file(mySocket):
	# Make sure the filename isn't empty.
	fname = ""
	while not fname:
		fname = input("Enter name of file to attach:\n")

	try:
		# Open the file in binary mode.
		with open(fname, "rb") as fp:
			data = fp.read()

	except FileNotFoundError as e:
		print("Error: Could not find file", fname)
		# Do not continue with attaching a file.
		return

	# Now data contains the bytes of the file.
	# We will not build up a byte string containg what we
	# need to send.

	# Command byte 3 means we're sending a file.
	command = b'\x03'
	# Binary filename.
	bfname = fname.encode()
	# Binary filename length, in a bytes string of size 2.
	bfname_size = struct.pack("H", len(bfname))
	# File size, in a bytes string of size 8.
	fsize = struct.pack("Q", len(data))

	# The protocol is that we send the command byte,
	# then the file name's length (2 bytes), then the
	# file name, then the file length (8 bytes),
	# then the file's actual contents.
	to_send = command + bfname_size + bfname + fsize + data

	mySocket.sendall(to_send)


# Keeps calling recv until we get length bytes.
def recvall(sock, length):
	retval = b''
	while (length != 0):
		data = sock.recv(length)
		# Subtract the length read from the remaining length.
		length -= len(data)
		retval += data
	return retval


if __name__ == '__main__':
	Main()
