import socket
import threading
import pickle
from codificacao import codificar
import random

def config():
    HEADER = 64
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
    lista_de_mensagens = []
    while connect:
        msg_lenght = conn.recv(serverData['HEADER']).decode(serverData['FORMAT'])
        if msg_lenght:
            msg_lenght = int(msg_lenght)
            serialized_msg = conn.recv(msg_lenght)
            # Gera uma chance de 10% de erro de paridade 
            if random.random() < 0.1:
                _msg = induce_parity_error(serialized_msg)
            # Verifica o bit de paridade
            if check_parity(serialized_msg):
                msg = pickle.loads(serialized_msg[:-1])  # Remove o bit de paridade antes de desserializar
                
                if msg == serverData['DISCONNECT_MESSAGE']:
                    connect = False
                    codificar(lista_de_mensagens)
                else:
                    lista_de_mensagens.append(msg)
                    print(f"{addr} {msg} (Mensagem recebida com sucesso)")
            else:
                print(f"{addr} Erro de bit de paridade detectado")

    conn.close()

def induce_parity_error(serialized_msg):
    # Converte a mensagem serializada para uma lista de bytes
    msg_bytes = bytearray(serialized_msg)

    # Inverte o último bit na mensagem
    last_byte_index = len(msg_bytes) - 1
    msg_bytes[last_byte_index] ^= 1  # Inverte o último bit usando operador XOR

    # Retorna a mensagem com o erro de bit de paridade
    return bytes(msg_bytes)


def check_parity(data):
    # Conta o número de bits 1 na mensagem
    number_of_ones = sum(map(int, bin(int.from_bytes(data, byteorder='big'))[2:]))
    
    # Retorna True se o número de bits 1 for par, indicando paridade correta
    return number_of_ones % 2 == 0

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