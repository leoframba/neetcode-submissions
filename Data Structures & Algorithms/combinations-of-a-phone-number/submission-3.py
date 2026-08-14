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
        
        def re(curr: str) -> None:
            # wall
            # found a valid string = reached the end of
            if len(curr) == d_len:
                res.append(curr)
                return
            
            for char in d_list[len(curr)]:
                re(curr + char)
            return
        
        re("")
        return res

        