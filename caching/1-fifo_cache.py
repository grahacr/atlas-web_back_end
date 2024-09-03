#!/usr/bin/python3
'''

'''
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    '''
    '''
    def __init__(self):
        '''
        constructor method calls parent constructor
        creates instance
        '''
        super().__init__()

    def put(self, key, item):
        cache_data = self.cache_data
        if key is not None and item is not None:
            if len(cache_data) >= BaseCaching.MAX_ITEMS:
                 first_item = next(iter(cache_data))
                 del cache_data[first_item]
                 print("Discard: {key}/n")
            cache_data[key] = item

    def get(self, key):
        '''
        get method takes 2 arguments:
        - self
        - key
        Returns: the value linked to the given key,
        as long as key exists and is not None
        '''
        return self.cache_data.get(key, None)
