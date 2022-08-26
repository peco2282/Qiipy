import requests
from requests import Response

BASE = "https://qiita.com/api/v2/"


class Session:
    def __init__(
            self,
            method: str,
            path: str,
            token: str,
            *args,
            **kwargs
    ):
        __method_type__ = {
            "GET",
            "POST",
            "DELETE",
            "PUT",
            "PATCH"
        }
        if method not in __method_type__:
            raise TypeError(f"This method not in {__method_type__}")

        self.method = method
        self.path = path
        self.token = token

        self.url = BASE + self.path

        self.headers = {
            "Authorization": f"Bearer {self.token}"
            # "Content-Type": "application/json"
        }

        data = requests.request(
            method=method,
            url=self.url,
            headers=self.headers,
            json=kwargs.get("json")
        )
        self.data = data

    @property
    def base(self) -> str:
        return BASE

    @property
    def response(self) -> Response:
        return self.data

