import socket
import pyautogui

SERVER_HOST = "0.0.0.0"
SERVER_PORT = 12345

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((SERVER_HOST, SERVER_PORT))
    server_socket.listen(1)

    print(f"[*] Listening on {SERVER_HOST}:{SERVER_PORT}")

    client_socket, client_address = server_socket.accept()
    print(f"[*] Accepted connection from {client_address[0]}:{client_address[1]}")

    while True:
        try:
            data = client_socket.recv(1024).decode()
            if not data:
                break

            if data.startswith("MOUSE"):
                x, y = map(int, data.split()[1:])
                pyautogui.moveTo(x, y)
            elif data.startswith("CLICK"):
                pyautogui.click()
            elif data.startswith("KEY"):
                key = data.split()[1]
                pyautogui.press(key)

        except Exception as e:
            print(f"Error: {e}")
            break

    client_socket.close()
    server_socket.close()

if __name__ == "__main__":
    main()
