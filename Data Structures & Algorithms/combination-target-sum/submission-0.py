class Solution:

    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(index, curr, sum):
            if sum == target:
                res.append(curr[:])
                return

            elif sum > target:
                return


            for i in range(index, len(nums)):
                curr.append(nums[i]) 
                backtrack(i, curr, sum + nums[i])
                curr.pop()
            return



        backtrack(0, [], 0)
        return res