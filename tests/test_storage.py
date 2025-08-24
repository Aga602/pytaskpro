import pytest
from app.storage import Jsonio

class TestJsonio:
    path = "tests/test_tasks.json"
    def test_read_json(self):
        client = Jsonio(self.path)
        file_read = client.read_json()
        assert len(file_read) == 1
    
    def test_read_jsonnotpresent(self):
        client = Jsonio("tests/test_task.json")  
        with pytest.raises(FileNotFoundError):
            client.read_json()
    
    def test_wite_to_json(self):
        client = Jsonio(self.path)
        data = [
            {
                "eat_brakfast": {
                            "title": "Eat Breakfast",
                            "description": "Eat first meal of the day",
                            "status": "repeat"
                }
            }
        ]
        
        client.write_json(
            data= data
        )
        
        assert client.read_json() == data
        
        
        
        