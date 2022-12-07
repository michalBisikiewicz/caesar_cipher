import json

data = {
    "employees": [
        {"name": "John Doe", "department": "Marketing", "place": "Remote"},
    ]
}
data_1 = {
    "elo": [
        {"name": "Jan Kowalski", "department": "Sales", "place": "Remote"},
    ]
}


def write_data(file_name, data):
    with open(file_name, "w") as outfile:
        json.dump(data, outfile, indent=4)


def read_data(file_name):
    with open(file_name) as json_file:
        data = json.load(json_file)
        print(data)


def append_data(file_name, new_data):
    with open(file_name, "r+") as file:
        # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        file_data["employees"].append(new_data)
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent=4)


# python object to be appended
x = {"name": "Mike", "email": "mike@sales.org", "job_profile": "Full Time"}


def main():
    write_data("elo.json", data)
    read_data("elo.json")
    append_data("elo.json", x)
    read_data("elo.json")


if __name__ == "__main__":
    main()
