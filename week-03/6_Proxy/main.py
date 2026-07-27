from typing import Any


class Proxy:
    def __init__(self, obj: object) -> None:
        self._obj = obj
        self._last_accessed = None
        self._access_counts = {}

    def __getattr__(self, name: str) -> Any:
        if not hasattr(self._obj, name):
            raise AttributeError("No such attribute.")

        self._last_accessed = name
        self._access_counts[name] = self._access_counts.get(name, 0) + 1
        return getattr(self._obj, name)

    def last_accessed_attribute(self) -> str:
        if self._last_accessed is None:
            raise Exception("No attribute was accessed.")
        return self._last_accessed

    def count_of_accesses(self, attribute_name: str) -> int:
        return self._access_counts.get(attribute_name, 0)

    def was_accessed(self, attribute_name: str) -> bool:
        return self.count_of_accesses(attribute_name) > 0
