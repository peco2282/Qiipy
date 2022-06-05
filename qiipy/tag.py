from typing import Dict, Any


class Tag:
    def __init__(self, data: Dict[str, Any]):
        self.data = data
        # self.followers_count = data.get("followers_count")
        # self.icon_url = data.get("icon_url")
        # self.id = data.get("id")
        # self.items_count = data.get("items_count")

    def __repr__(self):
        return (
            f"<Tag id={self.id} followers={self.followers_count} items={self.items_count}>"
        )

    @property
    def followers_count(self) -> int:
        return int(self.data.get("followers_count"))

    @property
    def icon_url(self) -> str:
        return self.data.get("icon_url")

    @property
    def id(self) -> str:
        return self.data.get("id")

    @property
    def items_count(self) -> int:
        return int(self.data.get("items_count"))
