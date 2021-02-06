# coding: utf-8
import typing

__all__ = ['memory_cache']


class _MemoryCache:
    """A simple cache that save key-value data in memory."""
    def __init__(self):
        self._cache = dict()

    def __setitem__(self, key: str, value: typing.Any):
        self._cache[key] = value

    def __getitem__(self, key: str):
        return self._cache.get(key, None)


memory_cache = _MemoryCache()
