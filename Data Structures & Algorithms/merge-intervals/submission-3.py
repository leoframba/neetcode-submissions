class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        n = len(intervals)

        #edge
        if n <= 1:
            return intervals
        

        # sort we can force prev[0] <= later[0]
        stack = sorted(intervals[:], reverse=True)
        print(stack)
        res = []
        while len(stack) > 1:
            prev = stack.pop()
            later = stack.pop()
            

            # case no overlap
            if prev[1] < later[0]:
                # we can confirm that the prev is safe 
                res.append(prev)
                stack.append(later)
                continue
            
            # matching starts - we take the later of the ends
            # in this case one interval is consumed so we have no "safe interval to append"
            # if prev[0] == later[0]:
            #     prev[1] = max(prev[1], later[1])
            #     stack.append(prev)
            #     continue
            
            # the ending of prev is within the later interval - merge intervals
            if prev[1] >= later[0]:
                prev[1] = max(prev[1], later[1])
                stack.append(prev)
                continue
        
        res.append(stack[0])
        return res
            

        