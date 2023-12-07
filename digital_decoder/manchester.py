# DESCOMENTE ESSA FUNÇÃO CASO QUEIRA TESTAR RODANDO UM make manchester
# def manchester(bits, amplitude):
#     result = []
    
#     for bit in bits:
#         if int(bit) == 0:
#             # cria uma lista com 50 elementos (-amplitude) e outra com 50 elementos (amplitude) por bit
#             # depois cancatena as duas e adiciona ao result
#             # FORAM ESCOLHIDOS 50 DE CADA PARA FORMAR 100 POR BIT DE FORMA TOTALMENTE ARBITRÁRIA
#             # poderia ter sido feito só com result.extend([-amplitude] + [amplitude]) mas com
#             # menos amostras o gráfico teria transições menos claras visualmente
#             result.extend([-amplitude] * 50 + [amplitude] * 50)
#         else:
#             result.extend([amplitude] * 50 + [-amplitude] * 50)
    
#     return result

def manchester_decoder(signal):
    encoded_bits = [] # recebe o sinal e retira as repetições das amostras
    
    manchester_bit = [] # como o manchester codifica dois bits pra cada bit essa variavel só pode ir até len 2 antes de incluido e apagado
    # cria uma lista de sublistas, abstraindo as amostras a 1 ao inves de 100 por bit.
    # coloca 2 elementos em cada sublista representando o resultado da codificação manchester ex: [[-1,1],[1,-1]]
    for i in range(0, len(signal), 50):
        manchester_bit.append(signal[i])

        if len(manchester_bit) >= 2:
            encoded_bits.append(manchester_bit[:2])
            manchester_bit = manchester_bit[2:]  # Remove os dois primeiros elementos

    # utiliza a lista criada anteriormente para decodificar o sinal
    # ex: [[-1,1],[1,-1]] = '01'
    decoded_bits = []
    for i in encoded_bits:
        if(i[0] < 0):
            decoded_bits.append(0)
        else:
            decoded_bits.append(1)
    
    return ''.join(map(str,decoded_bits))




# DESCOMENTE TUDO ABAIXO CASO QUEIRA TESTAR RODANDO O make manchester
# # Exemplo de uso:
# bits_originais = '0001110101'
# amplitude_sinal = 1.0

# sinal_codificado = manchester(bits_originais, amplitude_sinal)
# decoded_bits = manchester_decoder(sinal_codificado)

# print("Bits originais:", bits_originais)
# print("Sinal codificado:", sinal_codificado)
# print("Bits decodificados:", decoded_bits)
