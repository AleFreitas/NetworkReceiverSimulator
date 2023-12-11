def is_power_of_two(number):
    i = 1
    while i < number:
        i = i*2
    if i == number:
        return True
    return False

def menor_quantidade_potencias_de_dois(x):
    # Encontrar a representação binária de x
    binary_representation = bin(x)[2:][::-1]  # [2:] para remover o prefixo '0b' e [::-1] para inverter a string

    # Inicializar a lista de elementos resultantes
    elementos = []

    # Percorrer a representação binária e adicionar os elementos correspondentes
    for i, bit in enumerate(binary_representation):
        if bit == '1':
            elementos.append(2 ** i)

    return elementos

def remover_indices_potencia_de_2(bits_lista):
    # Encontrar índices de potência de 2 na lista de bits
    indices_potencia_de_2 = [i for i in range(len(bits_lista)) if (i + 1) & (i) == 0]

    # Remover os bits nos índices de potência de 2
    mensagem_sem_potencia_de_2 = [bit for i, bit in enumerate(bits_lista) if i not in indices_potencia_de_2]

    return mensagem_sem_potencia_de_2

def verify_hamming(hamming_bits):
    lista_de_caracteres = []
    for caractere in hamming_bits:
        caractere = int(caractere)
        lista_de_caracteres.append(caractere)
    hamming_bits = lista_de_caracteres
    # criando as relações dos bits verificadores
    i = 1
    number_of_verifiers = []
    verify_position_dict = {}
    for bit in hamming_bits:
        if is_power_of_two(i):
            number_of_verifiers.append(i)
            verify_position_dict[i] = [hamming_bits[i-1]]
            i+=1
        else:
            verify_positions = menor_quantidade_potencias_de_dois(i)
            for z in verify_positions:
                verify_position_dict[z].append(hamming_bits[i-1])
            i+=1
    error_index_in_bits = []
    for i in range(len(number_of_verifiers)): 
        error_index_in_bits.append(0 if sum(verify_position_dict[number_of_verifiers[i]]) % 2 == 0 else 1)
    if sum(error_index_in_bits) != 0:
        print('ERRO ENCONTRADO')
        print('RESOLVENDO...')
        print(verify_position_dict)
        print(error_index_in_bits)
        # Convertendo a lista de bits para um número inteiro que representa a posição do erro
        error_index_in_bits.reverse()
        number = int(''.join(map(str, error_index_in_bits)), 2)
        print(number)
        error_bit = hamming_bits[number - 1]
        if error_bit == 0:
            hamming_bits[number - 1] = 1
        else:
            hamming_bits[number - 1] = 0
        hamming_bits = remover_indices_potencia_de_2(hamming_bits)
        erro_encontrado = f"Erro Encontrado e Corrigido: Posição {number}"
    else:
        hamming_bits = remover_indices_potencia_de_2(hamming_bits)
        erro_encontrado = f"Não possui erros"
    return hamming_bits, erro_encontrado
