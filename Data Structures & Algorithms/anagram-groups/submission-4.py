class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # edge cases for empty/single item list
        if not strs:
            return [[""]]
        if len(strs) == 1:
            return [strs]

        # list >1 items
        ans = [[strs[0]]]

        for s1 in strs[1:]:
            flag = False 
            for s2 in ans:
                if self.isAnagram(s2[0], s1):
                    s2.append(s1)
                    flag = True
            if not flag:
                ans.append([s1])
        
        return ans
                  
            



    def isAnagram(self, str1: str, str2: str) -> bool:
        if len(str1) != len(str2):
            return False
        
        map = {}
        for s in str1:
            if s in map:
                map[s] += 1
            else:
                map[s] = 1
        
        for s in str2:
            if s in map and map[s] > 0:
                map[s] -= 1
            else:
                return False
        
        #print(map.values())
        for v in map.values():
            if v != 0:
                return False

        return True
                



        

        
        