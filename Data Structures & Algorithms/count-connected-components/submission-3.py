class Solution:
    class UnionFind:
        def __init__(self, n):
            self.parent = [i for i in range(n)]
            self.size = [1 for i in range(n)]
            self.count = n
        
        def find(self, v):
            if v < 0 or v >= len(self.parent):
                return
            curr = v
            while self.parent[curr] != curr:
                self.parent[curr] = self.parent[self.parent[curr]]
                curr = self.parent[curr]
            return curr
        
        def union(self, v1: int, v2: int) -> bool:
            # check both vals are inbounds..

            p1 = self.find(v1)
            p2 = self.find(v2)

            if p1 == p2:
                return False

            #else
            if self.size[p1] >= self.size[p2]:
                self.size[p1] += self.size[p2]
                self.parent[p2] = p1
            else:
                self.size[p2] += self.size[p1]
                self.parent[p1] = p2
            
            self.count -= 1
            return True

    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        # union find again

        # edge case 0/1 nodes will always be none or the only node
        if n <= 1:
            return n
        if not edges:
            return n

        uf = Solution.UnionFind(n)

        for v1, v2 in edges:
            uf.union(v1, v2)
        
        return uf.count
        

        

        