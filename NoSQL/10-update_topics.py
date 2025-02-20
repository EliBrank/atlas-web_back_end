#!/usr/bin/env python3

"""
Module for update_topics function
"""


def update_topics(mongo_collection, name, topics):
    """Changes topics in school document based on name
    """
    query_filter = { "name": name }
    update_operation = { "$set":
        { "topics": topics }
    }

    mongo_collection.update_many(query_filter, update_operation)
