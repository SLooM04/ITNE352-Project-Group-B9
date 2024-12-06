#import socket library 
import socket

#assign host and port num
host=""
port=""

#Establish a TCP connection 
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as f:
    f.connect((host,port))
    
    f.send("Hello server")
    data = f.recv(1024)

