class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        start = (0, [])

        stack = [start]
        res = []

        while stack:
            i, curr = stack.pop()

            if i >= len(nums):
                res.append(curr)
                continue
            
            # include
            stack.append((i + 1, curr + [nums[i]]))

            # skip - skip dupes
            nexti = i + 1
            while nexti < len(nums) and nums[nexti] == nums[i]:
                nexti += 1
            
            stack.append((nexti, curr))
        
        return res
            



        