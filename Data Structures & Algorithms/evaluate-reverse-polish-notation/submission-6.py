class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        val_stack = []
        op_stack = []

        op_set = {'+', '-', '*', '/'}
        for i in range(len(tokens)):
            t = tokens[i]
            if t in op_set:
                v2 = val_stack.pop()
                v1 = val_stack.pop()
                if t == '+':
                    val_stack.append(v1 + v2)
                if t == '-':
                    val_stack.append(v1 - v2)
                if t == '*':
                    val_stack.append(v1 * v2)
                if t == '/':
                    val_stack.append(int(v1 / v2))
            else:
                val_stack.append(int(t))
                
        
        print(val_stack)
        print(op_stack)

        
        return val_stack.pop()


            

        