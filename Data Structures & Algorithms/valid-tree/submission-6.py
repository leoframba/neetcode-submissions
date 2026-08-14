class Solution:
    class UnionFind:
        def __init__(self):
            self.parent = {}
            self.size = {}
        
        def add(self, v: int) -> None:
            if v in self.parent:
                return
            self.parent[v] = v
            self.size[v] = 1
        
        def find(self, v: int) -> int:
            if self.parent[v] != v:
                self.parent[v] = self.find(self.parent[v])
            return self.parent[v]
        
        def union(self, v1: int, v2: int) -> bool:
            p1 = self.find(v1)
            p2 = self.find(v2)

            if p1 == p2:
                return False
            
            if self.size[p1] > self.size[p2]:
                self.size[p1] += self.size[p2]
                self.parent[p2] = p1
            else:
                self.size[p2] += self.size[p1]
                self.parent[p1] = p2
            
            return True
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        # undirect = edges go both ways

        # valid tree:
        # all nodes connected
        # no cycles
        # every node has only 1 connection
        uf = Solution.UnionFind()
        # union find where final size must be = n
        for i in range(n):
            uf.add(i)
        for v1, v2 in edges:
            if not uf.union(v1, v2):
                # we found a cycle
                return False
        
        return max(uf.size.values(), default=0) == n
            
        