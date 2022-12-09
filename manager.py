from caesar_cipher import Cipher, Buffer


class Manager:
    def __init__(self):
        self.__buffer = Buffer()
        self.__is_running: bool = True
        self.__functions_dict = {
            "1": self.__encrypt_text,
            "2": self.__decrypt_text,
            "3": self.__edit_encrypted_text,
            "4": self.__peak_buffer,
            "5": self.__save_buffer,
            "6": self.__end_app,
        }

    def run(self) -> None:
        while self.__is_running:
            self.__print_menu()
            user_instruction = input("")
            self.__handle_instruction(user_instruction)
            print()

    def __handle_instruction(self, user_instruction):
        if user_instruction in self.__functions_dict:
            self.__functions_dict.get(user_instruction)()
        else:
            print("Invalid option")

    def __end_app(self):
        self.__is_running = False

    def __encrypt_text(self):
        rot_type = input(
            "Enter rot type to encrypt with. Choose between rot13 or rot47. : "
        )
        if rot_type == "rot13" or rot_type == "rot47":
            text_to_encrypt = input("Please enter text to encrypt: ")
            Cipher.run_encrypt(rot_type, text_to_encrypt)
            self.__buffer.add_encrypted_element(
                rot_type,
                text_to_encrypt,
                "encrypted",
            )
        else:
            print("Wrong Value. Please try again.")

    def __decrypt_text(self):
        rot_type = input(
            "Enter rot type to encrypt with. Choose between rot13 or rot47. : "
        )
        if rot_type == "rot13" or rot_type == "rot47":
            text_to_decrypt = input("Please enter text to encrypt: ")
            Cipher.run_decrypt(rot_type, text_to_decrypt)
            self.__buffer.add_decrypted_element(
                rot_type,
                text_to_decrypt,
                "decrypted",
            )
        else:
            print("Wrong Value. Please try again.")

    def __edit_encrypted_text(self):
        rot_type = input(
            "Enter rot type to encrypt with. Choose between rot13 or rot47. : "
        )
        text_to_change = input("Please enter text to change: ")
        new_text = input("Enter new text: ")
        for element in self.__buffer.buffer_list:
            for key, value in element.items():
                if value == text_to_change:
                    Cipher.run_encrypt(rot_type, new_text)
                    element[key] = new_text
                    break
                else:
                    print("There is no such an element. Please Try again.")

    def __peak_buffer(self):
        return self.__buffer.show_encrypted()

    def __save_buffer(self):
        # FileHandler.write_data()
        pass

    def __print_menu(self):
        print(
            """Please select an option from menu:
            1. Encrypt Text.
            2. Decrypt Text.
            3. Edit encrypted text.
            4. Show buffer.
            5. Save Buffer to file.
            6. Exit.
            """
        )
