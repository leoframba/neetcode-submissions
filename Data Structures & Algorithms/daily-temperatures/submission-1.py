class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        
        # edge cases
        # invalid inputs
        if n == 0:
            return []
        if n == 1:
            return [0]

        stack = []
        # everytime we encouanter a new day -- we look at temp
        
        res = [0] * n
        for i in range(n):
            curr = temperatures[i]
            # empty stack = nothing to compare
            if not stack:
                stack.append((curr, i))
            else:
                # we start the counter at 1 bc we start 1 ahead
                while stack and curr > stack[-1][0]:
                    p = stack.pop()
                    res[p[1]] = i - p[1]
                stack.append((curr, i))
        
        return res

            


                    
            


        