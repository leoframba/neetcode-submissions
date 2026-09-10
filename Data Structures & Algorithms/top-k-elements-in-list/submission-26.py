from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #bucket sort

        # We know the max frequency an item can be is of size n given every element in num is of one type
        n = len(nums)

        # each index = count
        buckets = [[] for _ in range(n + 1)]
        counts = Counter(nums)

        for key, count in counts.items():
            buckets[count].append(key)
        flat = [
            key 
            for bucket in buckets if bucket
            for key in bucket
        ]
        
        return flat[-k:]
       
        