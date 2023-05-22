from utils import permut, get_random_key
from f_function import f
from key_schedule import key_scheduler

IP = [
    57, 49, 41, 33, 25, 17, 9, 1, 59, 51, 43, 35, 27, 19, 11, 3, 61, 53, 45,
    37, 29, 21, 13, 5, 63, 55, 47, 39, 31, 23, 15, 7, 56, 48, 40, 32, 24, 16,
    8, 0, 58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4, 62, 54,
    46, 38, 30, 22, 14, 6
]
FP = [
    39, 7, 47, 15, 55, 23, 63, 31, 38, 6, 46, 14, 54, 22, 62, 30, 37, 5, 45,
    13, 53, 21, 61, 29, 36, 4, 44, 12, 52, 20, 60, 28, 35, 3, 43, 11, 51, 19,
    59, 27, 34, 2, 42, 10, 50, 18, 58, 26, 33, 1, 41, 9, 49, 17, 57, 25, 32, 0,
    40, 8, 48, 16, 56, 24
]


def des_block(block, keys):
    block = permut(block, IP)

    left = (block >> 32) & 0xffffffff
    right = block & 0xffffffff

    for i in range(16):
        tmp = right
        right = f(right, keys[i]) ^ left
        left = tmp

    combined = (right << 32) ^ left

    combined = permut(combined, FP)
    return combined


def segment(msg: bytes):
    for i in range(0, len(msg), 8):
        substr = msg[i:i + 8].ljust(8, b'\0')
        block = int(substr.hex(), 16)
        yield block


def join(blocks):
    msg = b''
    for block in blocks:
        for i in range(7, -1, -1):
            octet = ((block >> 8 * i) & 0xff)
            msg += bytes([octet])

    return msg


def encrypt(msg, keys):
    return join(des_block(block, keys) for block in segment(msg))


def decrypt(msg, keys):
    return encrypt(msg, keys[::-1])


def main():
    key = get_random_key()
    keys = key_scheduler(key)
    txt = input("Enter text to encrypt: \n").encode('utf-8')
    cipher = encrypt(txt, keys)
    print("cipher:", cipher)
    clear = decrypt(cipher, keys)
    print("clear: ", clear)


if __name__ == '__main__':
    main()
