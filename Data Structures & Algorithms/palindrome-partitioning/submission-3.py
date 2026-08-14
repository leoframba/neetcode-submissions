class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def is_pal(s1: str | List) -> bool:
            return s1 == s1[::-1]
        
        res = []
        ss = []
        def re(start):
            # wall
            if start >= len(s):
                # we have seen the whole string if we get here we have found a valid ss
                res.append(ss.copy())
                return

            for i in range(start, len(s)):
                curr = s[start:i + 1]
                if is_pal(curr):
                    ss.append(curr)
                    # keep going to see if the remiander of s can be cut into pal ss
                    re(i + 1)
                    # backtrack
                    ss.pop()
                # if its not a pal we keep adding values until it is
            
            return
        
        re(0)
        print(res)
        return res
        