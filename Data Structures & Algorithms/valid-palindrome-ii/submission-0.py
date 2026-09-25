class Solution:
    def validPalindrome(self, s: str) -> bool:

        if not s:
            return True
        
        # strip
        s = "".join(c.casefold() for c in s if c.isalnum())

        def dp(l, r, flag):
            if l >= r:
                return True
            
            # matches keep looking in
            if s[l] == s[r]:
                return dp(l + 1, r - 1, flag)
            
            # We have found a second bad match
            if flag:
                return False

            # no match delete left or right character
            del_left = dp(l + 1, r, True)
            del_right = dp(l, r - 1, True)

            return del_left or del_right
        
        return dp(0, len(s) - 1, False)


        