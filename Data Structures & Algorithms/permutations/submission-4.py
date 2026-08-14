class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        # permutations - unlike subsets permus are always of max len
        

        res = []

        # we dont need a start index as we are always going to look throught the entire list
        def gen(curr, visited):

            # wall - when we've reached a full curr
            if len(curr) == len(nums):
                res.append(curr.copy())
                return
            
            for num in nums:
                if num in visited:
                    continue

                curr.append(num)
                visited.add(num)
                gen(curr, visited)
                curr.pop()
                visited.remove(num)
            
            return
        
        gen([], set())
        return res

            

        