#!/usr/bin/env python3
def insert_school(mongo_collection, **kwargs):
    result = mongo_collection.insert_one(kwargs)
    new_id = result.inserted_id
    return str(new_id)
