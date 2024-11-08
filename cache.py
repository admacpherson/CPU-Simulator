# Implements specialized container data types
import collections

# Set default cache size
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