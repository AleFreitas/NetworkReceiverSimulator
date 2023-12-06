import socket
import threading
import pickle

def config():
    HEADER = 4
    PORT = 5051
    SERVER = socket.gethostbyname(socket.gethostname())
    ADDR = (SERVER, PORT)
    DISCONNECT_MESSAGE = "Desconectar"
    FORMAT = "utf-8"
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    serverData = {"HEADER": HEADER, "FORMAT": FORMAT, "server": server, "ip": SERVER, "DISCONNECT_MESSAGE": DISCONNECT_MESSAGE}
    return serverData

def handle_client(conn, addr, serverData):
    print('Nova Conexão!')
    connect = True
    while connect:
        msg_lenght = conn.recv(serverData['HEADER']).decode(serverData['FORMAT'])
        if msg_lenght:
            msg_lenght = int(msg_lenght)
            serialized_msg = conn.recv(msg_lenght)
            msg = pickle.loads(serialized_msg)
            if msg == serverData['DISCONNECT_MESSAGE']:
                connect = False
            print(f"{addr} {msg}")
    conn.close()

def start(serverData):
    serverData['server'].listen()
    print(f"O servidor está ouvindo em {serverData['ip']}")
    while True:
        conn, addr =  serverData['server'].accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr, serverData))
        thread.start()
        print(f"Conexões Ativas {threading.activeCount() - 1}")
