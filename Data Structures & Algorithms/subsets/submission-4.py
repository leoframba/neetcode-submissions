class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = []
        curr = []

        def bt(idx):
            if idx >= len(nums):
                res.append(curr.copy())
                return
            
            # include/skip values
            #include -> move on
            curr.append(nums[idx])
            bt(idx + 1)

            #back track
            curr.pop()
            #move
            bt(idx + 1)

            return

        
        bt(0)
        return res

        