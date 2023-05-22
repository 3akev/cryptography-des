import random


def permut(x, L):
    a = 0
    for i, n in enumerate(L):
        a ^= ((x >> n) & 1) << i
    return a


def test_permut():
    assert permut(0b101101, [2, 4, 5, 3, 0, 1]) == 0b011101


def get_random_key():
    return expand_key(random.getrandbits(56))


def expand_key(k):
    result = 0
    for _ in range(8):
        part = k & 0b1111111
        pair = 0
        for _ in range(7):
            pair ^= k & 1
            k >>= 1

        b = (pair << 7) ^ part

        result >>= 8
        result ^= (b << 56)

    return result


def test_expand_key():
    data = [
        (0xcdaa029a86b4f0),
        (0xa4a3557b5ea4f5),
        (0x00000000000000),
        (0x66b4f24ba88d98),
        (0x0e3d2d191317b9),
        (0xffffffffffffff),
        (0xd4773853e3c509),
        (0x10637af06e7e94),
        (0xa4639a651ed7eb),
        (0xa27eedcd287001),
    ]

    expected = [
        0x666ac0a9d49a69f0,
        0xd2286ad75afac9f5,
        0x0000000000000000,
        0x332d1e24dd221b18,
        0x870fa5d148ccaf39,
        0xffffffffffffffff,
        0x6a1de7059f0f0a09,
        0x88186faf03397d14,
        0xd218f3a6287bafeb,
        0xd19fdd5c69216081,
    ]

    for d, e in zip(data, expected):
        assert expand_key(d) == e


def extract_key(k):
    result = 0
    for _ in range(8):
        part = k & 0b1111111
        k >>= 8

        result >>= 7
        result ^= (part << 49)

    return result
