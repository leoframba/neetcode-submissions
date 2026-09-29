import bisect
from collections import deque
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        # find the insertion point using binary
        

        # once we have the insertion point we can loop k times to compare elements to eithr our left or right

        # resulting array
        res = deque()

        # we assume that x dosent exist in the list
        pos = bisect.bisect_left(arr, x)
        #pos is now the insertion point of x
        # all values to the right are > than x and left less than

        #split the list -- we can avoid this by tracking pointers
        lower = arr[:pos]
        higher = arr[pos:]
        higher.reverse()
        print(lower, higher)
        for i in range(k):
            # logic to find closest -- calc the distance between the two
            low_dst = float('inf')
            if lower:
                low_dst = abs(lower[-1] - x)
            high_dst = float('inf')
            if higher:
                high_dst = abs(higher[-1] - x)
            
            #check if both are empty
            if not lower and not higher:
                break

            if low_dst <= high_dst:
                res.appendleft(lower.pop())
            else:
                res.append(higher.pop())
        
        return list(res)




        