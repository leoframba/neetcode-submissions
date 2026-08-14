class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        curr = n
        while curr > 0:
            res += curr & 1
            curr = curr >> 1
                
        return res
        