##################################################################
## Socket server demo                                           ##
## @Author Aaron Earl                                           ##
##                                                              ##
## This script is a demo of a simple socket server.             ##
## You can use the linux system function netcat localhost 9900  ##
## to contact the server. You will have to type a message and   ##
## it will return an thank you message back after hitting enter.##
################################################################## 

# Import the socket Library
import socket               

########################################################
## Create a socket object                             ##
## The AF_INTET deines which socket family we will    ##
## use the protocol. This one is used for IPV4 and    ## 
## represents the IP as a string.                     ##
## The SOCK_STREAM represents the acutual protocol    ##
## to use for the connection.                         ##
## You can review the Python docs here                ##
## https://docs.python.org/3/library/socket.html      ##
########################################################
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         
print("Socket successfully created")

#####################################################
## This line reserves a port on your computer.     ##
## In this case it is 9900 but it can be anything  ##
## less than 32000 and usually greater than 4000.  ##
#####################################################
port = 9900                

########################################################
## Next bind to the port.                             ##
## I have not typed any ip in the ip field instead I  ##
## have input 'localhost' or the loopback IP          ##
## this will make the server listen to requests       ##
## coming from other computers on the network         ##
########################################################
s.bind(('localhost', port))        
print("socket binded to %s" %(port))

################################################
## Put the socket into listening mode.        ##
## The 5 represents the backlog or the amount ##
## of connections allowed at a time.          ##
## This is system dependednt, the number may  ##
## be more or less depending on your system   ##
################################################
s.listen(5)     
print("socket is listening")            

#############################################
## A forever loop until we interrupt it or ## 
## an error occurs                         ##
#############################################
while(True):
   # Establish connection with client.
   c, addr = s.accept()     
   data = c.recv(1024).decode('utf8')
   print("Got connection from" + str(addr) + " " + data + "\n")

   # Send a thank you message to the client.
   msg = "Thank you for connecting\n"
   byte_msg = msg.encode()
   c.send(byte_msg)
   # Close the connection with the client
   c.close() 