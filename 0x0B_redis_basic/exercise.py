#!/usr/bin/env python3
'''
module using redis to create simple cache and
use for basic exercises
'''
import redis
import uuid
from typing import Union, Callable, Any, Optional


class Cache():
    '''
    Cache class for simple cache system using redis db
    '''
    def __init__(self):
        '''
        initialization method
        creates instance of Redis and then flushes it
        '''
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''
        store method takes 2 args:
        - self
        - data (can be one of any listed data types)
        Return: string representing randomly generated key
        to store with data passed in
        '''
        data_key = str(uuid.uuid4())
        self._redis.set(data_key, data)
        return data_key

    def get(self, key: str, fn: Optional[Callable] = None
            ) -> Optional[Any]:
        '''
        '''
        data = self._redis.get(key)
        if data is None:
            return None
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> Optional[str]:
        '''
        '''
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        '''
        '''
        return self.get(key, fn=lambda d: int(d))
