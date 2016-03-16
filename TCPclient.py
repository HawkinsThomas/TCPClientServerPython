#Thomas Hawkins
#1148953


from socket import *
serverPort = 12000
serverName = "192.168.1.19"
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
clientSocket.setsockopt(SOL_SOCKET,SO_REUSEADDR, 1)
message = "GET /page.html HTTP/1.1"
clientSocket.send(message)
reply1 = (clientSocket.recv(2048))
reply = ""
for i in range (0, int(reply1)+1):
	reply = reply + clientSocket.recv(2048)

print reply
clientSocket.close()
