import socket

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 12345

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVER_HOST, SERVER_PORT))

    print("[*] Connected to remote server")

    while True:
        try:
            command = input("> ")
            client_socket.send(command.encode())
            if command.lower() == "exit":
                break
        except KeyboardInterrupt:
            break

    client_socket.close()

if __name__ == "__main__":
    main()
