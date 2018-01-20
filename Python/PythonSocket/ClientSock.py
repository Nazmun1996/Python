import socket

my_sock = socket.socket()

port = 5000

#IP of the local computer 
my_sock.connect(('127.0.0.1', port))

#Recieve Data
print my_sock.recv(1024)


#Closing Connection
print('Data Recieved')
my_sock.close()
