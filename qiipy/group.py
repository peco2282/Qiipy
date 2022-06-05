from datetime import datetime
from typing import Dict, Any

from .team import Team


class Group:
    def __init__(self, data: Dict[str, Any]):
        self.data = data
        # self.__created_at: str = data.get("created_at")
        # self.created_at: datetime = datetime.strptime(self.__created_at, "%Y-%m-%dT%H:%M:%S%z")
        # self.description: str = data.get("description")
        # self.name: str = data.get("name")
        # self.private: bool = True if str(data.get("private")) == "True" else False
        # self.__updated_at: str = data.get("updated_at")
        # self.updated_at: datetime = datetime.strptime(self.__updated_at, "%Y-%m-%dT%H:%M:%S%z")
        # self.url_name: str = data.get("url_name")

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
        return True if self.data.get("private").lower() == "True" else False

    @property
    def updated_at(self) -> datetime:
        _updated_at = self.data.get("updated_at")
        return datetime.strptime(_updated_at, "%Y-%m-%dT%H:%M:%S%z")

    @property
    def url_name(self) -> str:
        return self.data.get("url_name")
