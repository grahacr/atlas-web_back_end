#!/usr/bin/python3
'''
this module imports parent class BaseCaching
and adds a FIFO cache system, inserting data into a cache
and deleting first item in if the max number of items is met
'''
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    '''
    FIFOCache inherits from BaseCaching,
    and implements FIFO eviction strategy to maintain cache dict
    '''
    def __init__(self):
        '''
        constructor method calls parent constructor
        creates instance
        '''
        super().__init__()

    def put(self, key, item):
        '''
        put function takes 3 arguments:
        - self
        - key
        - item
        assigns item to given key, if key exists and is not None.
        if MAX_ITEMS has been met for the cache dictionary,
        FIFO method deletes first item in dictionary to make room
        for new item, and prints Discard message if necessary
        '''
        cache_data = self.cache_data
        if key is not None and item is not None:
            if len(cache_data) == self.MAX_ITEMS:
                first_item = next(iter(cache_data))
                del cache_data[first_item]
                print("DISCARD: {}".format(first_item))
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
