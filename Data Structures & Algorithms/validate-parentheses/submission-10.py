class Solution:
    def isValid(self, s: str) -> bool:
        d = {'{': '}', '(' : ')', '[' : ']'}
        close = []

        for c in s:
            if c in d:
                close.append(d[c])
            if c in d.values() :
                if len(close) == 0 or c != close.pop():
                    return False

        return len(close) == 0
                

        