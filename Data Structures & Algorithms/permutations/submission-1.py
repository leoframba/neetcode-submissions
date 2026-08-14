class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []
        
        def bt():
            # Base Case: Our permutation is the same length as the input
            if len(curr) == len(nums):
                res.append(curr.copy())
                return
            
            # We look at EVERY number for every slot
            for num in nums:
                # If the number is already in our current permutation, skip it
                if num in curr:
                    continue
                    
                # Include
                curr.append(num)
                # Recurse
                bt()
                # Backtrack
                curr.pop()
                
        bt()
        return res