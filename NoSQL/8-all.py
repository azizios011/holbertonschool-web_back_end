#!/usr/bin/env python3
"""Lists all documents in a MongoDB collection."""


def list_all(mongo_collection):
    """ 'mongo_collection (pymongo.collection.Collection)':
    The MongoDB collection object."""
    documents = []
    cursor = mongo_collection.find()
    for document in cursor:
        documents.append(document)
    """ 'list': A list of all documents in the collection."""
    return documents
