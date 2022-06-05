from datetime import datetime
from typing import Dict, Any

from .user import User


class Reaction:
    def __init__(self, data: Dict[str, Any]):
        self.data = data
        # self.__created_at: str = data.get("created_at")
        # self.created_at: datetime = datetime.strptime(self.__created_at, "%Y-%m-%dT%H:%M:%S%z")
        # self.image_url: str = data.get("image_url")
        # self.name: str = data.get("name")
        # self.user: User = data.get("user")

    @property
    def created_at(self) -> datetime:
        _created_at: str =  self.data.get("created_at")
        return datetime.strptime(_created_at, "%Y-%m-%dT%H:%M:%S%z")

    @property
    def image_url(self) -> str:
        return self.data.get("image_url")

    @property
    def name(self) -> str:
        return self.data.get("name")

    @property
    def user(self) -> User:
        return User(self.data.get("user"))
