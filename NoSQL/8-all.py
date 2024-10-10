#!/usr/bin/env python3
'''
module to list all documents in a collection
'''

def list_all(mongo_collection):
    '''
    list_all function takes 1 arg:
    - mongo_collection (collection to check)
    Return:
    Empty list if collection is none
    otherwise, list of documents in collection
    '''
    if mongo_collection is None:
        return []
    return list(mongo_collection.find())
