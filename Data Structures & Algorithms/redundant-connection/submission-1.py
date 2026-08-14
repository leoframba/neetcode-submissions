class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        # we create the parent list for union find -- all values start as their own parents
        parent = [i for i in range(len(edges) + 1)]
        print(parent)
        count = len(edges)

        # find function returns the parent of a given node
        # if the node is not its own parent it will compress the path 
        def find(i):
            if parent[i] == i:
                return i

            parent[i] = find(parent[i])
            return parent[i]

        def union(i, j):
            nonlocal count
            root_i = find(i)
            root_j = find(j)

            if root_i != root_j:
                parent[root_i] = root_j
                count -= 1
                return True 
            return False
        
        for a, b in edges:
            if not union(a, b):
                return [a, b]
        
        return []
        