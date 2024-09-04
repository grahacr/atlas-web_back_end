#!/usr/bin/python3
'''
Module adds to cache system from parent class BaseCaching,
utilizes OrderedDict method from collections module,
and evicts cache items based on Least Recently Used (LRU)
'''
from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    '''
    LRUCache class implements a class to add to cache system
    which evicts excess cache items by LRU Method
    '''
    def __init__(self):
        '''
        constructor method calls parent constructor
        creates instance.
        Creates ordered dictionary out of parent class cache_data
        '''
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        '''
        put method takes 3 arguments:
        - self
        - key
        - item
        Adds accessed cache items to end of dictionary.
        if Max Items of cache items is reached - the first key, value pair
        inserted into ordered dictionary is popped off
        '''
        if key is not None and item is not None:
            self.cache_data.move_to_end(key)
        elif len(self.cache_data) >= self.MAX_ITEMS:
            lru_key, _ = self.cache_data.popitem(last=False)
            print("DISCARD: {}".format(lru_key))
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
