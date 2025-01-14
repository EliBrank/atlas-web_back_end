#!/usr/bin/env python3

"""creates the LIFOCache class"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """instantiates a caching system with LIFO"""

    def __init__(self):
        """Instantiates FIFOCache with cache_data from BaseCaching"""
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """add an item in the cache"""
        if not (key and item):
            return
        if key in self.cache_data:
            self.queue.remove(key)
        elif len(self.cache_data) >= self.MAX_ITEMS:
            most_recent_key = self.queue.pop()
            del self.cache_data[most_recent_key]
            print(f"DISCARD: {most_recent_key}")
        self.queue.append(key)

        self.cache_data.update({key: item})

    def get(self, key):
        """get an item via its key"""
        return self.cache_data.get(key)
