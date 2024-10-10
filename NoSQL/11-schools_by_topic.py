#!/usr/bin/env python3
'''
python function for mongodb NoSql script
finds and returns a list of key, value pairs
'''
from pymongo import MongoClient


def schools_by_topic(mongo_collection, topic):
    '''
    schools_by_topic function takes 2 args:
    - mongo_collection (collection to search)
    - topic (keys to search in documents of collection)
    Return:
    result (list of schools associated with topic)
    '''
    result = list(mongo_collection.find({"topics": topic}))
    return result
