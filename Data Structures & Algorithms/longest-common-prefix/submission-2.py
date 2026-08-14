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
        pre = ""
        for tup in zip(str1, str2):
            if tup[0] == tup[1]:
                pre += tup[0]
            else:
                break

        return pre



        
        