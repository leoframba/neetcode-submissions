class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:

        t0 = []
        t1 = []
        t2 =[]
        for trip in triplets:
            # if any of the vals over shoot the target is invalid and bricks
            if trip[0] > target[0] or trip[1] > target[1] or trip[2] > target[2]:
                continue
            t0.append(trip[0])
            t1.append(trip[1])
            t2.append(trip[2])

        

        return False if not t0 else [max(t0), max(t1), max(t2)] == target
        
        

        