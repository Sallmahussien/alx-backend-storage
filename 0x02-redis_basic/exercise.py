#!/usr/bin/env python3
"""Defines Cache class"""

import redis
import uuid
from typing import Union


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
