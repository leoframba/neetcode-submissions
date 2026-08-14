class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return []
        
        digit_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        res = []

        def rec(start, curr):
            # need to find all combinations so a value is valid if we have done a full pass
            if start >= len(digits):
                res.append("".join(curr))
                return

            for letter in digit_map[digits[start]]:
                curr.append(letter)
                rec(start + 1, curr)

                #backtrack
                curr.pop()
            return

        rec(0, [])
        return res



        