class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        big_p = 0
        for p in piles:
            big_p = max(big_p, p)
        
        f = 1
        r = big_p
        res = big_p
        while f <= r:
            m = math.ceil((r + f) / 2)
            print(m)
            cur_tot = 0
            for p in piles:
                div = p / m
                div = int(div) + (div > int(div))
                cur_tot += div
            print(cur_tot)
            
            if cur_tot > h:
                f = m + 1
            else:
                res = m
                r = m - 1
        
        return res
        
        
        