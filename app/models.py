import json
from dataclasses import dataclass
import sys

from mixins.json_manuplation import Json
PATH = "../data/tasks.json"

@dataclass
class Task:
    title: str
    description: str
    status: str

class TaskManager:
    count:int = 0

    def __init__(self):
        self.list_of_tasks = []

    def add_task(self, tasks: list[Task] | Task):
        if isinstance(tasks, list):
            self.list_of_tasks.extend(
                    tasks
            )
        else:
            self.list_of_tasks.append(
                tasks
            )
            
    def save_load_tasks(self, path = PATH):
        # Find all the tasks in the json file.
        Json().remove_duplicat(path=path)
        
        for i in range(0, len(self.list_of_tasks)):
            try:
                with open(path, "r") as f:
                    existing_data = json.load(f)
            except (FileNotFoundError, json.JSONDecodeError):
                existing_data = [] # Initialize as an empty list if no data exists
            
            print("Existing date: ",existing_data)
        # Find if the current data is in the file.        
            print("Current data is: ", self.list_of_tasks[i].title.lower().replace(" ","_"))
            if any(self.list_of_tasks[i].title.lower().replace(" ","_") in dic for dic in existing_data):
                print("key already exists")
                continue
            else:
                # If data is not present then add them to the file    
                data = {
                        self.list_of_tasks[i].title.lower().replace(" ","_"): {
                            "title" : self.list_of_tasks[i].title,
                            "description" : self.list_of_tasks[i].description,
                            "status": self.list_of_tasks[i].status
                        }
                    }
                existing_data.append(data)
                
                try:
                    with open(path, "w") as r:
                        json.dump(existing_data, r, indent=4 )
                except:
                    print("File not found")
