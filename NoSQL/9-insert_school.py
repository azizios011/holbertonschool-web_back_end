#!/usr/bin/env python3
"""Inserts a new document into a 'MongoDB'
collection based on keyword arguments."""


def insert_school(mongo_collection, **kwargs):
    """ 'mongo_collection (pymongo.collection.Collection)':
    The 'MongoDB' collection object. '**kwargs': Keyword
    arguments representing the fields and values to insert."""
    result = mongo_collection.insert_one(kwargs)
    new_id = result.inserted_id
    """ 'str': The 'new _id' of the inserted document."""
    return str(new_id)
