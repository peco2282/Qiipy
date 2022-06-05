[![PyPI](https://img.shields.io/pypi/v/pyqiita)](https://pypi.org/project/pyqiita)
[![GitHub](https://img.shields.io/github/license/peco2282/qiipy)](https://github.com/peco2282/Qiipy/blob/main/license)
# pyqiita

This is an API wrapper for Qiita API v2.
# How to install
> on your console...
```bash
pip install pyqiita
```

## Usage...
example
```python
from qiipy import Client

client = Client(token="Your_Qiita_Access_Token")
user = client.get_authenticated_user_data()
print("my name is " + user.id)

---
my name is peco_2282
```

### How to get Qiita API Token ?
1. [Look at this url](https://qiita.com/settings/applications).
2. Select `Applications`.
3. Get Access Token from `Personal access tokens`
