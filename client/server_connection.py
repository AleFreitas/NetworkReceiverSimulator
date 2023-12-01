import socket

def receive_bits_from_server(server_ip, server_port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = (server_ip, server_port)
    client_socket.connect(server_address)

    buffer_size = 1024
    data = client_socket.recv(buffer_size)

    client_socket.close()

    return data