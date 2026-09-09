class MyHashSet:
    DEFAULT_SIZE = 15
    class HashSetNode:
        def __init__(self, val=None, prev=None, next=None):
            self.val = val
            self.prev = prev
            self.next = next


    def __init__(self):
        self.elements = [
            self.HashSetNode() 
            for _ in range(self.DEFAULT_SIZE)
        ]
        for head in self.elements:
            tail = self.HashSetNode(None, head, head)
            head.next = tail
            head.prev = tail
        self.size = self.DEFAULT_SIZE
        

    def add(self, key: int) -> None:
        if self.contains(key):
            return
        
        # Get a hash of the key + its index
        key_hash = hash(key)
        index = key_hash % self.size

        # Append to the end
        tail = self.elements[index].prev
        new_node = self.HashSetNode(key, tail.prev, tail)
        # fix links
        tail.prev = new_node
        new_node.prev.next = new_node

        return

    def remove(self, key: int) -> None:
        if not self.contains(key):
            return
        
        # Get a hash of the key + its index
        key_hash = hash(key)
        index = key_hash % self.size

        # we know the val is here because we passed contains
        curr = self.elements[index].next
        while curr.val != key:
            curr = curr.next

        # fix links
        curr.prev.next = curr.next
        curr.next.prev = curr.prev
        del curr

        return
        

    def contains(self, key: int) -> bool:
        # Get a hash of the key + its index
        key_hash = hash(key)
        index = key_hash % self.size

        # stops when we hit tail
        curr = self.elements[index].next
        while curr.val != None:
            if curr.val == key:
                return True
            curr = curr.next
        
        return False
        
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)