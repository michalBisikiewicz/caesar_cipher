def encrypt(text: str, key: int):
    result = ""
    # Traverse text
    for i in range(len(text)):
        char = text[i]

        # Encrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) + key - 65) % 26 + 65)

        # Encrypt lowercase characters
        else:
            result += chr((ord(char) + key - 97) % 26 + 97)

    return result


def decrypt(text: str, key: int):
    result = ""
    key = 26 - key
    # Traverse text
    for i in range(len(text)):
        char = text[i]

        # Encrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) + key - 65) % 26 + 65)

        # Encrypt lowercase characters
        else:
            result += chr((ord(char) + key - 97) % 26 + 97)

    return result


# check the above function
key = 13
text_to_encrypt = "abcdABCD"
text_to_decrypt = encrypt(text_to_encrypt, key)

print("Text  : " + text_to_encrypt)
print("Shift : " + str(key))
print("Encrypt: " + encrypt(text_to_encrypt, key))
print("Decrypt: " + decrypt(text_to_decrypt, key))
