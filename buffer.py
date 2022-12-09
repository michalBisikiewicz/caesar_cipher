class Buffer:
    def __init__(self):
        self.buffer_list = []

    def add_encrypted_element(
        self, rot_type: str, text_to_encrypt: str, status: str
    ) -> None:
        self.buffer_list.append(
            {"rot type": rot_type, "text": text_to_encrypt, "status": status}
        )

    def add_decrypted_element(
        self, rot_type: str, text_to_decrypt: str, status: str
    ) -> None:
        self.buffer_list.append(
            {"rot type": rot_type, "text": text_to_decrypt, "status": status}
        )

    def show_encrypted(self):
        return print(self.buffer_list)

    def show_decrypted(self):
        return self.buffer_list
