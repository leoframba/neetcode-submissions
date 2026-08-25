class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if not strs:
            return ""

        min_len = min(len(string) for string in strs)
        
        # brute
        count = 0
        while count < min_len:
            curr = strs[0][count]
            for i in range(1, len(strs)):
                if strs[i][count] != curr:
                    return strs[0][:count]
            count += 1
        
        return strs[0][:count]


                


        