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