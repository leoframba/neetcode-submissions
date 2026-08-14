class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_size = len(s1)
        s2_size = len(s2)

        if s1_size > s2_size:
            return False

        temp = sorted(s1)
       
        #create perm map
        s1_map = {}
        for c in s1:
            s1_map[c] = 1 + s1_map.get(c, 0)


        f = 0
        r = s1_size - 1
        while r < s2_size:
            if s2[f] not in s1_map:
                f += 1
                r += 1
            else:
                print(s2[f])
                print(s2[f:r])
                if temp == sorted(s2[f:r + 1]):
                    return True
                else:
                    f += 1
                    r += 1
        return False

        