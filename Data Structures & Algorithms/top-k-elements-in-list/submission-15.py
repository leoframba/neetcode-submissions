from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        n = len(nums)
        if n <= k:
            return list(set(nums))
        
        counts = Counter(nums)
        counts = sorted(counts.items(), key=lambda item:  item[1])


        return [counts.pop()[0] for _ in range(k)]

        