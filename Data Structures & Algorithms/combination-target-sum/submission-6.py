class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()

        res = []
        
        def bt(start, curr, total):
            if total == target:
                res.append(curr.copy())
                return
            if total > target or start >= len(nums):
                return
            
            for i in range(start, len(nums)):
                if nums[i] + total > target:
                    break
                
                curr.append(nums[i])
                bt(i, curr, total + nums[i])
                curr.pop()
            
            return
        
        bt(0, [], 0)
        return res

        