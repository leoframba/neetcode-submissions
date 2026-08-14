class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict = {}

        for c in s:
            val = dict.get(c)
            if val == None:
                dict[c] = 1
            else:
                dict[c] += 1

        for c in t:
            val = dict.get(c)
            if val == None:
                return False
            elif val > 1:
                dict[c] -= 1
            else:
                del dict[c]
        
        if not dict:
            return True
        else:
            return False

            

        