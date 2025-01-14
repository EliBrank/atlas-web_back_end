#!/usr/bin/env python3

"""creates the FIFOCache class"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """instantiates a caching system with FIFO"""

    def __init__(self):
        """Instantiates BasicCache with cache_data from BaseCaching"""
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """add an item in the cache"""
        if not (key and item):
            return
        if key not in self.cache_data:
            if len(self.cache_data) >= self.MAX_ITEMS:
                oldest_key = self.queue.pop(0)
                del self.cache_data[oldest_key]
                print(f"DISCARD: {oldest_key}")
            self.queue.append(key)
        self.cache_data.update({key: item})

    def get(self, key):
        """get an item via its key"""
        return self.cache_data.get(key)
