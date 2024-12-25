from pydantic import BaseModel, Field
from typing import Optional

class Task(BaseModel):
    id: int
    title: str
    completed: bool = False

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "title": "Завершить проект",
                "completed": False
            }
        }
