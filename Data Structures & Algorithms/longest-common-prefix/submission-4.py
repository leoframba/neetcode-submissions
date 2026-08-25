class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        count = 0
        for z in zip(*strs):
            if len(set(z)) > 1:
                return strs[0][:count]
            count += 1
        
        return strs[0][:count]

        
        