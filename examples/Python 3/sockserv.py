################################################################
## Multithreaded Socket Server                                ##
## @Author: Aaron Earl                                        ##
##                                                            ##
## This program demonstrates a simple socket server that uses ##
## the built in multithreading module. This allows a greater  ##
## number of connections per second than would otherwise be   ##
## possible with a standard socket connector. Since           ##
## Multithreading is better at IO related tasks it is great   ##
## for dealing with programs that return responses across     ##
## a network connection to multiple hosts. Otherwise          ##
## the program would only be able to process one connection   ##
## at a time before closing.                                  ##
##                                                            ##
## Special Notes: Linux has a maximum limit of 32000 sockets  ##
## that can be active. If too many connections happen at once ##
## the linux socket buffer will fill up and crash the OS. You ##
## could del the socket after supposed termination but this   ##
## leads to several sockets prematurely closing if too many   ##
## connections are waiting for a message return.              ##
##                                                            ##
## There are also some limiting factors on resources due to   ##
## the global interpreter lock. If the program has to use     ##
## the same set of resources, the resources will be locked    ##
## until the current thread is done with them. If not or      ##
## each of the connections are unique, this will not be       ##
## a problem.                                                 ##
################################################################

# Import the needed libraries
import socket
import threading

# Variables to store socket info
host = ''
port = 50000
connectionSevered=0

# Class definition calling the thread constructor
class client(threading.Thread):
    def __init__(self, conn):
        super(client, self).__init__()
        self.conn = conn
        self.data = ""
    # Override constructor run method
    def run(self):
        while True:
            self.data = self.data + self.conn.recv(1024)
            if self.data.endswith(u"\r\n"):
                print(self.data)
                self.data = ""
    # Return the input message
    def send_msg(self,msg):
        self.conn.send(msg)

    # Close the socket
    def close(self):
        self.conn.close()

# Bind and listen with error handling 
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host,port))
    s.listen(5)
except socket.error:
    print('Failed to create socket')
    sys.exit()

# Message prints that the socket is litening and the port number
# its listening on
print('[+] Listening for connections on port: {0}'.format(port))

# Accept the connection and return the message
conn, address = s.accept()
c = client(conn)
c.start()
print('[+] Client connected: {0}'.format(address[0]))
c.send_msg(u"\r\n")
print("connectionSevered:{0}".format(connectionSevered)) 
while (connectionSevered==0):
    try:
        response = raw_input()  
        c.send_msg(response + u"\r\n")
    except:
        c.close()