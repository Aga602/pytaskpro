from dataclasses import dataclass
from typing import Any, Literal
from enum import Enum


@dataclass
class Task:
    title: str
    description: str
    status: Literal["to-do", "done", "repeat"] = "to-do"

    def __post_init__(self):
        allowed_status = ["to-do", "done", "repeat"]
        if self.status not in allowed_status:
            raise ValueError("The provided status is not valid.")

    def __str__(self):
        return "Task needs to be added with a suitable title, \
        description and status('to-do','done','repeat)"

    # in case input from a json file or a yaml file we will need to
    # use the class method
    @classmethod
    def from_dict(cls, task: dict):
        return cls(
            title=task["title"],
            description=task["description"],
            status=task["status"]
        )

    @staticmethod
    def is_valid(obj: Any):
        if isinstance(obj, Task):
            print("Valid Task type")
        else:
            print("Invalid Task type")


class TaskFunctions(Enum):
    hello = "h"
    add_task = "at"
    remove_task = "rt"
    change_status = "cs"
