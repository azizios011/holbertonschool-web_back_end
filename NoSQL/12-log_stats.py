#!/usr/bin/env python3
"""  Python script that provides some statistics """
from pymongo import MongoClient


def estadistica(mongo_collection, tmp=None):
    """ statistics on Nginx logs stored in MongoDB """
    method = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    items = {}
    if tmp:
        value = mongo_collection.count_documents(
            {"method": {"$regex": tmp}})
        print(f"\tmethod {tmp}: {value}")
        return

    result = mongo_collection.count_documents(items)
    print(f"{result} logs")
    print("Methods:")
    for metodo in method:
        estadistica(client, metodo)
    status_check = mongo_collection.count_documents({"path": "/status"})
    print(f"{status_check} status check")


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017').logs.nginx
    estadistica(client)
