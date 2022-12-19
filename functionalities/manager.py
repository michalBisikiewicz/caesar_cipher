from functionalities.caesar_cipher import Cipher
from functionalities.file_handler import FileHandler
from functionalities.buffer import Buffer
import os

DIR_PATH = r"files/"


class Manager:
    """
    Allows user to manager program operations.
    """

    def __init__(self):
        self.__buffer = Buffer()
        self.__is_running: bool = True
        self.__functions_dict = {
            "1": self.__encrypt_text,
            "2": self.__decrypt_text,
            "3": self.__edit_encrypted_text,
            "4": self.__peak_buffer,
            "5": self.__save_buffer,
            "6": self.__read_saved_buffer,
            "7": self.__append_saved_buffer,
            "8": self.__end_app,
        }

    def run(self) -> None:
        """
        Function starts looping program with menu.
        """
        while self.__is_running:
            self.__print_menu()
            user_instruction = input("")
            self.__handle_instruction(user_instruction)
            print()

    def __handle_instruction(self, user_instruction):
        """
        Function gets right function and execute it based on user's choice.
        """
        if user_instruction in self.__functions_dict:
            self.__functions_dict.get(user_instruction)()
        else:
            print("Invalid option")

    def __print_menu(self) -> None:
        """
        Function prints available user's choices.
        """
        print(
            """Please select an option from menu:
            1. Encrypt text.
            2. Decrypt text.
            3. Edit encrypted text.
            4. Show buffer.
            5. Save buffer to a file.
            6. Read saved buffer from a file.
            7. Append saved buffer.
            8. Exit.
            """
        )

    def __encrypt_text(self) -> None:
        """
        Function encrypts user's input.
        """
        rot_type = input(
            "Enter rot type to encrypt with. Choose between rot13 or rot47. : "
        )
        if rot_type not in ["rot13", "rot47"]:
            print("Wrong Value. Please try again.")
        else:
            text_to_encrypt = input("Please enter text to encrypt: ")
            Cipher.run_encrypt(rot_type, text_to_encrypt)
            self.__buffer.add_encrypted_element(rot_type,
                                                text_to_encrypt,
                                                "encrypted")

    def __decrypt_text(self) -> None:
        """
        Function decrypts user's input.
        """
        rot_type = input(
            "Enter rot type to encrypt with. Choose between rot13 or rot47. : "
        )
        if rot_type not in ["rot13", "rot47"]:
            print("Wrong Value. Please try again.")
        else:
            text_to_decrypt = input("Please enter text to decrypt: ")
            Cipher.run_decrypt(rot_type, text_to_decrypt)
            self.__buffer.add_decrypted_element(
                rot_type,
                text_to_decrypt,
                "decrypted",
            )

    def __edit_encrypted_text(self) -> None:
        """
        Function allows to change encrypted text placed in buffer which stores
        data before saving into file.
        """
        text_to_change = input("Please enter text to change: ")
        rot_type = input(
            "Enter rot type to encrypt with. Choose between rot13 or rot47. : "
        )
        if rot_type not in ["rot13", "rot47"]:
            print("Wrong Value, Please Try again")
        else:
            new_text = input("Enter new text: ")
            found = False
            for element in self.__buffer.buffer_list:
                for key, value in element.items():
                    if value == text_to_change:
                        Cipher.run_encrypt(rot_type, new_text)
                        element[key] = new_text
                        found = True
                        break
            if not found:
                print("There is no such an element. Please Try again.")

    def __peak_buffer(self) -> None:
        """
        Function allows user to look into buffer list before saving into file.
        """
        self.__buffer.show_buffer()

    def __save_buffer(self) -> None:
        """
        Function allows user to save buffer into file.
        """
        file_name = input("Please enter file name: ")
        FileHandler.write_data(file_name, self.__buffer.buffer_list)

    def __read_saved_buffer(self) -> None:
        """
        Function allows user to read previously saved data.
        """
        # list to store files
        files = []
        for path in os.listdir(DIR_PATH):
            # check if current path  is a file
            if os.path.isfile(os.path.join(DIR_PATH, path)):
                files.append(path)
        for file_name in files:
            FileHandler.read_data(file_name)

    def __append_saved_buffer(self) -> None:
        """
        Function allows user to select a file to append an item into it.
        """
        files = []
        for path in os.listdir(DIR_PATH):
            if os.path.isfile(os.path.join(DIR_PATH, path)):
                files.append(path)
        file_name = input(f"Choose file to append: {files} ")
        rot_type = input(
            "Enter rot type to encrypt with. Choose between rot13 or rot47. : "
        )
        if rot_type not in ["rot13", "rot47"]:
            print("Wrong Value. Please try again.")
        else:
            text_to_encrypt: str = input("Please enter text to encrypt: ")
            Cipher.run_encrypt(rot_type, text_to_encrypt)
            FileHandler.append_data(
                file_name,
                {"rot type": rot_type,
                 "text": text_to_encrypt,
                 "status": "encrypted"},
            )

    def __end_app(self) -> None:
        """
        Function allows user to exit program.
        """
        self.__is_running = False
