class Solution:
    def countSubstrings(self, s: str) -> int:
        
        # edge case - invalid s
        if not s:
            return 0
        # top down
        # we start from the middle and attempt to expand

        # result tuple holds the bounds of our longest substring
        # defaults to 1 as any valid s will have a plaindrom of at least size 1

        # state is the bounds of our substring -> return t/f is its a valid palindrome
        def count_pals(left, right) -> int:
            count = 0
            while (
                left >= 0 and 
                right < len(s) and 
                s[left] == s[right]
            ):
                count += 1
                left -= 1
                right += 1
            return count
        
        res = 0
        for i in range(len(s)):
            # at each middle expand

            # attempt to expand itervely from middles
            res += (
                count_pals(i, i) + 
                count_pals(i, i + 1) 
            )
            
        
        return res
        
        

        