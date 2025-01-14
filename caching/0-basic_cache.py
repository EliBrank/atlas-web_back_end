#!/usr/bin/env python3

"""creates the BasicCache class"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """instantiates a caching system"""

    def __init__(self):
        """Instantiates BasicCache with cache_data from BaseCaching"""
        super().__init__()

    def put(self, key, item):
        """add an item in the cache"""
        if not (key and item):
            return
        self.cache_data[key] = item

    def get(self, key):
        """get an item via its key"""
        if not key or key not in self.cache_data:
            return None
        else:
            return self.cache_data[key]
