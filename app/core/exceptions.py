from collections.abc import Iterable

class JSONFileNotFound(FileNotFoundError):
    def __init__(self, *args,path:str):
        super().__init__(*args)
        self.path = path
    def __str__(self):
        return("The json file is not found in the path: ",self.path)

class InvalidLiteral(ValueError):
    def __str__(self):
        return(f"There is no cli command, The allowed values are hello")