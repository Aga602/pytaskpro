from dataclasses import dataclass
from typing import Literal

@dataclass
class Task:
    title: str
    description: str
    status: Literal["to-do", "done", "repeat"] = "to-do"
    
    def __post_init__(self):
        allowed_status = ["to-do", "done", "repeat"]
        if self.status not in allowed_status:
            raise ValueError("The provided status is not valid.")
