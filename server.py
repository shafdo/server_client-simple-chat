

import socket

mysocket = socket.socket()
mysocket.bind(('',4444))
mysocket.listen(1)

channel,details=mysocket.accept()
print("Connection established: ",details)
while True:
    data=raw_input("Enter data: ")
    channel.send(data)
    msg=channel.recv(1024)
    print("Message from client: "+msg)
    if data=="bye" or msg=='bye':
        channel.close()
        exit(0)

	
    
    



