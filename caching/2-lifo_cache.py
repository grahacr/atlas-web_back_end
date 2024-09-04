#!/usr/bin/python3
'''
this module imports parent class BaseCaching
and adds a LIFO cache system, inserting data into a cache
and deleting last added item if the max number of items is met
'''
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    '''
    LIFOCache inherits from BaseCaching,
    and implements LIFO eviction strategy to maintain cache dict
    '''
    def __init__(self):
        '''
        constructor method calls parent constructor
        creates instance
        '''
        super().__init__()
        self.order = []

    def put(self, key, item):
        '''
        put function takes 3 arguments:
        - self
        - key
        - item
        assigns item to given key, if key exists and is not None.
        if MAX_ITEMS has been met for the cache dictionary,
        LIFO method pops last item off of ordered list of data
        and deletes it with a discard message to make room for new item
        '''
        cache_data = self.cache_data
        if key is not None and item is not None:
            if len(cache_data) == self.MAX_ITEMS:
                last_key = self.order.pop()
                del cache_data[last_key]
                print("DISCARD: {}".format(last_key))
            cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        '''
        get method takes 2 arguments:
        - self
        - key
        Returns: the value linked to the given key,
        as long as key exists and is not None
        '''
        return self.cache_data.get(key, None)
