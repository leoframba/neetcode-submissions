from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        threshold = len(nums) // 3
        counts = Counter(nums)
        return [key for key, value in counts.items() if value > threshold]


        