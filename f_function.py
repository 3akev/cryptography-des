from sbox import calc_sbox
from utils import permut

P = [
    16, 7, 20, 21, 29, 12, 28, 17, 1, 15, 23, 26, 5, 18, 31, 10, 2, 8, 24, 14,
    32, 27, 3, 9, 19, 13, 30, 6, 22, 11, 4, 25
]
E = [
    31, 0, 1, 2, 3, 4, 3, 4, 5, 6, 7, 8, 7, 8, 9, 10, 11, 12, 11, 12, 13, 14,
    15, 16, 15, 16, 17, 18, 19, 20, 19, 20, 21, 22, 23, 24, 23, 24, 25, 26, 27,
    28, 27, 28, 29, 30, 31, 0
]


def f(h, k):
    # expansion
    b = permut(h, E)

    # xor with key
    b = b ^ k

    # sbox
    s = substitution(b)

    # permutation
    s = permut(s, P)

    return s


def substitution(x):
    s = 0
    for n in range(8, 0, -1):
        part = x & 0b111111
        x >>= 6

        b = calc_sbox(n, part)
        s >>= 4
        s ^= (b << 28)

    return s
