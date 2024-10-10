#!/usr/bin/env python3
'''
python module to update specific attributes
within document in given collection
'''
from pymongo import MongoClient


def update_topics(mongo_collection, name, topics):
    '''
    update_topics function takes 3 args:
    - mongo_collection (collection to update)
    - name (name of attribute key to update)
    - topics (values to be updated)
    '''
    mongo_collection.update_many(
        { 'name': name },
        { '$set': { 'topics': topics} }
    )
