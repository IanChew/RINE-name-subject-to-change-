#!/usr/bin/env python3

import socket
import keyboard
import time, keyboard, sys

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
                    if data.upper() == 'PLAY' or data.upper() == 'STOP':
                        keyboard.SendInput(keyboard.Keyboard(keyboard.VK_CONTROL))
                        time.sleep(0.1)
                        keyboard.SendInput(keyboard.Keyboard(keyboard.VK_SPACE))
                        keyboard.SendInput(keyboard.Keyboard(keyboard.VK_CONTROL, keyboard.KEYEVENTF_KEYUP),
                        keyboard.Keyboard(keyboard.VK_SPACE, keyboard.KEYEVENTF_KEYUP))
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
