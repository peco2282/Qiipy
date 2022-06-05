from datetime import datetime
from typing import Dict, Any, Optional


class Project:
    def __init__(self, data: Dict[str, Any]):
        self.data = data
        # self.rendered_body: str = data.get("rendered_body")
        # self.archived: bool = True if str(data.get("archived")) == "True" else False
        # self.body = data.get("body")
        # self.__created_at: str = data.get("created_at")
        # self.created_at: datetime = datetime.strptime(self.__created_at, "%Y-%m-%dT%H:%M:%S%z")
        # self.id = data.get("id")
        # self.name = data.get("name")
        # self.reactions_count = data.get("reactions_count")
        # self.__updated_at: str = data.get("updated_at")
        # self.updated_at: datetime = datetime.strptime(self.__updated_at, "%Y-%m-%dT%H:%M:%S%z")

    @property
    def rendered_body(self) -> str:
        return self.data.get("rendered_body")

    @property
    def is_archived(self) -> bool:
        return True if self.data.get("archived").lower() == "true" else False

    @property
    def body(self) -> str:
        return self.data.get("body")

    @property
    def created_at(self) -> datetime:
        _created_at = self.data.get("created_at")
        return datetime.strptime(_created_at, "%Y-%m-%dT%H:%M:%S%z")

    @property
    def id(self) -> str:
        return self.data.get("id")

    @property
    def name(self) -> str:
        return self.data.get("name")

    @property
    def reactions_count(self) -> Optional[int]:
        count: str = self.data.get("reactions_count")
        return int(count) if count.isdigit() else None

    @property
    def updated_at(self) -> datetime:
        _updated_at = self.data.get("updated_at")
        return datetime.strptime(_updated_at, "%Y-%m-%dT%H:%M:%S%z")


