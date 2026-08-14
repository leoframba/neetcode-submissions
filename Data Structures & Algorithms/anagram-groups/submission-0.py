class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        nested_d = {}
        result = []
        for s in strs:
            
            # convert to ana dict
            dic = {}
            for c in s:
                dic[c] = 1 + dic.get(c, 0)
            frozen = frozenset(dic.items())
            
            # check if dict is already in nested
            if frozen in nested_d:
                nested_d[frozen].append(s)
            else:
                nested_d[frozen] = [s]
        
        result = list(nested_d.values())
        return result

        
        
            

            

        


        