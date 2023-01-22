from dataclasses import dataclass #модуль для @dataclass
from datetime import datetime


@dataclass
class Task:
    id: int
    name: str
    priority: bool
    description: str
    execution_date: datetime


