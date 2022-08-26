from enum import Enum
from typing import List, Optional

from . import Group, GroupMember, Comment, Tagging, Team, TeamMember, Template, Project
from .exception import InvalidItemsRequested
from .item import Item
from .session import Session
from .tag import Tag
from .user import User


class Sort(Enum):
    COUNT = "count"
    NAME = "name"


class Client:
    def __init__(
            self,
            token
    ):
        if not isinstance(token, str):
            raise TypeError(
                f"token must be str, not {token.__class__.__name__}"
            )
        self.token = token

    # グループ
    def get_groups(self, page: int = 1, items: int = 20) -> List[Group]:
        if items > 100 | items <= 0:
            raise InvalidItemsRequested(
                "Too many items were requested. You can request more than 1 and less than 100."
            )

        response = Session(
            method="GET",
            token=self.token,
            path=f"groups?page={page}&per_page={items}"
        )
        return [Group(group) for group in response.response.json()]

    def get_group(self, url_name: str) -> Group:
        response = Session(
            method="GET",
            token=self.token,
            path=f"groups/{url_name}"
        )
        return Group(response.response.json())

    def create_group(self) -> None:
        pass

    def update_group(self) -> None:
        pass

    def delete_group(self, url_name: str) -> None:
        response = Session(
            method="DELETE",
            token=self.token,
            path=f"groups/{url_name}"
        )
        if response.response.status_code == 204:
            ...

    # グループメンバー
    def get_members(
            self,
            url_name: str,
            page: int = 1,
            items: int = 20
    ) -> List[GroupMember]:
        if items > 100 | items <= 0:
            raise InvalidItemsRequested(
                "Too many items were requested. You can request more than 1 and less than 100."
            )
        response = Session(
            method="GET",
            token=self.token,
            path=f"groups/{url_name}/members?page={page}&per_page={items}"
        )
        return [GroupMember(member) for member in response.response.json()]

    def get_member(
            self,
            url_name: str,
            user_id: str
    ) -> GroupMember:
        response = Session(
            method="GET",
            token=self.token,
            path=f"groups/{url_name}/members/{user_id}"
        )
        return GroupMember(response.response.json())

    def add_member(
            self,
            url_name: str,
            user_id: str = None,
            email: str = None
    ):
        json = dict()
        if user_id:
            json["identities"] = [user_id]

        elif email:
            json["identities"] = [email]

        else:
            raise ValueError()

        response = Session(
            method="POST",
            token=self.token,
            path=f"groups/{url_name}/members",
            json=json
        )

    def delete_member(
            self,
            url_name: str,
            user_id: str = None,
            email: str = None
    ):
        json = dict()
        if user_id:
            json["identities"] = [user_id]

        elif email:
            json["identities"] = [email]

        else:
            raise ValueError()

        response = Session(
            method="DELETE",
            token=self.token,
            path=f"groups/{url_name}/members",
            json=json
        )

    # コメント
    def delete_comment(
            self,
            comment_id: str
    ) -> bool:
        response = Session(
            method="DELETE",
            token=self.token,
            path=f"comments/{comment_id}"
        )
        if response.response.status_code == 404:
            return True

        return False

    def get_comment(
            self,
            comment_id: str
    ) -> Optional[Comment]:
        response = Session(
            method="GET",
            token=self.token,
            path=f"comments/{comment_id}"
        )
        if response.response.status_code == 200:
            return Comment(response.response.json())
        return None

    def get_comments(
            self,
            item_id: str
    ) -> Optional[List[Comment]]:
        response = Session(
            method="GET",
            token=self.token,
            path=f"items/{item_id}/comments"
        )
        if response.response.status_code == 200:
            return [Comment(comment) for comment in response.response.json()]
        return None

    def post_comment(
            self,
            item_id: str,
            comment: str
    ) -> Optional[Comment]:
        response = Session(
            method="POST",
            token=self.token,
            path=f"items/{item_id}/comments"
        )
        if response.response.status_code == 201:
            return Comment(response.response.json())
        return None

    def post_user_comment(self, item_id: str): ...

    def get_project_comments(
            self,
            project_id: str
    ) -> Optional[Comment]:
        response = Session(
            method="GET",
            token=self.token,
            path=f"projects/{project_id}/comments"
        )
        if response.response.status_code == 200:
            return Comment(response.response.json())
        return None

    def post_project_comment(
            self,
            project_id: str,
            comment: str
    ) -> Optional[Comment]:
        response = Session(
            method="POST",
            token=self.token,
            path=f"projects/{project_id}",
            json={"body": comment}
        )
        if response.response.status_code == 201:
            return Comment(response.response.json())
        return None

    def post_user_project_comment(
            self,
            project_id: str,
            comment: str,
            user_id: str
    ) -> Optional[Comment]:
        response = Session(
            method="POST",
            token=self.token,
            path=f"projects/{project_id}/imported_comments",
            json={"body": comment, "user_id": user_id}
        )
        if response.response.status_code == 201:
            return Comment(response.response.json())
        return None

    def edit_comment(
            self,
            comment_id: str,
            comment: str
    ) -> Optional[Comment]:
        response = Session(
            method="PATCH",
            token=self.token,
            path=f"comments/{comment_id}",
            json={"body": comment}
        )
        if response.response.status_code == 200:
            return Comment(response.response.json())
        return None

    # タギング
    def set_tag(
            self,
            item_id: str,
            tag_name: str,
            versions: List[str] = None
    ) -> Optional[Tagging]:
        json = dict()
        json["name"] = tag_name
        if versions:
            json["versions"] = versions
        response = Session(
            method="POST",
            token=self.token,
            path=f"items/{item_id}/tagging",
            json=json
        )
        if response.response.status_code == 201:
            return Tagging(response.response.json())
        return None

    def delete_tag(
            self,
            item_id: str,
            tagging_id: str
    ) -> bool:
        response = Session(
            method="DELETE",
            token=self.token,
            path=f"items/{item_id}/tagging/{tagging_id}"
        )
        if response.response.status_code == 204:
            return True
        return False

    # タグ
    def get_tag(
            self,
            tag_id: str
    ) -> Optional[Tag]:
        response = Session(
            method="GET",
            token=self.token,
            path=f"tags/{tag_id}"
        )
        if response.response.status_code == 200:
            return Tag(response.response.json())
        return None

    def get_tags(self, sort: Sort, page: int = 1, items: int = 20) -> Optional[List[Tag]]:
        if items > 100 | items <= 0:
            raise InvalidItemsRequested("Too many items were requested. You can request more than 1 and less than 100.")
        sort = sort.value
        response = Session(
            method="GET",
            token=self.token,
            path=f"tags?page={page}&per_page={items}"
        )
        if response.response.status_code == 204:
            return [Tag(data) for data in response.response.json()]
        return None

    def get_following_tags(
            self,
            user_id: str,
            page: int = 1,
            items: int = 20
    ) -> Optional[List[Tag]]:
        if items > 100 | items <= 0:
            raise InvalidItemsRequested(
                "Too many items were requested. You can request more than 1 and less than 100."
            )
        response = Session(
            method="GET",
            token=self.token,
            path=f"users/{user_id}/following_tags?page={page}&per_page={items}"
        )
        if response.response.status_code == 200:
            return [Tag(tag) for tag in response.response.json()]
        return None

    def delete_following_tag(
            self,
            tag_id: str
    ) -> bool:
        response = Session(
            method="DELETE",
            token=self.token,
            path=f"tags/{tag_id}/following"
        )
        if response.response.status_code == 200:
            return True
        return False

    def follow_tag(
            self,
            tag_id: str
    ) -> bool:
        response = Session(
            method="PUT",
            token=self.token,
            path=f"tags/{tag_id}/following"
        )
        if response.response.status_code == 204:
            return True
        return False

    # チーム
    def get_user_teams(self) -> Optional[List[Team]]:
        response = Session(
            method="GET",
            token=self.token,
            path=f"teams"
        )
        if response.response.status_code == 200:
            return [Team(team) for team in response.response.json()]
        return None

    # チームメンバー
    def get_team_members(
            self,
            items: int = 1,
            page: int = 20
    ) -> Optional[List[TeamMember]]:
        if items > 100 | items <= 0:
            raise InvalidItemsRequested(
                "Too many items were requested. You can request more than 1 and less than 100."
            )
        response = Session(
            method="GET",
            token=self.token,
            path=f"team_memberships?page={items}&per_page={page}"
        )
        if response.response.status_code == 200:
            return [TeamMember(member) for member in response.response.json()]
        return None

    # テンプレート
    def get_templates(
            self,
            page: int = 1,
            items: int = 20
    ) -> Optional[List[Template]]:
        if items > 100 | items <= 0:
            raise InvalidItemsRequested(
                "Too many items were requested. You can request more than 1 and less than 100."
            )
        response = Session(
            method="GET",
            token=self.token,
            path=f"templates?page={page}&per_page={items}"
        )
        if response.response.status_code == 200:
            return [Template(temp) for temp in response.response.json()]
        return None

    def delete_template(
            self,
            template_id: str
    ):
        response = Session(
            method="DELETE",
            token=self.token,
            path=f"templates/{template_id}"
        )
        if response.response.status_code == 200:
            return True
        return False

    def get_template(
            self,
            template_id: str
    ) -> Optional[Template]:
        response = Session(
            method="GET",
            token=self.token,
            path=f"templates/{template_id}"
        )
        if response.response.status_code == 200:
            return Template(response.response.json())
        return None

    def add_template(self): ...

    def update_template(self): ...

    def get_projects(
            self,
            page: int = 1,
            items: int = 20
    ) -> Optional[List[Project]]:
        if items > 100 | items <= 0:
            raise InvalidItemsRequested(
                "Too many items were requested. You can request more than 1 and less than 100."
            )
        response = Session(
            method="GET",
            token=self.token,
            path=f"projects?page={page}&per_page={items}"
        )
        if response.response.status_code == 200:
            return [Project(project) for project in response.response.json()]
        return None

    def add_project(self): ...

    def delete_project(self): ...

    def get_project(
            self,
            project_id: str
    ) -> Optional[Project]:
        response = Session(
            method="GET",
            token=self.token,
            path=f"projects/{project_id}"
        )
        if response.response.status_code == 200:
            return Project(response.response.json())
        return None

    def update_project(self): ...

    # ユーザー
    def get_authenticated_user_data(self) -> User:
        response = Session(
            method="GET",
            token=self.token,
            path="authenticated_user"
        )
        return User(response.response.json())

    def get_stockers(
            self,
            item_id: str,
            page: int = 1,
            items: int = 20
    ) -> Optional[List[Item]]:
        if items > 100 | items <= 0:
            raise InvalidItemsRequested(
                "Too many items were requested. You can request more than 1 and less than 100."
            )

        response = Session(
            method="GET",
            token=self.token,
            path=f"items/{item_id}/stockers?page={page}&per_page={items}"
        )
        if response.response.status_code == 200:
            return [User(item) for item in response.response.json()]
        return None

    def get_user(
            self,
            user_id: str
    ) -> Optional[User]:
        response = Session(
            method="GET",
            token=self.token,
            path=f"users/{user_id}"
        )
        if response.response.status_code == 200:
            return User(response.response.json())
        return None

    def get_users(
            self,
            page: int = 1,
            items: int = 20
    ) -> Optional[List[User]]:
        if items > 100 | items <= 0:
            raise InvalidItemsRequested(
                "Too many items were requested. You can request more than 1 and less than 100."
            )

        response = Session(
            method="",
            token=self.token,
            path=f"users?page={page}&per_page={items}"
        )
        if response.response.status_code == 200:
            return [User(json) for json in response.response.json()]
        return None

    def get_followees(
            self,
            user_id: str,
            page: int = 1,
            items: int = 20
    ) -> Optional[List[User]]:
        if items > 100 | items <= 0:
            raise InvalidItemsRequested(
                "Too many items were requested. You can request more than 1 and less than 100."
            )

        response = Session(
            method="GET",
            token=self.token,
            path=f"users/{user_id}/followees?page={page}&per_page={items}"
        )
        if response.response.status_code == 200:
            return [User(json) for json in response.response.json()]
        return None

    def get_followers(
            self,
            user_id: str,
            page: int = 1,
            items: int = 20
    ) -> Optional[List[User]]:
        if items > 100 | items <= 0:
            raise InvalidItemsRequested(
                "Too many items were requested. You can request more than 1 and less than 100."
            )

        response = Session(
            method="GET",
            token=self.token,
            path=f"users/{user_id}/followers?page={page}&per_page={items}"
        )
        if response.response.status_code == 200:
            return [User(json) for json in response.response.json()]
        return None

    def delete_following(
            self,
            user_id: str
    ) -> bool:
        response = Session(
            method="DELETE",
            token=self.token,
            path=f"users/{user_id}/following"
        )
        if response.response.status_code == 204:
            return True
        return False

    def is_following(
            self,
            user_id: str
    ) -> bool:
        response = Session(
            method="GET",
            token=self.token,
            path=f"users/{user_id}/following"
        )
        if response.response.status_code == 204:
            return True
        return False

    def set_following(
            self,
            user_id: str
    ) -> bool:
        response = Session(
            method="PUT",
            token=self.token,
            path=f"users/{user_id}/following"
        )
        if response.response.status_code == 204:
            return True
        return False

    # 投稿
    def get_item(
            self,
            item_id: str
    ) -> Item:
        response = Session(
            "GET",
            token=self.token,
            path=f"items/{item_id}"
        )
        if response.response.status_code == 200:
            return Item(response.response.json())
        return None

    def get_items(
            self,
            page: int = 1,
            items: int = 20
    ) -> List[Item]:
        if items > 100 | items <= 0:
            raise InvalidItemsRequested(
                "Too many items were requested. You can request more than 1 and less than 100."
            )

        response = Session(
            method="GET",
            token=self.token,
            path=f"authenticated_user/items?page={page}&per_page={items}"
        )
        if response.response.status_code == 200:
            return [Item(json) for json in response.response.json()]
        return None

    def delete_item(
            self,
            item_id: str
    ) -> bool:
        response = Session(
            method="DELETE",
            token=self.token,
            path=f"items/{item_id}"
        )
        if response.response.status_code == 200:
            return True
        return False

    def is_stock(
            self,
            item_id: str
    ) -> bool:
        response = Session(
            method="GET",
            token=self.token,
            path=f"items/{item_id}/stock"
        )
        if response.response.status_code == 204:
            return True
        return False

    def set_stock(
            self,
            item_id: str
    ) -> bool:
        response = Session(
            method="PUT",
            token=self.token,
            path=f"items/{item_id}/stock"
        )
        if response.response.status_code == 204:
            return True
        return False

    def get_tagging_items(
            self,
            tag_id: str,
            page: int = 1,
            items: int = 20
    ) -> Optional[List[Item]]:
        if items > 100 | items <= 0:
            raise InvalidItemsRequested("Too many items were requested. You can request more than 1 and less than 100.")
        response = Session(
            method="GET",
            token=self.token,
            path=f"tags/{tag_id}/items?page={page}&per_page={items}"
        )
        if response.response.status_code == 200:
            return [Item(item) for item in response.response.json()]
        return None

