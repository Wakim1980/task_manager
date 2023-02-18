from dataclasses import dataclass


@dataclass
class User:
    id: int
    login: str
    pass_hash: str
    last_name: str
    first_name: str
    email: str

    def __str__(self):
        return f"{self.id} {self.login} {self.last_name} {self.first_name} {self.email}"


