class Cipher:
    @staticmethod
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

    @staticmethod
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

    @staticmethod
    def run_encrypt(select, text_to_encrypt):
        if select == "rot13":
            key = 13
            print("You are encrypting with ROT13")
            print("Text  : " + text_to_encrypt)
            print("Shift : " + str(key))
            print("Encrypt: " + Cipher.encrypt(text_to_encrypt, key))
        elif select == "rot47":
            key = 47
            print("You are encrypting with ROT47")
            print("Text  : " + text_to_encrypt)
            print("Shift : " + str(key))
            print("Encrypt: " + Cipher.encrypt(text_to_encrypt, key))

    @staticmethod
    def run_decrypt(select, text_to_decrypt):
        if select == "rot13":
            key = 13
            print("You are decrypting with ROT13")
            print("Text  : " + text_to_decrypt)
            print("Shift : " + str(key))
            print("Decrypt: " + Cipher.decrypt(text_to_decrypt, key))
        elif select == "rot47":
            key = 47
            print("You are decrypting with ROT47")
            print("Text  : " + text_to_decrypt)
            print("Shift : " + str(key))
            print("Decrypt: " + Cipher.decrypt(text_to_decrypt, key))


def main():
    rot_type = input(
        "Enter rot type to encrypt with. Choose between rot13 or rot47. : "
    )
    text_to_encrypt = input("Please enter text to encrypt: ")
    Cipher.run_encrypt(rot_type, text_to_encrypt)
    rot_type = input(
        "Enter rot type to decrypt with. Choose between rot13 or rot47. : "
    )
    text_to_decrypt = input("Please enter text to decrypt: ")
    Cipher.run_decrypt(rot_type, text_to_decrypt)


if __name__ == "__main__":
    main()
