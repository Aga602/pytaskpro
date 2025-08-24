import pytest

from app.manager import TaskManager
from app.models import Task

class TestTaskManager:
    def test_add_task(self):
        with pytest.raises(TypeError):
            TaskManager().add_task(tasks=Task())
    
    