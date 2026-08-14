from collections import deque
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.q = deque()
        self.cap = capacity
        

    def get(self, key: int) -> int:
        if key in self.cache:
            if key in self.q:
                self.q.remove(key)
            #used key so add it to q
            self.q.append(key)
            return self.cache[key]
        else:
            return -1


    def put(self, key: int, value: int) -> None:
        if key in self.q:
            self.q.remove(key)

        self.q.append(key)
        self.cache[key] = value
        
        print(self.q)
        while len(self.cache) > self.cap and self.q:
            least = self.q.popleft()
            self.cache.pop(least, None)
        
        return None

        
