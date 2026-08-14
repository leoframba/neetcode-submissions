class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        # Edge case - an empty list has a subseq of 0
        if not nums:
            return 0

        # Define a new list to track the smallest tails found  
        tails = [nums[0]]

        def bisect_left(left: int, right: int, val: int) -> int:
            if left == right:
                return left
            
            mid = left + (right - left) // 2

            if val > tails[mid]:
                return bisect_left(mid + 1, right, val)
            else:
                return bisect_left(left, mid, val)

        for i in range(1, len(nums)):
            # iterate over nums at each point we have two senarios
            #Seanrio 1 the new tail is greater than anything we've seen
            # We append it 
            if nums[i] > tails[-1]:
                tails.append(nums[i]) 
            else:
            # We need to find where it fits in our tails list
                insert = bisect_left(0, len(tails) - 1, nums[i])
                tails[insert] = nums[i]
        
        return len(tails)