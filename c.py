import socket
import json

class NewsClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.client_socket = None

