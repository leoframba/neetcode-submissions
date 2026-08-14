"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if not head: return None

        cur = head
        prev = head
        while cur:
            prev = cur
            cur = cur.next

            prev.next = Node(prev.val)
            prev.next.next = cur

        cur = head
        dummy = Node(0)
        dummy.next = head.next
        while cur:
           # print(f"{cur.val}, {cur.random}")
            copy = cur.next
        
            if cur.random:
                copy.random = cur.random.next
            else:
                copy.random = None
        
            cur = copy.next
        
        cur = head
        while cur:
            copy = cur.next
            cur.next = copy.next
        
            if copy.next:
                copy.next = copy.next.next
            else:
                copy.next = None
            
            cur = cur.next
            

        
        # cur = head
        # while cur:
        #     print(f"{cur.val}, {cur.random}")
        #     cur = cur.next
            
        
        return dummy.next

        