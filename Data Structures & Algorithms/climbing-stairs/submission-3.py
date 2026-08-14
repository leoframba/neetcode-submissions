class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n

        p1 = 1
        p2 = 2 
        curr = 0
        

        for i in range(3, n + 1):
            curr = p1 + p2
            p1 = p2
            p2 = curr
        
        return p2

        
        