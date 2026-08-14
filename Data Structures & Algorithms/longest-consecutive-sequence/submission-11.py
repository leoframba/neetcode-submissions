class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        maxi = max(nums) # O(n)
        mini = min(nums) 
        offset = 0

        # if we have negatives we need to do an offset
        if mini < 0:
            offset = -mini # a min of -5 gives us an offset of 5. nums[0 + offset(5)] = -5 bucket
        bucket = [0] * (maxi + offset + 1) # +1 to handle 0

        for num in nums:
            bucket[num + offset] = True # dont care about dupes
        
        res = 0
        curr = 0
        # look through bucks -- Looking for seq of True as True == we have this val in nums
        for b in bucket:
            if b: # if we have the val
                curr += 1 #increase the current seq
                res = max(curr, res) # check if new max
            else: # dud we reset
                curr = 0
        return res