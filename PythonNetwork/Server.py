#!/usr/bin/python

import socket

###
### Socket programming Python tutorial
###

s = socket.socket()
host = socket.gethostname()
port = 12345
s.bind((host, port))

s.listen(5)

listening = True
while listening:
    c, addr = s.accept()                # Wait for client connection
    print 'Got connection from', addr
    c.send('Thank you for connecting')
    c.close()                            # Close the connection 
    listening = False  
