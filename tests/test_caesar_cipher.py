from functionalities.caesar_cipher import Cipher


def test_encrypt_rot_13():
    text = "Test"
    key = 13
    assert Cipher.encrypt(text, key) == "Grfg"


def test_decrypt_rot_13():
    text = "Grfg"
    key = 13
    assert Cipher.decrypt(text, key) == "Test"


def test_encrypt_rot_47():
    text = "Test"
    key = 47
    assert Cipher.encrypt(text, key) == "Ozno"


def test_decrypt_rot_47():
    text = "Ozno"
    key = 47
    assert Cipher.decrypt(text, key) == "Test"
