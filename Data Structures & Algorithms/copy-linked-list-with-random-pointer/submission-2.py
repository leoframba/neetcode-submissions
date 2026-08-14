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

        # Key = OG node -> Value -> Deep Copy Node
        node_map = {None : None}

        # deep copy

        curr = head
        while curr:
           node_map[curr] = Node(curr.val)
           curr = curr.next
        
        # set links
        curr = head
        while curr:
            # get curr copy
            copy_node = node_map[curr]

            # set copy links
            copy_node.next = node_map[curr.next]    
            copy_node.random = node_map[curr.random]

            curr = curr.next
        
        return node_map[head]

        