import itertools

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
            
        dmap = {'2':"abc", '3':"def", '4':"ghi", '5':"jkl", 
                '6':"mno", '7':"pqrs", '8':"tuv", '9':"wxyz"}
        
        # 1. Generate a list of strings to combine: ["abc", "def"]
        mapped_letters = [dmap[d] for d in digits]
        
        # 2. Use itertools.product to find every combination, and join them
        # The '*' unpacks the list so product() treats each string as a separate argument
        return ["".join(combo) for combo in itertools.product(*mapped_letters)]