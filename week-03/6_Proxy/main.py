class Proxy:
    def __init__(self, obj: object) -> None:
        self._obj = obj

    def last_accessed_attribute(self) -> str:
        ...

    def count_of_accesses(self, attribute_name: str) -> int:
        ...

    def was_accessed(self, attribute_name: str) -> bool:
        ...
