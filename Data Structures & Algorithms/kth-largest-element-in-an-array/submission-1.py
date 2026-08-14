import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        maxheap = [-num for num in nums]
        maxheap = heapq.nsmallest(k, maxheap)
        res = -1
        for i in range(k - 1):
            heapq.heappop(maxheap)
        return -maxheap[0]

        

        