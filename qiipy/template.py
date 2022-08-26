from typing import Any, Dict, List, Union

from .tagging import Tagging
from .group import Group


class Template:
    def __init__(self, data: Dict[str, Any]):
        self.data = data

    @property
    def body(self) -> str:
        return self.data.get("body")

    @property
    def id(self) -> int:
        return int(self.data.get("id", 0))

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
        return self.data.get("coedit", False)
