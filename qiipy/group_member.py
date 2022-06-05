from typing import Dict, Any

from .member import Member


class GroupMember(Member):
    def __init__(self, data: Dict[str, Any]):
        super().__init__(data)
