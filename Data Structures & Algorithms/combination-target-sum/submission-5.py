class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:


        # so we can use repeats
        res = []
        def gen(i, curr, total):
            # wall
            # if total 
            if total == target:
                res.append(curr.copy())
                return
            if i >= len(nums) or total > target:
                return
            
            # take current num - dont incrament as we can take multiple
            curr.append(nums[i])
            gen(i, curr, total + nums[i])
            # natural backtrack
            # skip
            curr.pop()
            gen(i + 1, curr, total)
        
            return
        
        gen(0, [], 0)
        return res

        