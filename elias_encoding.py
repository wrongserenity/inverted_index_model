from math import log
from math import floor

def binary_representation_without_msb(x):
    binary = "{0:b}".format(int(x))
    binary_without_MSB = binary[1:]
    return binary_without_MSB


def elias_gamma_encode(k):
    if (k == 0):
        return '0'
    n = 1 + floor(log(k, 2))
    unary = (n - 1) * '0' + '1'
    return unary + binary_representation_without_msb(k)


def elias_delta_encode(x):
    gamma = elias_gamma_encode(1 + floor(log(x, 2)))
    binary_without_msb = binary_representation_without_msb(x)
    return gamma + binary_without_msb


def elias_encoding(number, encoding):
    if encoding == 1:
        return elias_gamma_encode(number)
    elif encoding == 2:
        return elias_delta_encode(number)