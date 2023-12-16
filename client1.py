import socket
import threading


def recv_msgandprint(c_socket):
    while True:
        msg = c_socket.recv(1024)
        print(msg.decode())


host = '127.0.0.1'
port = 12345
clientSocket2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket2.connect((host, port))

while True:
    threading.Thread(target=recv_msgandprint, args=(clientSocket2,)).start()
    message1 = input()
    clientSocket2.send(message1.encode())

