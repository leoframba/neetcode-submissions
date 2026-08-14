class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        visited = set()

        def backtrack(curr):
            # when our current list is full weve found a permutation
            if len(curr) == len(nums):
                res.append(list(curr))
                return
            
            for num in nums:
                if num in visited:
                    continue
                
                #1 choose
                curr.append(num)
                visited.add(num)

                #2 explore
                backtrack(curr)

                #3 backtrack
                curr.pop()
                visited.remove(num)
        
        backtrack([])
        return res
        