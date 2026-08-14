class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        curr = []

        def gen(i):
            if i >= len(nums):
                res.append(curr.copy())
                return
            
            #include
            curr.append(nums[i])
            gen(i + 1)
            
            #backtrack
            curr.pop()
            
            nexti = i + 1
            while nexti < len(nums) and nums[nexti] == nums[i]:
                nexti += 1
            #skip
            gen(nexti)
        
        gen(0)
        return res
        