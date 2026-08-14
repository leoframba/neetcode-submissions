from collections import Counter
class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        # dict of char counts
        counts = Counter(s)

        res = []
        n = len(s)
        curr = set()
        size = 0
        for i in range(n):
            # if we find a char we must use all counts before starting a new string
            # if in the meanwhile we encounter another char we must include that as well
            char = s[i] # get current char
            
            # we always add the current char
            curr.add(char)
            counts[char] -= 1 # consume one
            size += 1 
            
            if counts[char] == 0: # we must use all counts of a word or another sub seq will contain it
                curr.remove(char)
            
            if not curr: 
                res.append(size)
                size = 0
        
        return res
            

             



        