class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += "<" + s + ">"
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        flag = False
        for i, c in enumerate(s):
            if c == "<": #set start pointer
                prev = i + 1
                flag = True
            if flag == True and c == ">":
                res.append(s[prev:i])
        print(res)
        return res


