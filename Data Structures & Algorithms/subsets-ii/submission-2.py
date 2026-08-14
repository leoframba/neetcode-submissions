class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
       # sorth the list so we can group dupes
        nums.sort()

        # we use the same alg as regualr subsets porblem but we need ot handle dupes

        res = []
        # track index + current set
        def rec(i, curr):
            # wall 
            # end of this subset 
            if i >= len(nums):
                res.append(curr.copy())
                return
            

            # take current val
            curr.append(nums[i])
            rec(i + 1, curr)

            #back track
            curr.pop()
            #skip dupes
            next = i + 1
            while next < len(nums) and nums[next] == nums[i]:
                next += 1
            rec(next, curr)

            return
        
        rec(0, [])
        return res

        