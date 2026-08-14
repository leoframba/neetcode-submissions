class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max = 0
        min = 0
        for n in nums:
            if n > max:
                max = n
            if n < min:
                min = n
        
        offset = min * -1

        bucket = [False for _ in range(max + 1 + offset)]
        
        for n in nums:
            bucket[n + offset] = True
        
        res = 0
        curr = 0
        for flag in bucket:
            if flag:
                curr += 1
            else:
                curr = 0
            if curr > res:
                res = curr
        
        return res

        