from client.server_connection import receive_bits_from_server

def main():
    print("Hello, World!")
    server_ip = '127.0.1.1'
    server_port = 5050

    received_data = receive_bits_from_server(server_ip, server_port)
    print("Bits recebidos:", received_data)

if __name__ == "__main__":
    main()