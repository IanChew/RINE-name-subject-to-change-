#!/usr/bin/env python3

import socket
import time, sys
from threading import Thread
import urllib.request

def Main():
    port = 5000
    host = socket.gethostname()
    
    mySocket = socket.socket()
    
    mySocket.bind((host,port))
    print('your ip is :' , urllib.request.urlopen('https://ident.me/').read().decode('utf8'))
    connections = int(input("How many people are watching with you?"))
    mySocket.listen(connections)
    
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
def listen(peer, peers):
    while True:
        
        print("Waiting for message from clients.")
        data = peer.get_connection().recv(1024).decode()
        print ('Received from client: ' + data)
        for client in peers:
            client.get_connection().send(data.encode())
        if data.upper() == 'PLAY' or data.upper() == 'STOP':
            time.sleep(0.1)
                    
          
            
class user:
    
    def __init__(self, conn, addr):
        self.connection = conn
        self.address = addr
    
    def get_connection(self):
        return self.connection
        
    def get_address(self):
        return self.address
        
        
if __name__ == '__main__':
    Main()
