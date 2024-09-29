import socket

def create_message():
    id = 7
    id_bytes = id.to_bytes(4, 'big')
    return len(id_bytes).to_bytes(4, 'big') + id_bytes


def handle_client(client_socket):
    request = client_socket.recv(1024)
    print(request)
    client_socket.sendall(create_message())
    client_socket.close()

def main():
    server = socket.create_server(("localhost", 9092), reuse_port=True)
    client_socket, client_addr = server.accept()
    handle_client(client_socket)

if __name__ == "__main__":
    main()
