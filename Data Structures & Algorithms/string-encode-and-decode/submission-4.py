class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            slen = len(s)
            res += str(slen) + "." + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        print(s)

        prev = 0
        delim = 0
        while delim < len(s):
            while s[delim] != ".":
                delim += 1        
            
            print(delim)
            print(prev)
            print(s[prev:delim])
            num = int(s[prev:delim])
            
            delim += 1 
            res.append(s[delim:delim + num])
            delim += num
            prev = delim


        print(res)
           
        return res


