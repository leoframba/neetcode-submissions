class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == '(':
                stack.append(')')
            elif c == '[':
                stack.append(']')
            elif c == ('{'):
                stack.append('}')
            elif c in {')', '}', ']'}:
                if not stack or stack.pop() != c:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False

        