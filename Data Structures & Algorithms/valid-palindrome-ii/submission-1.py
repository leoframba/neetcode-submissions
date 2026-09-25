class Solution:
    def validPalindrome(self, s: str) -> bool:

        # empty string is valid
        if not s:
            return True
        
        # we can have at most one error
        # we search for the error - if we find it we attempt to drop either char

        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                # we have found the error
                del_left = s[:left] + s[left + 1:]
                del_right = s[:right] + s[right + 1:]

                return del_left == del_left[::-1] or del_right == del_right[::-1]
            
            left += 1
            right -= 1
        
        return True
            
        