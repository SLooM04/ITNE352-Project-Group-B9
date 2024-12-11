import socket
import threading
import json
import requests


HOST = '127.0.0.1'
PORT = 12346
API_KEY = '7e298875cb264cee89ac50bb42c59a83'
BASE_URL = 'https://newsapi.org/v2/'

class NewsServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        print("The server is ready for connection")

    