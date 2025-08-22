import pytest

from app.models import Task, TaskFunctions

class TestModels:
    def test_default_status(self):
        passTask = Task(
            title = "Check Default Status",
            description= "checking default value"
        )
        assert passTask.status == "to-do"

    def test_default_fail(self):
        newTask = Task(
            title = "Check Default Status",
            description= "checking default value"
        )
        assert not newTask.status == "repeat"
    
    def test_unkown_status(self):
        with pytest.raises(ValueError):
            invalidTask = Task(
                title = "Check Default Status",
                description= "checking default value",
                status="fail"
            )