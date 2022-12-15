import json

DIR_PATH = r"files/"


class FileHandler:
    @staticmethod
    def write_data(file_name, data):
        with open(f"{DIR_PATH}{file_name}", "w") as outfile:
            json.dump(data, outfile, indent=4)

    @staticmethod
    def read_data(file_name):
        with open(f"{DIR_PATH}{file_name}") as json_file:
            data = json.load(json_file)
            print(data)

    @staticmethod
    def append_data(file_name, new_data):
        with open(f"{DIR_PATH}{file_name}", "r+") as file:
            # First we load existing data into a dict.
            file_data = json.load(file)
            # Join new_data with file_data inside emp_details
            file_data.append(new_data)
            # Sets file's current position at offset.
            file.seek(0)
            # convert back to json.
            json.dump(file_data, file, indent=4)
