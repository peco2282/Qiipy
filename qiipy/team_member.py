from datetime import datetime
from typing import Dict, Any

from .member import Member


class TeamMember(Member):
    def __init__(self, data: Dict[str, Any]):
        super().__init__(data)
        # self.description: str = data.get("description")
        # self.__last_accessed_at: str = data.get("last_accessed_at")
        # self.last_accessed_at: datetime = datetime.strptime(self.__last_accessed_at, "%Y-%m-%dT%H:%M:%S%z")

    @property
    def description(self) -> str:
        return self.data.get("description")

    @property
    def last_accessed_at(self) -> datetime:
        _last: str = self.data.get("last_accessed_at")
        return datetime.strptime(_last, "%Y-%m-%dT%H:%M:%S%z")
