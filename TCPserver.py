#Thomas Hawkins
#import socket module 
from socket import * 
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM) 
serverSocket.setsockopt(SOL_SOCKET,SO_REUSEADDR, 1) #prevents a windows machine from putting a delay on a port after it closes
serverSocket.bind(('', serverPort)) #opens a socket connection on port 80 using socket.gethostname() this binds the socket to a public host
serverSocket.listen(5) #queue up to 5 connection requests on serverSocket

while True: 
        #Establish the connection 
        print 'Ready to serve...' 
        connectionSocket, addr = serverSocket.accept()
        try:
                data = []
                message = connectionSocket.recv(1024)
                filename = message.split(" ")[1] 
                f = open(filename[1:])
                responseLine = "HTTP/1.1 200 OK"
                headerLine = "Connection: close"
                for line in f:
                        data.append(line)
                
                outputdata = [responseLine, headerLine]
                for i in range (0, len(data)):
                        outputdata.append(data[i])
                length = len(outputdata)
                outputdata.insert(0, str(length))
                for i in range(0, len(outputdata)):
                        connectionSocket.send(outputdata[i])
                        connectionSocket.send("\r\n")
                # Close the client connection socket
                connectionSocket.close() 

        except IOError:
                connectionSocket.send("2")
                connectionSocket.send("\r\n")
                connectionSocket.send("404 Error: File Not Found")
        connectionSocket.close()

serverSocket.close() 
