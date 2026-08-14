class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_dict = {}
        for c in s:
            if c in char_dict:
                char_dict[c] += 1
            else:
                char_dict[c] = 1
        
        for c in t:
            if c in char_dict:
                char_dict[c] -= 1
            else:
                return False
        
        for i in char_dict.values():
            if i != 0:
                return False
        return True


        