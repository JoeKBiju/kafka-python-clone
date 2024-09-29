import socket

def create_message(id, api_version):
    response_bytes = id.to_bytes(4, 'big')

    if (api_version == 35):
        response_bytes += api_version.to_bytes(2, 'big')
    
    return_message = len(response_bytes).to_bytes(4, 'big') + response_bytes
    return return_message

def get_request_length(request):
    length = int.from_bytes(request[0:4], 'big')
    return length

def get_api_version(request):
    api_version = int.from_bytes(request[6:8], 'big')

    if(api_version < 0 or api_version > 4):
        return 35
    
    return api_version

def parse_correlation(request):
    correlation_id = int.from_bytes(request[8:12], 'big')
    return correlation_id

def handle_client(client_socket):
    request = client_socket.recv(1024)
    correlation_id = parse_correlation(request)
    api_version = get_api_version(request)
    client_socket.sendall(create_message(correlation_id, api_version))
    client_socket.close()

def main():
    server = socket.create_server(("localhost", 9092), reuse_port=True)
    client_socket, client_addr = server.accept()
    handle_client(client_socket)

if __name__ == "__main__":
    main()
