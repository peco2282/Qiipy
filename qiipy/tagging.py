from typing import Dict, Any, List, Optional, TYPE_CHECKING


class Tagging:
    def __init__(self, data: Dict[str, Any]):
        self.data = data
        # self.name: str = data.get("name")
        # self.versions: List[Optional[str]] = data.get("versions")

    def __repr__(self) -> str:
        return (
            f"<Tagging name={self.name}>"
        )

    @property
    def name(self) -> str:
        return self.data.get("name")

    @property
    def versions(self) -> List[str]:
        return self.data.get("versions")
