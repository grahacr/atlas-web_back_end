#!/usr/bin/python3
'''
module imports BaseCaching and uses it as parent class for new BasicCache class
which will implement a cache system with put and get methods.
'''
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    '''BasicCache inherits from BaseCaching,
    a straightforward parent class.
    This child class implements the put and get functions
    for cache system
    '''
    def __init__(self):
        '''
        constructor method calls parent constructor
        '''
        super().__init__()

    def put(self, key, item):
        '''
        put method takes 3 arguments:
        - self
        - key
        - item
        if key and item are not empty, store item at given key
        in the designated cache system
        '''
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        '''
        get method takes 2 arguments:
        - self
        - key
        Returns: the value linked to the given key,
        as long as key exists and is not None
        '''
        return self.cache_data.get(key, None)
