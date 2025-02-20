#!/usr/bin/env python3

"""
Module for schools_by_topic function
"""

from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    print(f"{collection.count_documents({})} logs")
    print("Methods:")

    for method in methods:
        num_docs_with_method = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {num_docs_with_method}")

    get_status_query = collection.count_documents({
        "$and": [
            {"method": "GET"},
            {"path": "/status"}
        ]
    })

    print(f"{get_status_query} status check")
