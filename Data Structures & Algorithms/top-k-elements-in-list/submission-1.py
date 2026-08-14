class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for _ in range(len(nums) + 1)]
        d = {}

        for n in nums:
            d[n] = 1 + d.get(n, 0)

        for key, v in d.items():
            bucket[v].append(key)
        
        print(bucket)

        res = []
        for i in range(len(bucket) - 1, -1, -1):
            while bucket[i] and k > 0:
                res.append(bucket[i].pop())
                k -= 1
            
        return res

      
        