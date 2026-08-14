import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # The max pile size - By setting k to this val we can eat all bananas in len(piles) hours
        max_k = max(piles)

        # but we need to find the min...

        # brute force - try all values till we can no longer eat in h

        # time to eat a given pile
        #sum of all ttes has to be less than or = h
        time = len(piles)
        best_rate = max_k
        # while we are within time calc a lower rate

        def validate_rate(rate):
            time = 0

            for pile in piles:
                time += math.ceil((pile / rate))

            return time <= h

        # we can view the possible rates as a sorted list
        # 0 is impossible and max_k is gaurunteed in a vlid input
        left, right = 1, max_k - 1
        
        res = max_k
        while left <= right:
            mid = (left + right) // 2

            if validate_rate(mid):
                res = mid
                # we need to try faster
                right = mid - 1
            else:
                # we need to try slower
                left = mid + 1
        
        return res



        