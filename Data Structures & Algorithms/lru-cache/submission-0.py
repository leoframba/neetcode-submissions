class LRUCache:

    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity
        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        # Move the accessed item to the end (Most Recently Used)
        self.cache.move_to_end(key)
        return self.cache[key]
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Update value and move to end
            self.cache.move_to_end(key)
        
        self.cache[key] = value
        
        # If we exceeded capacity, remove the first item (Least Recently Used)
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)
        

        
