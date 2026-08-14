class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        vals = []

        op_set = {'+', '-', '*', '/'}

        for token in tokens:
            if token not in op_set:
                vals.append(int(token))
            else:
                b, a = vals.pop(), vals.pop() 
                if token == '+':
                    vals.append(a + b)
                elif token == '-':
                    vals.append(a - b)
                elif token == '*':
                    vals.append(a * b)
                elif token == '/':
                    vals.append(int(a / b))
            
        
        return vals[0]
            


        