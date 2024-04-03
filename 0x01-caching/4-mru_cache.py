#!/usr/bin/env python3
""" This is a basic cache class"""
from datetime import datetime
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """ The FIFO Cache Class"""
    def __init__(self):
        """ This is the constructor"""
        super().__init__()
        self.log = {}

    def put(self, key, item):
        """ This is the put function to insert into the cache
        @key: The key of the item to be inserted
        @item: The item to be inserted
        Return: Returns nothing
        """
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            mru_key = max(self.log, key=self.log.get)
            self.cache_data.pop(mru_key)
            print("DISCARD: ".format(mru_key))
        if key is not None and item is not None:
            self.cache_data[key] = item
            self.log[key] = datetime.now()

    def get(self, key):
        """ This function gets the item from a cache using the key
        @key: The key to search with
        Return: Returns the value linked to the key
        """
        if key is not None:
            self.log[key] = datetime.now()
            return (self.cache_data[key])
        if key not in self.cache_data:
            return None
