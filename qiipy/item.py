from datetime import datetime
from typing import Dict, Any, Optional

from .member import Member
from .tagging import Tagging
from .team import Team
from .user import User


class Item:
    def __init__(self, data: Dict[str, Any]):
        self.data = data
        # self.rendered_body: str = data.get("rendered_body")
        # self.body: str = data.get("body")
        # self.coediting: bool = data.get("coediting")
        # self.comments_count: int = int(data.get("comments_count"))
        # self.__created_at: str = data.get("created_at")
        # self.created_at: datetime = datetime.strptime(self.__created_at, "%Y-%m-%dT%H:%M:%S%z")
        # self.group: Team = data.get("group")
        # self.id: str = data.get("id")
        # self.likes_count: int = int(data.get("likes_count"))
        # self.private: bool = True if str(data.get("private")) == "True" else False
        # self.reactions_count: int = int(data.get("reactions_count"))
        # self.tags: List[Dict[str, Union[str, List[str]]]] = data.get("tags")
        # self.title: str = data.get("title")
        # self.__updated_at: str = data.get("updated_at")
        # self.updated_at: datetime = datetime.strptime(self.__updated_at, "%Y-%m-%dT%H:%M:%S%z")
        # self.url: str = data.get("url")
        # self.user: User = User(data.get("user"))
        # self.page_views_count: Optional[int] = int(data.get("page_views_count"))
        # self.team_membership: Member = data.get("team_membership")

    def __repr__(self) -> str:
        return (
            f"<Item user_id={self.user.id} article_id={self.id}"
            f" views_count={self.page_views_count} url={self.url}>"
        )

    @property
    def rendered_body(self) -> str:
        return self.data.get("rendered_body")

    @property
    def body(self) -> str:
        return self.data.get("body")

    @property
    def coediting(self) -> bool:
        if self.data.get("coediting").lower() == "true":
            return True
        return False

    @property
    def comments_count(self) -> int:
        return int(self.data.get("comments_count"))

    @property
    def created_at(self) -> datetime:
        _created_at: str = self.data.get("created_at")
        return datetime.strptime(_created_at, "%Y-%m-%dT%H:%M:%S%z")

    @property
    def group(self) -> Team:
        return Team(self.data.get("group"))

    @property
    def id(self) -> str:
        return self.data.get("id")

    @property
    def likes_count(self) -> int:
        return int(self.data.get("likes_count"))

    @property
    def private(self) -> bool:
        if self.data.get("private") == "True":
            return True
        return False

    @property
    def reactions_count(self) -> int:
        return int(self.data.get("reactions_count"))

    @property
    def tags(self) -> Tagging:
        return Tagging(self.data.get("tags"))

    @property
    def title(self) -> str:
        return self.data.get("title")

    @property
    def updated_at(self) -> datetime:
        _updated_at = self.data.get("updated_at")
        return datetime.strptime(_updated_at, "%Y-%m-%dT%H:%M:%S%z")

    @property
    def url(self) -> str:
        return self.data.get("url")

    @property
    def user(self) -> User:
        return User(self.data.get("user"))

    @property
    def page_views_count(self) -> Optional[int]:
        count: str = self.data.get("page_views_count")
        return int(count) if count else None

    @property
    def team_membership(self) -> Member:
        return Member(self.data.get("team_membership"))

