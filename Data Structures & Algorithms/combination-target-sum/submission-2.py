class Solution:
    class State:
        def __init__(self, i, combo, total):
            self.i = i
            self.combo = combo
            self.total = total
        
        def __iter__(self):
            yield self.i
            yield self.combo
            yield self.total

    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        
        # iterative
        stack = [self.State(0, [], 0)]
        res = []

        while stack:
            i, combo, total = stack.pop()
            #wall conditions
            # valid combo
            if total == target:
                res.append(combo)
                continue
            # overshot target or out of nums
            if i >= len(nums) or total > target:
                continue
            
            # include current index
            stack.append(self.State(i, combo + [nums[i]], total + nums[i]))

            # skip
            stack.append(self.State(i + 1, combo, total))
        
        return res
            



        
        