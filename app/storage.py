import json


class Jsonio:
    def __init__(self, path):
        self.path = path

    def read_json(self):
        with open(self.path, "r") as readfile:
            return json.load(readfile)

    def write_json(self, data):
        with open(self.path, "w") as writefile:
            json.dump(data, writefile, indent=4)
