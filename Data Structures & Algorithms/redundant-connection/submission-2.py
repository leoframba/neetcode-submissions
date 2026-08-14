class Solution:
    class UnionFind:
        def __init__(self, n: int):
            self.parent = [i for i in range(n + 1)]
            self.size = [1 for _ in range(n + 1)]
            self.count = n
        
        def find(self, v) -> int:
            curr = v
            while self.parent[curr] != curr:
                self.parent[curr] = self.parent[self.parent[curr]]
                curr = self.parent[curr]
            return curr

        def union(self, v1, v2) -> bool:
            p1 = self.find(v1)
            p2 = self.find(v2)

            if p1 == p2:
                return False
            
            if self.size[p1] >= self.size[p2]:
                self.size[p1] += self.size[p2]
                self.parent[p2] = p1
            else:
                self.size[p2] += self.size[p1]
                self.parent[p1] = p2
            
            self.count -= 1
            return True

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        # we can brute force. Attempt to build a valid graph for all edges except the curr to see if its still valid
        # The other option is to see what edge makes the graph a cycle

        n = len(edges) # n - 1 + 1(redundant)
        uf = Solution.UnionFind(n)

        for v1, v2 in edges:
            if not uf.union(v1, v2):
                return [v1, v2]
        
        return []

        




        