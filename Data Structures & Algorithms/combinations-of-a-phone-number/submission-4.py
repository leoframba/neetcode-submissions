class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
            
        dmap = {'2':"abc", '3':"def", '4':"ghi", '5':"jkl", 
                '6':"mno", '7':"pqrs", '8':"tuv", '9':"wxyz"}
        res = [""]
        for digit in digits:
            res = [
                combo + char 
                    for combo in res 
                    for char in dmap[digit]
            ]
            
        return res