from digital_decoder.nrz_polar import nrz_polar_decoder
from digital_decoder.bipolar import bipolar_decoder
from digital_decoder.manchester import manchester_decoder
import connections.client as client
from paridade import *
from gerador_erro import *

def codificar(opcoes):
    # Opções de Decodificação Digital
    encoding_dict = {
        'NRZ': nrz_polar_decoder,
        'Manchester': manchester_decoder,
        'Bipolar': bipolar_decoder,
    }
    # Opções de Verificação de Erro
    erro_dict = {
        'PAR': verificar_bit_parity,
        'SIM': alterar_um_bit_aleatoriamente
        ## 'CRC' : funcao_CRC
    }

    lista_interface = []                                    # Cria a lista para enviar os dados
    signal = encoding_dict[opcoes[1]](opcoes[0])            # Faz a decodificação do Sinal
    mensagem_erro = erro_dict[opcoes[3]](signal)
    mensagem, erro = erro_dict[opcoes[2]](mensagem_erro)    # Retira o bit de paridade e retorna o Erro

    lista_interface.append(mensagem)                        # Adiciona os dados a lista
    lista_interface.append(erro)

    clientData = client.connect('interface')             # Cria a conexão com a interface e envia os dados
    client.send(mensagem, clientData)
    client.send(erro, clientData)
    client.disconnect(clientData)

