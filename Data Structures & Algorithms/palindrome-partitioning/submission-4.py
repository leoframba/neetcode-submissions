class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # palindrome = string that is the same front and back
        def is_pal(s1):
            return s1 == s1[::-1]
        
        # edge cases
        # empty string
        if not s:
            return []
        
        res = []
        # index + current partition
        def rec(start, curr):
            # wall - base
            # end of input - we have succesfully split the arry into palis
            if start >= len(s):
                res.append(curr.copy())
                return
            
            for i in range(start, len(s)):
                # find a palindrome
                # get current slice
                cut = s[start:i+1]
                if is_pal(cut):
                    # we can take it
                    curr.append(cut)
                    rec(i + 1, curr)
                    #backtrack
                    curr.pop()
                # if we dont find a pall we do nothing
            
            return
        
        rec(0, [])
        return res
        




        