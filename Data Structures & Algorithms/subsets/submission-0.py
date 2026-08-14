class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # im using a set to prevent dupes
        # start with the empty set
        result = []
        
        def backtrack(start, curr):
            result.append(list(curr))

            for i in range(start, len(nums)):
                curr.append(nums[i])

                backtrack(i + 1, curr)
                curr.pop()
        
        backtrack(0, [])
        return result

        




        