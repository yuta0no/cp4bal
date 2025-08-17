from typing import Generic, TypeVar

T = TypeVar("T")


class Cache(Generic[T]):
    def __init__(self):
        self._cache: T | None = None

    def get(self) -> T | None:
        return self._cache

    def update(self, value: T):
        self._cache = value

    def reset(self):
        self._cache = None
