class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:


        res = []
        curr = []

        def bt(i, total):
            # wall conditions
            if total == target:
                res.append(curr.copy())
                return
            if i >= len(nums) or total > target:
                return
            
            
            # include a number
            curr.append(nums[i])
            bt(i, total + nums[i])

            #back track
            curr.pop()
            bt(i + 1, total)
        
        bt(0, 0)
        return res

        
        