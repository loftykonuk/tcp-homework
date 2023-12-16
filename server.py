import socket
import threading


def recvmsgandsend(cs):
    while True:
        a = cs.recv(1024)
        for _client in clients:
            _client.send(a)


host = '127.0.0.1'
port = 12345
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((host, port))
serverSocket.listen(10)

clients = []

while True:
    clientSocket, clientAddress = serverSocket.accept()
    clients.append(clientSocket)
    threading.Thread(target=recvmsgandsend, args=(clientSocket,)).start()

