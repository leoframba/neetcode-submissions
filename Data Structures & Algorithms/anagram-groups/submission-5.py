class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # edge cases for empty/single item list
        if not strs:
            return [[""]]
        if len(strs) == 1:
            return [strs]

        # list >1 items
        ans_dict = {}
        
        sorted_strs = []
        for s in strs:
            sort = "".join(sorted(s))
            if sort in ans_dict:
                ans_dict[sort].append(s)
            else:
                ans_dict[sort] = [s]
            
        return list(ans_dict.values())
                  
                



        

        
        