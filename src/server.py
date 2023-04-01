import socket

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(('127.0.0.1', 10000))
serverSocket.listen(5)
clientSocket, addr = serverSocket.accept()

print(clientSocket)

while True:
    data = clientSocket.recv(1024)
    if data:
        clientSocket.sendall(data)
    else:
        break

clientSocket.close()
serverSocket.close()
