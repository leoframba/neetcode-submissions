import heapq
from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        # we want to complete tasks with the highest qunt first to get cd rolling
        # consume tasks with highest quant
        # use max heap to track tast with highest 
        taskcount = len(tasks)
        quant = {}
        for task in tasks:
            if task in quant:
                quant[task] += 1
            else:
                quant[task] = 1
        
        counts = [(-quant[task], task) for task in quant.keys()]
        heapq.heapify(counts)

        res = 0
        q = deque()
        while taskcount != 0:
            if counts:
                taskcount -= 1
                count, task = heapq.heappop(counts)
                q.append((count + 1, task))
            else:
                q.append(())
            if len(q) > n:
                left = q.popleft()
                if left and left[0] < 0:
                    heapq.heappush(counts, left)
            res += 1
        return res
            

        

        

        