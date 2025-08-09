import json

from models import Task
from storage import Jsonio

PATH = "../data/tasks.json"

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
        
        for i in range(0, len(self.list_of_tasks)):
            try:
                existing_data = Jsonio(path).read_json()
                print("EXISTING DATA: ", existing_data)
            except (FileNotFoundError, json.JSONDecodeError):
                existing_data = [] # Initialize as an empty list if no data exists

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
                print("DATA: ",data)
                existing_data.append(data)

                print(existing_data)
                try:
                    Jsonio(path).write_json(data=existing_data)
                except:
                    print("File not found")

A = TaskManager()
A.add_task(
    Task(
        title="Do Homework",
        description="Doing homework is good for you acadamics and decipline",
        status="repeat"
        
        
    )
)

A.save_load_tasks()