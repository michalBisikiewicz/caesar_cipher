class Cipher:
    ROTS = {"rot13": 13, "rot47": 47}

    @staticmethod
    def encrypt(text: str, key: int) -> str:
        """
        This method allows you to input text to be encrypted.
        """
        result: str = ""
        # Traverse text
        for char in text:
            # Encrypt uppercase characters
            if char.isupper():
                result += chr((ord(char) + key - 65) % 26 + 65)
            # Encrypt lowercase characters
            else:
                result += chr((ord(char) + key - 97) % 26 + 97)
        return result

    @staticmethod
    def decrypt(text: str, key: int) -> str:
        """
        This method allows you to input text to be decrypted.
        """
        result: str = ""
        key = 26 - key
        # Traverse text
        for char in text:
            # Encrypt uppercase characters
            if char.isupper():
                result += chr((ord(char) + key - 65) % 26 + 65)
            # Encrypt lowercase characters
            else:
                result += chr((ord(char) + key - 97) % 26 + 97)
        return result

    @staticmethod
    def run_encrypt(select: str, text_to_encrypt: str) -> None:
        """
        This method allows you to encrypt text.
        """
        key = Cipher.ROTS.get(select)
        print(f"You are decrypting with {select.upper()}")
        print("Text  : " + text_to_encrypt)
        print("Shift : " + str(key))
        print("Decrypt: " + Cipher.encrypt(text_to_encrypt, key))

    @staticmethod
    def run_decrypt(select: str, text_to_decrypt: str) -> None:
        """
        This method allows you to decrypt text.
        """
        key = Cipher.ROTS.get(select)
        print(f"You are decrypting with {select.upper()}")
        print("Text  : " + text_to_decrypt)
        print("Shift : " + str(key))
        print("Decrypt: " + Cipher.decrypt(text_to_decrypt, key))
