import socket
import threading
import pickle
def connect(dst):
    HEADER = 4
    PORT = {'transmissor': 5050, 'receptor': 5051, 'interface': 5052}
    FORMAT = "utf-8"
    SERVER = socket.gethostbyname(socket.gethostname())
    ADDR = (SERVER, PORT.get(dst))
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    clientData = {"HEADER": HEADER, "FORMAT": FORMAT, "client": client}
    return clientData

def disconnect(clientData):
    DISCONNECT_MESSAGE = 'Desconectar'
    send(DISCONNECT_MESSAGE, clientData)

def send(msg, clientData):
    serialized_msg = pickle.dumps(msg)
    msg_lenght = len(serialized_msg)
    send_lenght = str(msg_lenght).encode(clientData['FORMAT'])
    send_lenght += b' '*(clientData['HEADER'] - len(send_lenght))
    clientData['client'].send(send_lenght)
    clientData['client'].send(serialized_msg)