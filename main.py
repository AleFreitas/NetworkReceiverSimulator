#Bibliotecas Utilizadas
import socket
import threading
import pickle
import random

#Modulos
from codificacao import codificar

# Cria a Configuração do Servidor
def config():
    HEADER = 64                                             # Tamanho Máximo da Mensagem
    PORT = 5051                                             # Porta Host
    SERVER = socket.gethostbyname(socket.gethostname())     # Seleciona o IP Local
    ADDR = (SERVER, PORT)
    DISCONNECT_MESSAGE = "Desconectar"
    FORMAT = "utf-8"
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    serverData = {"HEADER": HEADER, "FORMAT": FORMAT, "server": server, "ip": SERVER, "DISCONNECT_MESSAGE": DISCONNECT_MESSAGE}
    return serverData                                        # Retorna todas as informações necessárias do server


# Função Responsável por receber as mensagens // Funciona por Thread
def handle_client(conn, addr, serverData):
    print('Nova Conexão!')
    connect = True
    lista_de_mensagens = []
    while connect:
        msg_lenght = conn.recv(serverData['HEADER']).decode(serverData['FORMAT'])
        if msg_lenght:
            msg_lenght = int(msg_lenght)
            serialized_msg = conn.recv(msg_lenght)
            msg = pickle.loads(serialized_msg)
            if msg == serverData['DISCONNECT_MESSAGE']:
                connect = False
            else:
                codificar(msg)          # Decodifica as mensagens

    conn.close()

# Função para Iniciar o Servidor
def start(serverData):
    serverData['server'].listen()
    print(f"O servidor está ouvindo em {serverData['ip']}")
    while True:
        conn, addr =  serverData['server'].accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr, serverData))
        thread.start()
        print(f"Conexões Ativas {threading.active_count() - 1}")


ServerData = config()
start(ServerData)