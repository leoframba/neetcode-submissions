class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        # for num in nums:
        #     res += [curr + [num] for curr in res]
        

        for num in nums: # iterate through all numbers
            new_subsets = []
            for curr in res: # iterate through all subsets
                new = curr + [num]
                new_subsets.append(new)
            res.extend(new_subsets)
            
        return res
        