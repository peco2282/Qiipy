import json

import requests

BASE = "https://qiita.com/api/v2"

token = "6ed96829083437217f9c077c61d225fcb619d7ca"
Auth = {"Authorization": f"Bearer {token}"}

url = BASE + "/authenticated_user"

data = dict()

data["Auth"] = f"Bearer {token}"

r = requests.get(url=url, headers=Auth)
print(r)
print(r.json())
