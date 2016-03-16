from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))

print "Ready to serve"
while True:  
	message, clientAddress = serverSocket.recvfrom(2048)
	reply = 'fuck your' + message
	serverSocket.sendto(reply, clientAddress)