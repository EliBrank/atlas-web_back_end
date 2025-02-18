#!/usr/bin/env python3

"""
Module for list_all function
"""


def list_all(mongo_collection):
    """Retrieves all documents in collection
    """
    return mongo_collection.find()
