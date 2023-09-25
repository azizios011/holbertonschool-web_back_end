#!/usr/bin/env python3
"""Lists all documents in a MongoDB collection."""


from typing import List


def list_all(mongo_collection):
    """ 'mongo_collection (pymongo.collection.Collection)':
    The MongoDB collection object."""
    documents = List(mongo_collection.find({}))
    """ 'list': A list of all documents in the collection."""
    return documents
