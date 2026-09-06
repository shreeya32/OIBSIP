import socket
import threading
import sys

HOST = '127.0.0.1'
PORT = 5555


def receive_messages(client_socket):
    """Listens for incoming messages from the server."""
    while True:
        try:
            msg = client_socket.recv(1024).decode('utf-8')
            if not msg:
                print("\n[Server] Disconnected from the server.")
                break

            # Print received message (adds a newline to not heavily disrupt the typing prompt)
            print(f"\n{msg}")
        except:
            print("\n[Server] Connection lost.")
            break

    # Force exit if the receiving thread dies
    client_socket.close()
    sys.exit(0)


def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect((HOST, PORT))
    except ConnectionRefusedError:
        print("Could not connect to the server. Is it running?")
        return

    username = input("Enter your username: ")
    client_socket.send(username.encode('utf-8'))
    print("Connected to chat! Type your messages below (or type 'quit' to exit):")

    # Start a background thread to listen for incoming messages while we type
    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.daemon = True
    receive_thread.start()

    # Main thread handles sending messages
    while True:
        try:
            msg = input()
            if msg.lower() == 'quit':
                break
            if msg.strip():  # Don't send empty messages
                client_socket.send(msg.encode('utf-8'))
        except KeyboardInterrupt:
            break

    # Graceful shutdown
    client_socket.close()
    print("You left the chat.")


if __name__ == "__main__":
    start_client()