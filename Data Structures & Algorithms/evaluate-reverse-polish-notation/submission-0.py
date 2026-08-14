class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = 0
        stack = []
        for t in tokens:
            if t == '+':
                stack.append(stack.pop() + stack.pop())
            elif t == '-':
                first = stack.pop()
                stack.append(stack.pop() - first)
            elif t == '*':
                stack.append(stack.pop() * stack.pop())
            elif t == '/':
                first = stack.pop()
                stack.append(int(stack.pop() / first))
            else:
                stack.append(int(t))
        return stack.pop() 
                



        