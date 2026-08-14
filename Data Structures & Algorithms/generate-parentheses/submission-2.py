class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(open_count, closed_count, path):
            # Base Case: Our string has used all n pairs
            if len(path) == n * 2:
                res.append(path)
                return
            
            # Decision 1: Add an open parenthesis
            # We can do this as long as we haven't reached our limit of n
            if open_count < n:
                backtrack(open_count + 1, closed_count, path + "(")
                
            # Decision 2: Add a closed parenthesis
            # We can ONLY do this if there is an unmatched open parenthesis
            if closed_count < open_count:
                backtrack(open_count, closed_count + 1, path + ")")
                
        # Kick off the recursion with 0 open, 0 closed, and an empty string
        backtrack(0, 0, "")
        
        return res