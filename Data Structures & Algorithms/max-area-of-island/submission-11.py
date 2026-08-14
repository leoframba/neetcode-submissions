class Solution:
    class UnionFind:
        def __init__(self):
            self.parent = {}
            self.size = {}
            self.count = 0
        
        def add(self, val: int) -> None:
            self.parent[val] = val
            self.size[val] = 1
            self.count += 1
        
        # Find the parent of a given val
        def find(self, val: int) -> int:
            curr = val
            while self.parent[curr] != curr:
                self.parent[curr] = self.parent[self.parent[curr]]
                curr = self.parent[curr]
            return self.parent[curr]
        
        # Preform the union of two vals - returns true if values were unified
        def union(self, v1: int, v2: int) -> bool:
            # Get the parents
            p1 = self.find(v1)
            p2 = self.find(v2)

            # check for same parent
            if p1 == p2:
                return False
            
            # union by size
            if self.size[p1] >= self.size[p2]:
                self.size[p1] += self.size[p2]
                self.parent[p2] = p1
            else: #p2 > p1
                self.size[p2] += self.size[p1]
                self.parent[p1] = p2

            self.count -= 1
            return True    


    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # edge case - invalid input empty
        if not grid:
            return 0 # No grid no island
        
        uf = Solution.UnionFind()

        rows, cols = len(grid), len(grid[0])
        island_id = 1
        r_minus1 = [0] * cols
        for r in grid:
            r_curr = [0] * cols
            for i in range(cols):
                # if we find a land union
                if r[i] == 1:
                    uf.add(island_id)
                    r_curr[i] = island_id
                    island_id += 1

                    # check up
                    if r_minus1[i] > 0:
                        uf.union(r_curr[i], r_minus1[i])
                    
                    # check left
                    if i > 0 and r_curr[i - 1] > 0:
                        uf.union(r_curr[i], r_curr[i - 1])
            r_minus1 = r_curr 
        
        return max(uf.size.values(), default=0) 
            

        