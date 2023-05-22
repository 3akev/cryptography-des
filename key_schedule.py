from utils import permut, get_random_key

PC1 = [
    57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18, 10, 2, 59, 51, 43,
    35, 27, 19, 11, 3, 60, 52, 44, 36, 63, 55, 47, 39, 31, 23, 15, 7, 62, 54,
    46, 38, 30, 22, 14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 20, 12, 4
]
PC2 = [
    14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10, 23, 19, 12, 4, 26, 8, 16, 7,
    27, 20, 13, 2, 41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 33, 48, 44, 49, 39,
    56, 34, 53, 46, 42, 50, 36, 29, 32
]
rotation_table = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]


def left_rotate(block, decalage):
    tmp = block >> (28 - decalage)
    return ((block << decalage) | tmp) & 0xfffffff


def test_left_rotate():
    assert left_rotate(0x26d7123, 1) == 0x4dae246
    assert left_rotate(0xbd333cf, 1) == 0x7a6679f
    assert left_rotate(0xbd333cf, 4) == 0xd333cfb


def key_scheduler(key=None):
    keys = []
    key = key or get_random_key()
    key = permut(key, PC1)

    right = key & 0xfffffff
    left = (key >> 28) & 0xfffffff

    for i in range(16):
        decalage = rotation_table[i]

        left = left_rotate(left, decalage)
        right = left_rotate(right, decalage)

        k_n = (left << 28) ^ (right)
        k_n = permut(k_n, PC2)
        keys.append(k_n)

    return keys
