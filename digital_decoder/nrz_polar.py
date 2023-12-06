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