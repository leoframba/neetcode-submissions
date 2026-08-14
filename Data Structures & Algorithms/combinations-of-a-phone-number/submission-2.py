class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
            
        d_len = len(digits)
        dmap = {
            '2' : "abc",
            '3' : "def",
            '4' : "ghi",
            '5' : "jkl",
            '6' : "mno",
            '7' : "pqrs",
            '8' : "tuv",
            '9' : "wxyz"
        }

        #Can cascade

        res = []
        d_list = [dmap[digit] for digit in digits]
        print(d_list)
        
        curr = []
        def re(didx):
            # wall
            # found a valid string = reached the end of
            if didx >= d_len:
                res.append("".join(curr))
                return
            
            chars = d_list[didx]
            for char in chars:
                curr.append(char)
                re(didx + 1)
                curr.pop() 
            
            return
        
        re(0)
        return res

        