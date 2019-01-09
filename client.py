import socket

mysocket=socket.socket()
mysocket.connect(('localhost',4444))
while True:
    msg = mysocket.recv(1024)
    print("Message from server: "+msg)
    data=raw_input("Enter data: ")
    mysocket.send(data)
    if msg=='bye' or data=='bye':
        break
    
