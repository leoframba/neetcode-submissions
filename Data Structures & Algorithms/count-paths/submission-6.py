# bottoms up

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 0 and n == 0:
            return 0
        
        dp_cur = [1 for _ in range(n)]
        for r in range(1, m):
            for c in range(1, n):
                # from each point on the grid u can go down or right
                # the valid amount of paths at each grid are therefore 
                dp_cur[c] += + dp_cur[c - 1]
            
        
        return dp_cur[n - 1]

        