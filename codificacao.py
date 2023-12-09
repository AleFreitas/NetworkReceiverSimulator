from digital_decoder.nrz_polar import nrz_polar_decoder
from digital_decoder.bipolar import bipolar_decoder
from digital_decoder.manchester import manchester_decoder
import connections.client as client

def codificar(opcoes):
    # Dicionário simulando switch
    encoding_dict = {
        'NRZ': nrz_polar_decoder,
        'Manchester': manchester_decoder,
        'Bipolar': bipolar_decoder,
    }

    print(opcoes[0])
    signal = encoding_dict[opcoes[0][0]](opcoes[0][1])
    clientData = client.connect('interface')
    client.send(signal, clientData)
    client.disconnect(clientData)

