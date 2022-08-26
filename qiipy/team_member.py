from datetime import datetime
from typing import Dict, Any

from .member import Member


class TeamMember(Member):
    def __init__(self, data: Dict[str, Any]):
        super().__init__(data)

    @property
    def description(self) -> str:
        return self.data.get("description")

    @property
    def last_accessed_at(self) -> datetime:
        _last: str = self.data.get("last_accessed_at")
        return datetime.strptime(_last, "%Y-%m-%dT%H:%M:%S%z")
