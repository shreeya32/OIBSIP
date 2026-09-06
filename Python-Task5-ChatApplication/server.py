import socket
import threading
import datetime

HOST = '127.0.0.1'
PORT = 5555

# Dictionary to keep track of connected clients and their usernames
clients = {} 

def get_time():
    """Returns the current time in HH:MM format."""
    return datetime.datetime.now().strftime("%H:%M")

def broadcast(message, sender_conn=None):
    """Sends a message to all connected clients except the sender."""
    for client_conn in list(clients.keys()):
        if client_conn != sender_conn:
            try:
                client_conn.send(message.encode('utf-8'))
            except:
                # Remove client if sending fails
                client_conn.close()
                if client_conn in clients:
                    del clients[client_conn]

def handle_client(conn, addr):
    """Handles individual client connections."""
    try:
        # First message received is always the username
        username = conn.recv(1024).decode('utf-8')
        clients[conn] = username
        
        # Announce the new user to others
        join_msg = f"[{get_time()}] Server: {username} has joined the chat!"
        print(join_msg)
        broadcast(join_msg, conn)

        # Listen for messages
        while True:
            msg = conn.recv(1024).decode('utf-8')
            if not msg:
                break # Client disconnected gracefully
            
            # Format and broadcast the message
            formatted_msg = f"[{get_time()}] {username}: {msg}"
            print(formatted_msg) # Log to server console
            broadcast(formatted_msg, conn)

    except ConnectionResetError:
        pass # Client forcibly closed the connection
    finally:
        # Handle graceful disconnection
        conn.close()
        if conn in clients:
            username = clients.pop(conn)
            leave_msg = f"[{get_time()}] Server: {username} has disconnected."
            print(leave_msg)
            broadcast(leave_msg)

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print(f"Server is listening on {HOST}:{PORT}")

    while True:
        conn, addr = server.accept()
        # Start a new thread for every client that connects
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

if __name__ == "__main__":
    start_server()