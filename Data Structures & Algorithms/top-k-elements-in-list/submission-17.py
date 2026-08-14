from collections import Counter 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counts = Counter(nums)

        # count vals in freq buckets
        freq = [[] for _ in range(len(nums))]

        for key, v in counts.items():
            freq[v - 1].append(key)
        
        res = []
        for i in range(k):
            #skip empty buckets
            while freq and not freq[-1]:
                freq.pop()
            res.append(freq[-1].pop())
        
        return res

        