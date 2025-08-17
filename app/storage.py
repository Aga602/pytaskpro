import json
from core.exceptions import JSONFileNotFound
class Jsonio:
    def __init__(self, path):
        self.path = path 
    
    def read_json(self):
        print("PATH: ",self.path) 
        with open(self.path,"r") as readfile:
            print(
                "file opened successfully"
            )
            return json.load(readfile)
    
    def write_json(self, data):
        print("Trying to add list to json file")
        with open(self.path,"w") as writefile:
            json.dump(data, writefile, indent=4)