class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if not strs:
            return ""
        
        # brute
        count = 0
        while len(strs[0]) > count:
            curr = strs[0][count]
            for i in range(1, len(strs)):
                if len(strs[i]) <= count or strs[i][count] != curr:
                    return strs[0][:count]
            count += 1
        
        return strs[0][:count]


                


        