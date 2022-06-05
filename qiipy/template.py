from typing import Any, Dict, List, Union

from .tagging import Tagging
from .group import Group


class Template:
    def __init__(self, data: Dict[str, Any]):
        self.data = data
        # self.body: str = data.get("body")
        # self.id: int = int(data.get("id"))
        # self.name: str = data.get("name")
        # self.expanded_body: str = data.get("expanded_body")
        # self.expanded_tags: List[Dict[str, Union[str, List[str]]]] = data.get("expanded_tags")
        # self.expanded_title: str = data.get("expanded_title")
        # self.group: Group = data.get("group")
        # self.tags: List[Dict[str, Union[str, List[str]]]] = data.get("tags")
        # self.title: str = data.get("title")
        # self.coedit: bool = True if str(data.get("coedit")) == "True" else False

    @property
    def body(self) -> str:
        return self.data.get("body")

    @property
    def id(self) -> int:
        _id: str = self.data.get("id")
        return int(_id) if _id.isdigit() else None

    @property
    def name(self) -> str:
        return self.data.get("name")

    @property
    def expanded_body(self) -> str:
        return self.data.get("expanded_body")

    @property
    def expanded_tags(self) -> Tagging:
        return Tagging(self.data.get("expanded_tags"))

    @property
    def expanded_title(self) -> str:
        return self.data.get("expanded_title")

    @property
    def group(self) -> Group:
        return Group(self.data.get("group"))

    @property
    def tags(self) -> Tagging:
        return Tagging(self.data.get("tags"))

    @property
    def title(self) -> str:
        return self.data.get("title")

    @property
    def coedit(self) -> bool:
        return True if self.data.get("coedit").lower() == "true" else False
