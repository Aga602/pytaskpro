import json

from models import Task
from storage import Jsonio
from typing import Optional
from app.exceptions import JSONFileNotFound
import os

PATH = os.path.join(os.path.curdir ,"data", "tasks.json")
try:
    if os.path.exists(PATH):
        print("Path exists")
except:
    raise JSONFileNotFound(path=PATH)
    
class TaskManager:

    def __init__(self):
        self.list_of_tasks = []

    def add_task(self, tasks: list[Task] | Task):
        print(type(tasks))
        if isinstance(tasks, list):
            self.list_of_tasks.extend(
                    tasks
            )
        else:
            self.list_of_tasks.append(
                tasks
            )

    def save_load_tasks(self, task: list[Task] | Task ,path: str = PATH):
        # Find all the tasks in the json file.
        self.add_task(tasks=task)
        print(self.list_of_tasks)
        for i in range(0, len(self.list_of_tasks)):
            try:
                existing_data:list = Jsonio(path).read_json()
                print("EXISTING DATA: ", existing_data)
            except (FileNotFoundError, json.JSONDecodeError):
                existing_data = [] # Initialize as an empty list if no data exists
        # Find if the current data is in the file.   
            print("Current data is: "
                  ,self.list_of_tasks[i].title.lower().replace(" ","_"))
            if any(
                self.list_of_tasks[i].title.lower().replace(" ","_") in dic 
                for dic in existing_data
                ):
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
                    JSONFileNotFound(path=path)
                    
    def list_tasks(self, type: Optional[str], path = PATH ):
        existing_data = Jsonio(path).read_json()
        tasks = [ 
                 Task(
                     title=v["title"],
                     description=v["description"],
                     status=v["status"]
                    ) 
                 for x in existing_data 
                 for _,v in x.items()
                ]
        if type != None:
            print("List of Tasks with status ", type)
            print([task.title for task in tasks if task.status == type.lower()])
        else:
            print("List of ALL Tasks: ")
            print([task.title for task in tasks])

    def remove_task(self, title:str, path = PATH):
        # see if title exists
        try:
                existing_data:list = Jsonio(path).read_json()
                print("Existing data: ", existing_data)
                if any(title.replace(" ","_").lower().strip() in dic for dic in existing_data):
                    print("title is present")
                    remove = [dic for dic in existing_data if title.replace(" ","_").lower().strip() in dic]
                    existing_data = [x for x in existing_data if x not in remove]
                    print(existing_data)   
                    Jsonio(path).write_json(data=existing_data)
                else:
                    print("Title is not found")
        except Exception as e:
            print(f"The json file is empty: {e}")
