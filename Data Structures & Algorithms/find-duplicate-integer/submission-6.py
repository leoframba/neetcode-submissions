class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast = 0
        slow = 0
        
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if slow == fast:
                break
        
        slow2 = 0
        while slow != slow2:
            slow2 = nums[slow2]
            slow = nums[slow]
        
        return slow



        