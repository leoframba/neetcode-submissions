class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # set up parent list - at the start everybody is their own parent
        parent = [i for i in range(n)]
        count = n

        def find(i):
            if parent[i] == i:
                return i
            
            parent[i] = find(parent[i]) # path comp
            return parent[i]
        
        def union(i, j):
            root_i = find(i)
            root_j = find(j)

            if root_i != root_j:
                parent[root_i] = root_j
                return True

            return False
        
        for a, b in edges:
            if union(a, b):
                count -= 1
        
        return count