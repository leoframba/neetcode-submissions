class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        m = 0

        llen = len(temperatures)
        

        for i in range(llen - 1, -1, -1):
            
            cur = temperatures[i]
            gap = 0
            while stack and cur >= stack[-1][0] :
                stack.pop()
                gap += 1
            
            if not stack:
                temperatures[i] = 0
            else:
                temperatures[i] = stack[-1][1] - i
            
            stack.append((cur, i))
        
        return temperatures

            
            
            
            





            
            


        return 
        