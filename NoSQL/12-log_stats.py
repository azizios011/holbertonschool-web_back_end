#!/usr/bin/env python3
"""a Python script that provides some stats about
Nginx logs stored in MongoDB"""


from pymongo import MongoClient


def log_stats():
    """Connect to the MongoDB server"""
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    collection = db.nginx

    """Count the total number of documents in the collection"""
    total_logs = collection.count_documents({})

    """Count the number of documents with each HTTP method"""
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_counts = {method: collection.count_documents
                     ({"method": method})for method in methods}

    """Count the number of documents with method=GET and path=/status"""
    status_check_count = collection.count_documents
    ({"method": "GET", "path": "/status"})

    """Print the results"""
    print(f"{total_logs} logs")
    print("Methods:")
    for method, count in method_counts.items():
        print(f"\tmethod {method}:", count)
    print(f"{status_check_count} status check")


if __name__ == "__main__":
    log_stats()
