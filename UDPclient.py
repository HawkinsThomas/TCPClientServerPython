from socket import *
servername  = 'hostname'
serverPort = 12000
clientSocket = socket(socket.AF_INET, socket.SOCK_DGRAM) #indicates address field is using IPV4, sets socket to be UDP socket
message = "hello world"
clientSocket.sendto(message,servername, serverPort)
reply, serverAddress = clientSocket.recvfrom(2048)
clientsSocket.close()