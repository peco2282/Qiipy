from typing import Dict, Any


class Team:
    def __init__(self, data: Dict[str, Any]):
        self.data = data
        # self.is_active: bool = True if str(data.get("active")) == "True" else False
        # self.id: str = data.get("id")
        # self.name: str = data.get("name")

    def __repr__(self):
        return (
            f"<Team name={self.name} id={self.id} active={self.is_active}>"
        )

    @property
    def is_active(self) -> bool:
        return True if self.data.get("is_active").lower() == "true" else False

    @property
    def id(self) -> str:
        return self.data.get("id")

    @property
    def name(self) -> str:
        return self.data.get("name")

