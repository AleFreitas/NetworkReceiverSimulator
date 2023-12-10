from digital_decoder.nrz_polar import nrz_polar_decoder
from digital_decoder.bipolar import bipolar_decoder
from digital_decoder.manchester import manchester_decoder
import connections.client as client

def codificar(opcoes):
    # Opções de Decodificação Digital
    encoding_dict = {
        'NRZ': nrz_polar_decoder,
        'Manchester': manchester_decoder,
        'Bipolar': bipolar_decoder,
    }
    # Opções de Verificação de Erro
    erro_dict = {
        'PAR': verificar_bit_parity
        ## 'CRC' : funcao_CRC
    }

    lista_interface = []                                 # Cria a lista para enviar os dados
    signal = encoding_dict[opcoes[1]](opcoes[0])         # Faz a decodificação do Sinal
    mensagem, erro = erro_dict[opcoes[2]](signal)                # Retira o bit de paridade e retorna o Erro

    lista_interface.append(mensagem)                     # Adiciona os dados a lista
    lista_interface.append(erro)

    clientData = client.connect('interface')             # Cria a conexão com a interface e envia os dados
    client.send(mensagem, clientData)
    client.send(erro, clientData)
    client.disconnect(clientData)

def verificar_bit_parity(bits):
    # Converte os bits para inteiros, se necessário
    bits = [int(bit) for bit in bits]
    # Calcula o número de bits 1 na lista, excluindo o bit de paridade
    number_of_bits = sum(bits[:-1])
    # Verifica se o número total de bits 1, incluindo o bit de paridade, é par
    parity_check = (number_of_bits + bits[-1]) % 2 == 0
    # Remove o bit de paridade da lista
    bits_sem_parity = bits[:-1]

    erro = "Existe Erro"
    sem_erro = "Mensagem sem Erro"
    if parity_check == True:
        return bits_sem_parity, sem_erro
    else:
        return bits_sem_parity, erro