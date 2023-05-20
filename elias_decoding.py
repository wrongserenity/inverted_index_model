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


def decode(x):
    num = 0
    for i in range(len(x)):
        num += (int(x[len(x) - 1 - i]) * (math.pow(2, i)))
    return num


def elias_delta_decoding(x):
    if x == '1':
        return 1
    else:
        x = list(x)
        t = 0
        v = []
        b = 0
        w = []
        c = 0
        for i in x:
            if b != 1:
                if i == '0':
                    t += 1
                else:
                    v.append(i)
                    b = 1
            elif c != 1:
                if t == 0:
                    c = 1
                    w.append('1')
                    w.append(i)
                else:
                    v.append(i)
                    t -= 1
            else:
                num = decode(v)
                if num == 0:
                    break
                else:
                    w.append(i)
                    num -= 1
        ans = decode(w)
    return int(ans)


def elias_decoding(x, encoding):
    if encoding == 1:
        return elias_gamma_decoding(x)
    else:
        return elias_delta_decoding(x)