class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        most_char = 0
        f = 0
        longest = 0

        for i in range(len(s)):
            cur = s[i]
            count[cur] = 1 + count.get(cur, 0) #update the count

            most_char = max(most_char, count[cur]) #update most comman char count

            #check if window is invalid
            w_size = (i - f + 1) - most_char
            while w_size > k:
                count[s[f]] -= 1 
                f += 1
                w_size = (i - f + 1) - most_char
            
            longest = max(longest, i - f + 1)
        return longest






        

            
            


        