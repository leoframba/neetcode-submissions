class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        ss = []

        def bt(i):
            if i >= len(nums):
                res.append(ss.copy())
                return
            
            # we include i
            ss.append(nums[i])
            bt(i + 1) # go next

            #back track
            ss.pop()
            bt(i + 1)

            return
        
        bt(0)
        return res
        