class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_size = len(s1)
        s2_size = len(s2)

        if s1_size > s2_size:
            return False


        f1 = [0] * 26  
        f2 = [0] * 26       

        for i in range(s1_size):
            f1[ord(s1[i]) - ord('a')] += 1
            f2[ord(s2[i]) - ord('a')] += 1

        
        if f1 == f2:
            return True

        f = 1
        i = s1_size
        while i < s2_size:
            f2[ord(s2[i]) - ord('a')] += 1
            f2[ord(s2[f - 1]) - ord('a')] -= 1
            f += 1
            i += 1
            if f1 == f2:
                return True

            
        return False

        