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
                res.append(curr)
                return
            
            for c in num_to_char_map[digits[index]]:
                backtrack(curr + c, index + 1)
            return
        
        backtrack("", 0)
        return res



        

        