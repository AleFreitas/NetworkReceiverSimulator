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

    signal = encoding_dict[opcoes[1]](opcoes[0])
    clientData = client.connect('interface')
    client.send(signal, clientData)
    client.disconnect(clientData)

