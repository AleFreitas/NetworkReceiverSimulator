import random

def alterar_um_bit_aleatoriamente(bits):
    # Converte os bits para uma lista para torná-los mutáveis
    bits_mutaveis = list(bits)

    # Escolhe aleatoriamente a posição de um bit para ser alterado
    posicao_alteracao = random.randint(0, len(bits_mutaveis) - 2)  # -2 para excluir o último bit

    # Inverte o bit na posição escolhida
    bits_mutaveis[posicao_alteracao] = '1' if bits_mutaveis[posicao_alteracao] == '0' else '0'

    # Converte a lista de bits de volta para uma string
    bits_alterados = ''.join(bits_mutaveis)

    return bits_alterados
