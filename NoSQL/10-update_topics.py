#!/usr/bin/env python3
"""a Python function that changes all topics of
a school document based on the name"""


def update_topics(mongo_collection, name, topics):
    """Update the topics for the school with the specified name"""
    filtro = {"name": name}
    remplazo = {
            "$set": {"topics": topics}}
    actualizacion = mongo_collection.update_many(filtro, remplazo)
