from functools import cache
class Solution:
    def longestPalindrome(self, s: str) -> str:

        # edge - invalid input s
        if not s:
            return None

        #cache1 = {}
        def is_pal(left, right):
            # wall
            if left >= right:
                return True

            state = (left, right)
            # if state in cache1:
            #     return cache1[state]

            if s[left] != s[right]:
                #cache1[state] = False
                return False

            #cache1[state] = is_pal(left + 1, right - 1)
            return is_pal(left + 1, right - 1)
            

        
        # state = slice of s
        # we calc each state once using dp
        # total number of slices is n(n + 1) / 2 assuming all unique chars
        @cache
        def dp(left, right) -> tuple[int, int]:

            # wall - We will always find a plaindrome when we reach single chars
            # the min size pali of a valid input will at min be 1
            if left == right:
                return (left, 1)
            
            # Check if the current slice is a pali - because we start from the full input the first pali we find will be the longest
            # technically this will catch the wall case aswell
            if is_pal(left, right):
                return (left, right - left + 1)
            
            # else we need to choose
            cut_left = dp(left + 1, right)
            cut_right = dp(left, right - 1)

            if cut_left[1] > cut_right[1]:
                return cut_left
            else:
                return cut_right

        res = dp(0, len(s) - 1)
        return s[res[0]:res[0] + res[1]]





            


        
        