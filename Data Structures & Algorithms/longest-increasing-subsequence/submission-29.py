class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        # Edge case - an empty list has a subseq of 0
        if not nums:
            return 0

        # Define a new list to track the smallest tails found  
        tails_idx = [0]

        def bisect_left(left: int, right: int, val: int) -> int:
            
            while left < right:
                mid = left + (right - left) // 2
                if val > nums[tails_idx[mid]]:
                    left = left + 1
                else:
                    right = mid
            
            return left
                
                
        parent = [-1 for n in nums]
        for i in range(1, len(nums)):
            # iterate over nums at each point we have two senarios
            #Seanrio 1 the new tail is greater than anything we've seen
            # We append it 
            if nums[i] > nums[tails_idx[-1]]:
                parent[i] = tails_idx[-1]
                tails_idx.append(i) 
            else:
            # We need to find where it fits in our tails list
                insert = bisect_left(0, len(tails_idx) - 1, nums[i])
                tails_idx[insert] = i

                # we only mark a parent if its not the head
                if insert > 0:
                    parent[i] = tails_idx[insert - 1]
        
        #build the list
        curr = tails_idx[-1]

        res = []
        while curr != -1:
            res.append(nums[curr])
            curr = parent[curr]
        
        print(res[::-1])
        return len(res)