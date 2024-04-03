#!/usr/bin/env python3
""" This is a basic cache class"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ The FIFO Cache Class"""
    def __init__(self):
        """ This is the constructor"""
        super().__init__()

    def put(self, key, item):
        """ This is the put function to insert into the cache
        @key: The key of the item to be inserted
        @item: The item to be inserted
        Return: Returns nothing
        """
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key = list(self.cache_data.keys())[-1]
            self.cache_data.popItem()
            print("DISCARD: ".format(first_key))
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ This function gets the item from a cache using the key
        @key: The key to search with
        Return: Returns the value linked to the key
        """
        if key is not None:
            return (self.cache_data[key])
        if key is None or key is not in self.cache_data.keys():
            return None
