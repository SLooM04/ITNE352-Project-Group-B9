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
        while True:
            try:
                print("\nMain Menu:")
                print("1 - Search Headlines")
                print("2 - List Sources")
                print("3 - Quit")

                choice = input("Choose an option: ").strip()

                if choice == "1":
                    self.headlines_menu()
                elif choice == "2":
                    self.sources_menu()
                elif choice == "3":
                    self.client_socket.send("quit".encode())
                    print("Goodbye!")
                    break
                else:
                    print("Invalid choice. Please try again.")
            except KeyboardInterrupt:
                print("\nProgram interrupted. Exiting...")
                break       