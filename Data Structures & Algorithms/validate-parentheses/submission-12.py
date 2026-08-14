class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {'{' : '}',
            '(' : ')',
            '[' : ']'
        }

        for c in s:
            if c in d:
                stack.append(d[c])
                continue
            
            if not stack:
                return False


            peek = stack[-1]
            if c == peek:
                stack.pop()
            else:
                return False
            
        
        if not stack:
            return True
        else:
            return False
        