class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        res = []
        num_to_char_map = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }

        

        
        def backtrack(curr, index):
            # we've proccesed all letters
            if index == len(digits):
                res.append("".join(curr))
                return
            
            for c in num_to_char_map[digits[index]]:
                curr.append(c)
                backtrack(curr, index + 1)
                curr.pop()
            
            return
        
        backtrack([], 0)
        return res



        

        