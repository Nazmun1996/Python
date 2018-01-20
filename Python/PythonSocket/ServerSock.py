import socket

my_sock = socket.socket()
port = 5000

my_sock.bind(('', port))

my_sock.listen(10)

while True:

   # Establish connection with client.
   c, addr = my_sock.accept()
   print 'Connected To:', addr


   c.send('Closing Connection')

   # Close the connection 
   c.close()
