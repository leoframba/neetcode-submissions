class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        
        stack = []
        # everytime we encouanter a new day -- we look at temp
        
        res = [0] * n
        for i in range(n):
            curr = temperatures[i]            
            while stack and curr > temperatures[stack[-1]]:
                pidx = stack.pop()
                res[pidx] = i - pidx
            stack.append(i)
        
        return res

            


                    
            


        