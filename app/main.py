import socket  # noqa: F401

def create_message():
    return "\U00000008\U00000007"

def handle_client(client_socket):
    request = client_socket.recv(1024)
    client_socket.send(create_message())
    client_socket.close()

def main():
    server = socket.create_server(("localhost", 9092), reuse_port=True)
    client_socket, client_addr = server.accept()

if __name__ == "__main__":
    main()
