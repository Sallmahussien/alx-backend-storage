#!/usr/bin/env python3
"""Defines Cache class"""

import redis
import uuid
from functools import wraps
from typing import Union, Callable


def count_calls(method: Callable) -> Callable:
    """Decorator to count the number of times a method is called."""

    @wraps(method)
    def wrapper(self, *args, **kwds):
        """Wrapper function for the decorated method."""
        if isinstance(self._redis, redis.Redis):
            self._redis.incr(method.__qualname__)

        return method(self, *args, **kwds)

    return wrapper


def call_history(method: Callable) -> Callable:
    """"""

    @wraps(method)
    def wrapper(self, *args, **kwds):
        """"""
        generated_key = method(self, *args, **kwds)

        if isinstance(self._redis, redis.Redis):
            self._redis.rpush(f"{method.__qualname__}:inputs", str(args))
            self._redis.rpush(f"{method.__qualname__}:outputs", generated_key)

        return generated_key

    return wrapper


class Cache:
    """The implementation of Cash class"""
    def __init__(self) -> None:
        """Initialize a new object from Cash class"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Takes a data argument and returns a string"""
        generated_key = str(uuid.uuid4())
        self._redis.set(generated_key, data)
        return generated_key

    def get(self, key: str, fn: Union[Callable, None] = None) -> str:
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
