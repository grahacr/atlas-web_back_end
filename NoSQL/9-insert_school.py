#!/usr/bin/env python3
'''
module creates python script
it will insert new document into MongoDB collection
'''
from pymongo import MongoClient


def insert_school(mongo_collection, **kwargs):
    '''
    insert_school function takes 2 args:
    - mongo_collection (collection to insert new document)
    - **kwargs (key:value pairs to insert)
    Return:
    - id of inserted document (result)
    '''
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
