# ESSA FUNÇÃO ESTÁ AQUI APENAS PARA RODAR OS TESTES
def _nrz_polar(bits, amplitude=1):
    result = []
    for bit in bits:
        if int(bit) > 0:
            # cria uma lista com 100 elementos (amplitude) por bit
            # depois adiciona ao result
            # FORAM ESCOLHIDOS 100 DE CADA POR BIT DE FORMA TOTALMENTE ARBITRÁRIA
            # poderia ter sido feito só com result.extend([amplitude]) mas com
            # menos amostras o gráfico teria transições menos claras visualmente
            result.extend([amplitude] * 100)
        else:
            result.extend([-amplitude] * 100)
    return result


def nrz_polar_decoder(signal):
    decoded_bits = []

    for sample in signal:
        if sample > 0:
            decoded_bits.append(1)
        else:
            decoded_bits.append(0)

    # Agora, precisamos reduzir a lista de decoded_bits para apenas um bit por amostra.
    # considerando que cada bit é representado por 100 amostras dentro do sinal.

    bit_stream = []
    for i in range(0, len(decoded_bits), 100):
        bit_stream.append(decoded_bits[i])

    # converte cada bit inteiro dentro da lista em string e junta em uma unica string
    return ''.join(map(str, bit_stream))

sinal_codificado = _nrz_polar('01010011')
decoded_bits = nrz_polar_decoder(sinal_codificado)

print("Bits originais:", '01010011')
print("Sinal codificado:", sinal_codificado)
print("Bits decodificados:", decoded_bits)
