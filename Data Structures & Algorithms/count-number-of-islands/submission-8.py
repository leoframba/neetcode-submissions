class Solution:
    class UnionFind:
        def __init__(self):
            self.parent = {}
            self.size = {}
            self.count = 0
        
        # Add a new value to the union find struct
        def add(self, val: int) -> None:
            self.parent[val] = val
            self.size[val] = 1
            self.count += 1

        # Finds the parent of a given union
        def find(self, val: int) -> int:
            # base
            if self.parent[val] == val:
                return val
            # compress
            self.parent[val] = self.find(self.parent[val])
            return self.parent[val]

        # True if unified false if they were already part of the same union
        def union(self, v1: int, v2: int) -> bool:
            # compress
            f1 = self.find(v1)
            f2 = self.find(v2)

            # Same parents = alrdy unified
            if f1 == f2:
                return False
            
            # Union based on rank
            # Smaller rnk joins bigger
            if self.size[f1] >= self.size[f2]:
                self.parent[f2] = f1
                self.size[f1] += self.size[f2]
            else:
                self.parent[f1] = f2
                self.size[f2] += self.size[f1]

            self.count -=1
            return True  
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        
        uf = Solution.UnionFind()
        island_count = 1

        r_minus1 = [0] * cols
        for row in grid:
            r_curr = [0] * cols

            for i, c in enumerate(row):
                # If we encounter a new land create it in uf
                if c == '1':
                    uf.add(island_count)
                    r_curr[i] = island_count
                    island_count += 1

                    #attempt to union it with up or left
                    # up - check if land then union
                    if r_minus1[i] != 0:
                        uf.union(r_curr[i], r_minus1[i])
                    # left
                    if i > 0 and r_curr[i - 1] != 0:
                        uf.union(r_curr[i], r_curr[i - 1])
            
            r_minus1 = r_curr
        
        return uf.count
                    





        return -1
        