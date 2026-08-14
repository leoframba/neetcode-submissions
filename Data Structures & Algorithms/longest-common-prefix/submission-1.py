class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        # if empty longest prefix is empty
        if not strs:
            return ""
        
        # if only one string longest prefix is the only string
        if len(strs) == 1:
            return strs[0]


        # we 2+ strings
        currPre = strs[0]

        for str in strs[1:]:
            currPre = self.findLongestPrefix(currPre, str)

        return currPre



    
    def findLongestPrefix(self, str1: str, str2: str) -> str:
        shorter = min(str1, str2, key=len)
        pre = ""
        for i, c in enumerate(shorter):
            if str1[i] == str2[i]:
                pre += c
            else:
                break
        
        return pre



        
        