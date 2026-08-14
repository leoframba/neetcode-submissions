class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def is_palindrome(s):
            return s == s[::-1]
        
        def backtrack(start, curr):
            # if we are at the end of the string
            if start == len(s):
                res.append(list(curr))
                return
            
            for end in range(start + 1, len(s) + 1):
                substring = s[start:end]

                if is_palindrome(substring):
                    curr.append(substring)
                    backtrack(end, curr)
                    curr.pop()
        
        backtrack(0, [])
        return res
            


        