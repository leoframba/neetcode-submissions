from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        

        # create a list of tuple counts
        counts = [(v, k) for k, v in Counter(nums).items()]

        # create a max heap
        res = [key for _, key in heapq.nlargest(k, counts)]

        # res = []
        # for _ in range(k):
        #     if counts:
        #         res.append(heapq.heappop(counts)[1])
        #     else:
        #         break
        
        return res
        
        