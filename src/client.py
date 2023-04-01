import socket

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect(("127.0.0.1", 10000))

try:
    clientSocket.send('Hello! I"m client'.encode())
    msg = clientSocket.recv(1024)
    print(msg.decode())

finally:
    print('closing socket')
    clientSocket.close()
