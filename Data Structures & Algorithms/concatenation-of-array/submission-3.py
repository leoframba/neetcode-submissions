class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
            
        return nums + nums
        