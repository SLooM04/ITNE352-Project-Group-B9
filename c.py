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
    def headlines_menu(self):
        while True:
            print("\nHeadlines Menu:")
            print("1 - Search by Keyword")
            print("2 - Search by Category")
            print("3 - Search by Country")
            print("4 - List All Headlines")
            print("5 - Back to Main Menu")

            choice = input("Choose an option: ").strip()

            if choice == "1":
                keyword = input("Enter keyword: ")
                self.client_socket.send(f"headlines q={keyword}".encode())
            elif choice == "2":
                category = input("Enter category (business, general, health, science, sports, technology): ")
                self.client_socket.send(f"headlines category={category}".encode())
            elif choice == "3":
                country = input("Enter country code (au, ca, jp, ae, sa, kr, us, ma): ")
                self.client_socket.send(f"headlines country={country}".encode())
            elif choice == "4":
                self.client_socket.send("headlines".encode())
            elif choice == "5":
                break
            else:
                print("Invalid choice.")
                continue

            self.display_response("Headlines")

    def sources_menu(self):
        while True:
            print("\nSources Menu:")
            print("1 - Search by Category")
            print("2 - Search by Country")
            print("3 - Search by Language")
            print("4 - List All Sources")
            print("5 - Back to Main Menu")

            choice = input("Choose an option: ").strip()

            if choice == "1":
                category = input("Enter category (business, general, health, science, sports, technology): ")
                self.client_socket.send(f"sources category={category}".encode())
            elif choice == "2":
                country = input("Enter country code (au, ca, jp, ae, sa, kr, us, ma): ")
                self.client_socket.send(f"sources country={country}".encode())
            elif choice == "3":
                language = input("Enter language code (ar, en): ")
                self.client_socket.send(f"sources language={language}".encode())
            elif choice == "4":
                self.client_socket.send("sources".encode())
            elif choice == "5":
                break
            else:
                print("Invalid choice.")
                continue

            self.display_response("Sources")

    def display_response(self, item_type):
        try:
            response = self.client_socket.recv(50000).decode()
            data = json.loads(response)

            items = data.get("articles", []) if item_type == "Headlines" else data.get("sources", [])
            if not items:
                print(f"No {item_type.lower()} found.")
                return

            # Limit the results to 15
            items = items[:15]

            for i, item in enumerate(items):
                if item_type == "Headlines":
                    print(f"{i + 1}. {item['title']} ({item['source']['name']})")
                else:
                    print(f"{i + 1}. {item['name']} ({item['country']})")

            while True:
                choice = input(f"Enter the number of the {item_type.lower()} to view details (or 'back' to return): ").strip()
                if choice.lower() == 'back':
                    break

                try:
                    index = int(choice) - 1
                    if 0 <= index < len(items):
                        self.display_details(items[index], item_type)
                    else:
                        print("Invalid number. Try again.")
                except ValueError:
                    print("Invalid input. Enter a number or 'back'.")
        except json.JSONDecodeError:
            print("Failed to decode server response.")
