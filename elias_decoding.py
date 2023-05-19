import math


# function
def elias_gamma_decoding(x):
    x = list(x)
    K = 0
    while True:
        if not x[K] == '0':
            break
        K = K + 1

    # Reading K more bits from '1'
    x = x[K:2 * K + 1]

    n = 0
    x.reverse()

    # Converting binary to integer
    for i in range(len(x)):
        if x[i] == '1':
            n = n + math.pow(2, i)
    return int(n)


def elias_delta_decoding(x):
    x = list(x)
    L = 0
    while True:
        if not x[L] == '0':
            break
        L = L + 1

    # Reading L more bits and dropping ALL
    x = x[2 * L + 1:]

    # Prepending with 1 in MSB
    x.reverse()
    x.insert(0, '1')
    n = 0

    # Converting binary to integer
    for i in range(len(x)):
        if x[i] == '1':
            n = n + math.pow(2, i)
    return int(n)


def elias_decoding(x, encoding):
    if encoding == 1:
        return elias_gamma_decoding(x)
    else:
        return elias_delta_decoding(x)