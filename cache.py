# Implements specialized container data types
import collections

# Set  cache size
CACHE_SIZE = 16


# Creates a cache as a dequeue data type
class Cache:
    # Initialization function - stored as dequeue of tuples and initialized as empty
    def __init__(self):
        self.cache = collections.deque(maxlen=CACHE_SIZE)
        self.flush_cache()

    # Replace all bits in the cache
    def flush_cache(self):
        for bit in range(CACHE_SIZE):
            self.cache.append(("", ""))

    # Write to cache by appending address/value tuple
    def write_cache(self, address, value):
        self.cache.append((address, value))

    # Search cache by address. Returns value if found or None if not
    def search_cache(self):
        for address in range(CACHE_SIZE):
            if self.cache[i][0] == address:
                return self.cache[i][1]
        return None
