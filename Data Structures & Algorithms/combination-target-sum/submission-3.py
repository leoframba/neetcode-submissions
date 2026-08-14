class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # 1. Sort the array to enable early stopping
        nums.sort()
        
        res = []
        curr = []

        def bt(start_index, current_total):
            # Base case: We hit the exact target
            if current_total == target:
                res.append(curr.copy())
                return
            
            # Iterate through all possible next choices
            for i in range(start_index, len(nums)):
                
                # 2. THE PRUNING STEP
                # If adding the current number exceeds the target, stop completely.
                # Because the array is sorted, every number after nums[i] will also exceed it.
                if current_total + nums[i] > target:
                    break 
                
                # Include the number
                curr.append(nums[i])
                
                # Recurse deeper. Notice we pass 'i' (not 'i + 1') because we are 
                # allowed to reuse the exact same number in the next level.
                bt(i, current_total + nums[i])
                
                # Backtrack
                curr.pop()
        
        # Kick off the recursion at index 0 with a total of 0
        bt(0, 0)
        
        return res