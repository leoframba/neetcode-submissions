class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        n = len(strs)
        # empty edge case
        if n == 0:
            return []
        
        count = {}
        for s in strs:
            curr = [0] * 26 # bucket counter for word

            for c in s:
                #convert to a index
                curr[ord(c) - ord('a')] += 1
            
            count.setdefault(tuple(curr), []).append(s)
        
        return list(count.values())
            
        


        