import json


class Jsonio:
    def __init__(self, path, mode):
        self.path = path
        self.mode = mode

    def __enter__(self):
        self.open_file = open(self.path, self.mode)
        return self.open_file

    def __exit__(self, exc_type, exc_value, exc_tb):
        if self.open_file:
            self.open_file.close()


def read_file(path):
    with Jsonio(path, "r") as read_file:
        return json.load(read_file)


def write_file(path, data):
    with Jsonio(path, "w") as write_file:
        json.dump(write_file, data, indent=4)
