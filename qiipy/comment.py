from datetime import datetime
from typing import Any, Dict

from .user import User


class Comment:
    def __init__(self, data: Dict[str, Any]):
        self.data = data

    @property
    def body(self) -> str:
        return self.data.get("body")

    @property
    def created_at(self) -> datetime:
        _created_at: str = self.data.get("created_at")
        return datetime.strptime(_created_at, "%Y-%m-%dT%H:%M:%S%z")

    @property
    def id(self) -> str:
        return self.data.get("id")

    @property
    def rendered_body(self) -> str:
        return self.data.get("rendered_body")

    @property
    def updated_at(self) -> datetime:
        _updated_at = self.data.get("updated_at")
        return datetime.strptime(_updated_at, "%Y-%m-%dT%H:%M:%S%z")

    @property
    def user(self) -> User:
        return User(self.data.get("user"))
