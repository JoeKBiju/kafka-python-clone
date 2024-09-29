import socket

def create_message(id):
    id_bytes = id.to_bytes(4, 'big')
    return_message = len(id_bytes).to_bytes(4, 'big') + id_bytes
    return return_message

def get_request_length(request):
    length_bytes = request[0:4]
    length = int.from_bytes(length_bytes, 'big')
    return length

def parse_correlation(request):
    correlation_id = int.from_bytes(request[8:12], 'big')
    return correlation_id

def handle_client(client_socket):
    request = client_socket.recv(1024)
    correlation_id = parse_correlation(request)
    client_socket.sendall(create_message(correlation_id))
    client_socket.close()

def main():
    server = socket.create_server(("localhost", 9092), reuse_port=True)
    client_socket, client_addr = server.accept()
    handle_client(client_socket)

if __name__ == "__main__":
    main()
