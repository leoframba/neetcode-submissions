class Solution:
    def isValid(self, s: str) -> bool:
        
        n = len(s)
        if n % 2 != 0:
            return False

       
        open = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        

        stack = []
        for i in range(n):
            curr = s[i]
            if curr in open:
                stack.append(open[curr])
            elif not stack or curr != stack.pop():
                return False
        


        return True if not stack else False
        
        