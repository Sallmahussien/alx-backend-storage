#!/usr/bin/env python3
"""Defines Cache class"""

import redis
import uuid
from typing import Union, Callable


class Cache:
    """The implementation of Cash class"""
    def __init__(self) -> None:
        """Initialize a new object from Cash class"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Takes a data argument and returns a string"""
        generated_key = str(uuid.uuid4())
        self._redis.set(generated_key, data)
        return generated_key

    def get(self, key: str, fn: Callable) -> str:
        """Retrieves and type-converts the value of a specific key using fn"""
        value = self._redis.get(key)

        if fn:
            return fn(value)

        return value

    def get_str(self, key: str) -> str:
        """Retrieves and type-converts the value of a specific key to str."""
        return self.get(key, lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> int:
        """Retrieves and type-converts the value of a specific key to int."""
        return self.get(key, int)
