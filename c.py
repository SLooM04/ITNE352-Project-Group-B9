import socket
import json

class NewsClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.client_socket = None

    def start(self):
        if not self.client_socket:
            print("Socket is not connected.")
            return

        username = input("Enter your name: ")
        self.client_socket.send(username.encode())
        print(self.client_socket.recv(1024).decode())