from typing import Optional, Dict, Any


class User:
    def __init__(self, data: Dict[str, Any]):
        self.data: Dict[str, Any] = data

    def __repr__(self) -> str:
        return (
            f"<User user_id={self.id} followees_count={self.followees_count}"
            f" followers_count={self.followers_count} items_count={self.items_count}>"
        )

    @property
    def description(self) -> Optional[str]:
        return self.data.get("description")

    @property
    def facebook_id(self) -> Optional[str]:
        return self.data.get("facebook_id")

    @property
    def followees_count(self) -> int:
        return int(self.data.get("followees_count"))

    @property
    def followers_count(self) -> int:
        return int(self.data.get("followers_count"))

    @property
    def github_login_name(self) -> Optional[str]:
        return self.data.get("github_login_name")

    @property
    def id(self) -> str:
        return self.data.get("id")

    @property
    def items_count(self) -> int:
        return int(self.data.get("items_count"))

    @property
    def linkedin_id(self) -> Optional[str]:
        return self.data.get("linkedin_id")

    @property
    def location(self) -> Optional[str]:
        return self.data.get("location")

    @property
    def name(self) -> Optional[str]:
        return self.data.get("name")

    @property
    def organization(self) -> Optional[str]:
        return self.data.get("organization")

    @property
    def permanent_id(self) -> str:
        return self.data.get("permanent_id")

    @property
    def profile_image_url(self) -> str:
        return self.data.get("profile_image_url")

    @property
    def team_only(self) -> bool:
        return True if self.data.get("team_only").lower() == "true" else False

    @property
    def twitter_screen_name(self) -> Optional[str]:
        return self.data.get("twitter_screen_name")

    @property
    def website_url(self) -> Optional[str]:
        return self.data.get("website_url")

    @property
    def image_monthly_upload_limit(self) -> Optional[int]:
        limit = self.data.get("image_monthly_upload_limit")
        return int(limit) if limit is not None else None

    @property
    def image_monthly_upload_remaining(self) -> Optional[int]:
        remain = self.data.get("image_monthly_upload_remaining")
        return int(remain) if remain is not None else None
