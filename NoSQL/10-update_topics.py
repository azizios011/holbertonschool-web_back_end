#!/usr/bin/env python3
"""a Python function that changes all topics of
a school document based on the name"""


def update_topics(mongo_collection, name, topics):
    """Update the topics for the school with the specified name"""
    result = mongo_collection.update_one({"name": name},
                                         {"$set": {"topics": topics}})

    """Check if the update was successful"""
    if result.matched_count == 1:
        print(f"Topics updated for school {name}")
    else:
        print(f"School {name} not found")
