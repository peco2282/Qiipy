from datetime import datetime
from typing import Dict, Any

from .team import Team


class Group:
    def __init__(self, data: Dict[str, Any]):
        self.data = data

    def __repr__(self) -> str:
        return (
            f"<Group group_name={self.name} description={self.description}>"
        )

    @property
    def created_at(self) -> datetime:
        _created_at: str = self.data.get("created_at")
        return datetime.strptime(_created_at, "%Y-%m-%dT%H:%M:%S%z")

    @property
    def description(self) -> str:
        return self.data.get("description")

    @property
    def name(self) -> str:
        return self.data.get("name")

    @property
    def private(self) -> bool:
        return self.data.get("private", False)

    @property
    def updated_at(self) -> datetime:
        _updated_at = self.data.get("updated_at")
        return datetime.strptime(_updated_at, "%Y-%m-%dT%H:%M:%S%z")

    @property
    def url_name(self) -> str:
        return self.data.get("url_name")
