class JSONFileNotFound(FileNotFoundError):
    def __init__(self, *args,path):
        super().__init__(*args)
        self.path = path
    def __str__(self):
        return("The json file is not found in the path: ",self.path)