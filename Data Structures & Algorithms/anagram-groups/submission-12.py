from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #anagram = words that have the same char count

        # can create counters for each word and group them?
        # lots of memory - n * s
        # compare against current counts 
        if not strs:
            return []

        anagram_map = {}
        for string in strs:
            frozen = frozenset(Counter(string).items())
            
            # new list if not alredy in otherwise append
            anagram_map.setdefault(frozen, []).append(string)
        

        res = []
        for val in anagram_map.values():
            res.append(val)
        return res