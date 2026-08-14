"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def __init__(self):
        self.visited = {}
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        # # empty check
        # if not node:
        #     return node
        
        # visited: Dict[Node: Node] = {}

        # visited[node] = Node(node.val, [])
        # q = deque([node]) # use a q to track the nodes we have linked

        # while q:
        #     curr = q.popleft()

        #     # if we havent seen this node make a copy
        #     if curr not in visited:
        #         visited[curr] = Node(curr.val, [])
            
        #     for n in curr.neighbors:
        #         if n not in visited:
        #             visited[n] = Node(n.val, [])
        #             q.append(n)
        #         visited[curr].neighbors.append(visited[n])
        
        # return visited[node]
        # empty check
        # if not node:
        #     return node
        
        # visited: Dict[Node: Node] = {}

        # visited[node] = Node(node.val, [])
        # stack = [node] # use a q to track the nodes we have linked

        # while stack:
        #     curr = stack.pop()

        #     # if we havent seen this node make a copy
        #     if curr not in visited:
        #         visited[curr] = Node(curr.val, [])
            
        #     for n in curr.neighbors:
        #         # here we are using visted as a first time seeing struct. The first time we see ie not in our visted we throw that node in the q to make sure we proccess it
        #         if n not in visited:
        #             visited[n] = Node(n.val, [])
        #             stack.append(n)
        #         visited[curr].neighbors.append(visited[n])
        
        # return visited[node]
        # empty check
        if not node:
            return node
        
        # skip already visited nodes
        if node in self.visited:
            return self.visited[node]
        
        # create a copy of current node
        copy_node = Node(node.val, [])

        # link copy to og
        self.visited[node] = copy_node

        if node.neighbors:
            #copy_node.neighbors = [self.cloneGraph(n) for n in node.neighbors]
            for n in node.neighbors:
                copy_node.neighbors.append(self.cloneGraph(n))
        
        return copy_node


        