#!/usr/bin/env python3

"""
Module for schools_by_topic function
"""


def schools_by_topic(mongo_collection, topic):
    """Gets list of schools which include input topic
    """
    return list(mongo_collection.find({ "topics": topic })) or []
