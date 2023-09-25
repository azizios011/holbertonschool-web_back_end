#!/usr/bin/env python3
"""Inserts a new document into a 'MongoDB'
collection based on keyword arguments."""


def insert_school(mongo_collection, **kwargs):
    """ 'mongo_collection (pymongo.collection.Collection)':
    The 'MongoDB' collection object. '**kwargs': Keyword
    arguments representing the fields and values to insert."""
    documento = {}
    for clave, valor in kwargs.items():
        documento[clave] = valor
    insertar = mongo_collection.insert_one(documento)
    """ 'str': The 'new _id' of the inserted document."""
    if insertar.acknowledged:
        return insertar.inserted_id
    return {}
