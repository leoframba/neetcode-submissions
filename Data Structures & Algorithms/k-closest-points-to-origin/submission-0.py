import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        distances = [(-(((x[0]**2) + (x[1]**2)) ** .5), i)  for i, x in enumerate(points)]
        heapq.heapify(distances)

        while len(distances) > k:
            heapq.heappop(distances)
        
        return [points[point] for _, point in distances]
        

        
        