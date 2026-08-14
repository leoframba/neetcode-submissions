# brute banner
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        # edge
        if not nums:
            return 0
        n = len(nums)
        if n == 1:
            return n
        
        # Longest subseq found
        res = 0

        cache = {}

        # starting from given index look for vals > start to form a increasing subseq
        def dp(start) -> int:
            # wall - reached the end of nums
            if start == n:
                return 0
            
            if start in cache:
                return cache[start]
            
            tot = 1
            # n
            for i in range(start + 1, n):
                if nums[i] > nums[start]:
                    test = 1 + dp(i)
                    tot = max(test, tot)
            
            #print(f"s={start} -> {tot}")
            cache[start] = tot
            return tot

        # n
        for start in range(n):
            if res >= n - start:
                break
            res = max(dp(start), res)

        return res
        

        