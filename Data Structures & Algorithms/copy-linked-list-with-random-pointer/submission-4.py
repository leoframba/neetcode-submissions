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
        node_map = {None : None}

        curr = head

        def dfs(node) -> Optional[Node]:
            # wall - we have already proccesed this node
            if node in node_map:
                return node_map[node]

            copy_node = Node(node.val)
            node_map[node] = copy_node
            
            
            copy_node.next = dfs(node.next)
            copy_node.random = dfs(node.random)
            return copy_node
        
        
        dfs(head)
        return node_map[head]

        