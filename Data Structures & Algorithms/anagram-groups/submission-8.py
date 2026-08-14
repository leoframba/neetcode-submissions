from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        
        # edge
        if not strs:
            return res
        

        counts = {}

        for s in strs:
            # count the chars in the current string
            curr = frozenset(Counter(s).items())

            # check if we have already found this anagram
            # if not start a new list
            # else append the string to the current ana group
            counts.setdefault(curr, []).append(s)
        
        return list(counts.values())


        