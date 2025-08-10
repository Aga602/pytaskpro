import json
from core.exceptions import JSONFileNotFound
class Jsonio:
    def __init__(self, path):
        self.path = path 
    
    def check_file_exists(self, mode = "r"):
        try:
            open(self.path,mode)
        except:
            raise(JSONFileNotFound(path=self.path))
    def read_json(self):
        with self.check_file_exists() as readfile:
            return json.load(readfile)
    
    def write_json(self, data):
        with self.check_file_exists(mode="w") as writefile:
            # all value are intended to 4 later this can be a parameter as well
            json.dump(data, writefile, indent=4)