from dataclasses import dataclass #модуль для @dataclass
from datetime import datetime


@dataclass
class Task:
    id: int
    name: str
    priority: bool
    description: str
    execution_date: datetime
    task_completed: bool = False

    def __str__(self):
        return f"{self.id} {self.name} {self.priority} {self.description} {self.execution_date} {self.task_completed}"



