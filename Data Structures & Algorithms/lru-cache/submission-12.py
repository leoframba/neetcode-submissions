class LRUCache:
    class Node:
        def __init__(self, val, key):
            self.val = val
            self.key = key
            self.prev = None
            self.next = None

    # need a struct with O(1) lookup for get
    # hashmap
    # need a struct with O(1) remove
    def __init__(self, capacity: int):
        self.m = {}
        self.head = self.Node(-1, -1)
        self.tail = self.Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cap = capacity

    # needs to O(1)
    def get(self, key: int) -> int:
        #get counts as a use
        if key in self.m:
            #handle use - append
            node = self.m[key]
            #remove node and append it to the end
            next = node.next
            prev = node.prev
            prev.next = next
            next.prev = prev

            # insert used node at tail
            prev = self.tail.prev
            
            # connect prev and new node
            prev.next = node
            node.prev = prev

            # connect tail to new node
            node.next = self.tail
            self.tail.prev = node

            return node.val
        else:
            return -1

        
    # needs to O(1)
    def put(self, key: int, value: int) -> None:

        node = None
        if key in self.m:
            # remove it from list to reappend
            #handle use - append
            node = self.m[key]
            node.val = value
            #remove node and append it to the end
            next = node.next
            prev = node.prev
            prev.next = next
            next.prev = prev
        else:
            # we just set it to the end
            node = self.Node(value, key)
            self.m[key] = node
        
        # insert used node at tail
        prev = self.tail.prev
        
        # connect prev and new node
        prev.next = node
        node.prev = prev

        # connect tail to new node
        node.next = self.tail
        self.tail.prev = node
            
        
        if len(self.m) > self.cap:
            node = self.head.next
            self.head.next = node.next
            node.next.prev = self.head
            
            self.m.pop(node.key)
        
        return None




        
