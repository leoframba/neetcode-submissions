class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counts = {}
        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1

        #heap = []

        #for key in counts:
         #   heapq.heappush(heap, (counts[key], key))

          #  if len(heap) > k:
           #     heapq.heappop(heap)
        
        bucket = [None] * len(nums)

        for key, value in counts.items():
            if bucket[value - 1] == None:
                bucket[value - 1] = [key]
            else:
                bucket[value - 1].append(key)
        

        ans = []
        
        for i in range(len(bucket) - 1, -1, -1):
            if bucket[i] == None:
                continue
            while k > 0 and len(bucket[i]) > 0:
                ans.append(bucket[i].pop())
                k -= 1
                
        #return [pair[1] for pair in heap]
        return ans