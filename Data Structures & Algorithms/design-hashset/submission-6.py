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
        head = self._get_bucket_head(key)
        if self._bucket_find(head, key):
            return

        tail = head.prev
        # Append to the end
        new_node = self.HashSetNode(key, tail.prev, tail)
        # fix links
        tail.prev = new_node
        new_node.prev.next = new_node

        return
    
    def _get_bucket_head(self, key: int) -> HashSetNode:
        return self.elements[hash(key % self.size)]
    
    # returns node if found else returns tail
    def _bucket_find(self, bucket: HashSetNode, key: int) -> Optional[HashSetNode]:
        # stops when we hit tail
        curr = bucket.next 
        tail = bucket.prev
        while curr != tail:
            if curr.val == key:
                return curr
            curr = curr.next
        
        return None

    def remove(self, key: int) -> None:
        node_to_remove = self._find(key)
        if not node_to_remove:
            return

        # delete fix links
        node_to_remove.prev.next = node_to_remove.next
        node_to_remove.next.prev = node_to_remove.prev

        return
        
    def _find(self, key: int) -> HashSetNode:
        head = self._get_bucket_head(key)
        tail = head.prev
        node = self._bucket_find(head, key)

        return node if node != tail else None 

        

    def contains(self, key: int) -> bool:
        return self._find(key) != None
        
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)