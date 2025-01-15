#!/usr/bin/env python3

"""creates the LRUCache class"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """instantiates a caching system with LRU"""

    def __init__(self):
        """Instantiates LRUCache with cache_data from BaseCaching"""
        super().__init__()
        self.usage_queue = []

    def put(self, key, item):
        """add an item in the cache"""
        if not (key and item):
            return
        if key in self.cache_data:
            self.usage_queue.remove(key)
        elif len(self.cache_data) >= self.MAX_ITEMS:
            recently_used_key = self.usage_queue.pop(0)
            del self.cache_data[recently_used_key]
            print(f"DISCARD: {recently_used_key}")
        self.usage_queue.append(key)

        self.cache_data.update({key: item})

    def get(self, key):
        """get an item via its key"""
        if key in self.usage_queue:
            self.usage_queue.remove(key)
            self.usage_queue.append(key)
        return self.cache_data.get(key)
