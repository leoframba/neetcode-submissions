class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        canidate = None
        count = 0

        for num in nums:
            if count == 0:
                canidate = num
            
            if num == canidate:
                count += 1
            else:
                count -= 1
        
        
        return canidate
        