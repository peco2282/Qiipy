from typing import Dict, Any


class Member:
    def __init__(self, data: Dict[str, Any]):
        self.data = data
        # self.id: str = data.get("id")
        # self.name: str = data.get("name")
        # self.email: str = data.get("email")

    @property
    def id(self) -> str:
        return self.data.get("id")

    @property
    def name(self) -> str:
        return self.data.get("name")

    @property
    def email(self) -> str:
        return self.data.get("email")
