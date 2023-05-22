from DES import encrypt, decrypt
from key_schedule import key_scheduler


def test_DES():
    key = 0x56f5db1b7e9f4142
    keys = key_scheduler(key)
    msg = b'test message'
    expected = b'\x19g\xb7R\x91Cn\x88/\xbe{\xea\x0b\xe6\xcbI'

    cipher = encrypt(msg, keys)
    clear = decrypt(cipher, keys)

    assert clear.startswith(msg)
    assert cipher == expected
    assert len(cipher) == len(clear)
