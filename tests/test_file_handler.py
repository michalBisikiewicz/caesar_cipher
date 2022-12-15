import json
import os

from unittest.mock import patch, mock_open


@patch("builtins.open", new_callable=mock_open, read_data="data")
def test_read_data(mock_file):
    assert open("r'/files/buffer_1.json'").read() == "data"
    mock_file.assert_called_with("r'/files/buffer_1.json'")


def test_write_data():
    mock = mock_open()
    with patch(f"{__name__}.open", mock, create=True):
        with open("file.json", "w") as file:
            file.write("testing")

    mock.assert_called_once_with("file.json", "w")
    handle = mock()
    handle.write.assert_called_once_with("testing")


def test_append_data():
    file = open("file.json", "w")
    data = {"employees": [{"name": "Mike", "departament": "sales"}]}
    json.dump(data, file)
    file.close()
    file_1 = open("file.json", "r+")
    data_1 = json.load(file_1)
    assert data_1 == {"employees": [{"name": "Mike", "departament": "sales"}]}
    data_to_append = {"name": "John", "departament": "unknown"}
    data_1["employees"].append(data_to_append)
    file_1.seek(0)
    json.dump(data_1, file_1)
    file_1.close()
    file_2 = open("file.json", "r")
    data_2 = json.load(file_2)
    assert data_2 == {
        "employees": [
            {"name": "Mike", "departament": "sales"},
            {"name": "John", "departament": "unknown"},
        ]
    }

    if os.path.exists("file.json"):
        os.remove("file.json")
    else:
        print("The file does not exist.")
