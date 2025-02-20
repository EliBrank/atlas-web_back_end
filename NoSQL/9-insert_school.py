#!/usr/bin/env python3

"""
Module for insert_school function
"""


def insert_school(mongo_collection, **kwargs):
    """Inserts school document with info from kwargs
    """
    school_document = mongo_collection.insert_one(kwargs)
    return school_document.inserted_id
