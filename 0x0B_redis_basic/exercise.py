#!/usr/bin/env python3
'''
module using redis to create simple cache and
use for basic exercises
'''
import redis
import uuid
from typing import Union, Callable, Any, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    '''
    '''
    @wraps(method)
    def wrapper(self, *args, **kwds):
        '''
        '''
        key = method.__qualname__
        self._redis.incr(key)
        result = method(self, *args, **kwds)
        return result
    
    return wrapper

def call_history(method: Callable) -> Callable:
    '''
    '''
    @wraps(method)
    def wrapper(self, *args):
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"
        self._redis.rpush(input_key, str(args))

        output = method(self, *args)
        self._redis.rpush(output_key, str(output))

        return output

    return wrapper

def replay(method):
    '''
    '''
    input_key = f"{method.__qualname__}:inputs"
    output_key = f"{method.__qualname__}:outputs"

    inputs = method.__self__._redis.lrange(input_key, 0, -1)
    outputs = method.__self__._redis.lrange(output_key, 0, -1)
    call_count = len(inputs)

    print(f"{method.__qualname__} was called {call_count} times:")
    for in_value, out_value in zip(inputs, outputs):
        in_value = in_value.decode('utf-8')
        out_value = out_value.decode('utf-8')
        print(f"{method.__qualname__}(*{in_value},)) -> {out_value}")


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

    @count_calls
    @call_history
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
