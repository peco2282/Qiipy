from datetime import datetime
from typing import Dict, Any, Optional


class Project:
    def __init__(self, data: Dict[str, Any]):
        self.data = data

    @property
    def rendered_body(self) -> str:
        return self.data.get("rendered_body")

    @property
    def is_archived(self) -> bool:
        return self.data.get("archived", False)

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
        return int(self.data.get("reactions_count", 0))

    @property
    def updated_at(self) -> datetime:
        _updated_at = self.data.get("updated_at")
        return datetime.strptime(_updated_at, "%Y-%m-%dT%H:%M:%S%z")


