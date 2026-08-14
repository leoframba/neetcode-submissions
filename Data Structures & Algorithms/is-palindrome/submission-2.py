class Solution:
    def isPalindrome(self, s: str) -> bool:

        left = 0
        right = len(s) - 1

        while left < right:
            # skip non alpha numeric
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            
            # convert both to lower as we ignore case
            if s[left].lower() != s[right].lower():
                return False
            
            # move pointers
            left += 1
            right -= 1
        
        return True
        