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

    def fetch_news(self, endpoint, params=None):
        
        try:
            if not params:
                params = {}
            params['apiKey'] = API_KEY
            params['pageSize'] = 15
            url = f"{BASE_URL}{endpoint}"
            response = requests.get(url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            return {"error": f"Failed to fetch data: {e}"}

    def handle_client(self, client_socket, client_address):
        
        print(f"Connected to {client_address}")
        try:
            client_name = client_socket.recv(1024).decode()
            print(f"Client Name: {client_name}")
            client_socket.send(f"Welcome, {client_name}!".encode())

            while True:
                client_request = client_socket.recv(1024).decode().strip().lower()

                if not client_request or client_request == "quit":
                    print(f"Client {client_name} disconnected.")
                    break

                if client_request.startswith("headlines"):
                    print(f"[Request from {client_name}] headlines")
                    params = self.parse_request(client_request)
                    news = self.fetch_news("top-headlines", params)
                    self.save_to_json(client_name, "headlines", news)
                    client_socket.send(json.dumps(news).encode())

                elif client_request.startswith("sources"):
                    print(f"[Request from {client_name}] sources")
                    params = self.parse_request(client_request)
                    sources = self.fetch_news("sources", params)
                    self.save_to_json(client_name, "sources", sources)
                    client_socket.send(json.dumps(sources).encode())

                else:
                    client_socket.send("Invalid request. Try 'headlines', 'sources', or 'quit'.".encode())

        except Exception as e:
            print(f"Error with client {client_address}: {e}")
        finally:
            client_socket.close()

    def parse_request(self, request):
        
        params = {}
        if "q=" in request:
            params['q'] = request.split("q=")[1]
        elif "category=" in request:
            params['category'] = request.split("category=")[1]
        elif "country=" in request:
            params['country'] = request.split("country=")[1]
        elif "language=" in request:
            params['language'] = request.split("language=")[1]
        else:
            params['language'] = 'en'  # Default parameter
        return params

    def save_to_json(self, client_name, option, data):
        
        filename = f"{client_name}_{option}_B9.json"
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)

   