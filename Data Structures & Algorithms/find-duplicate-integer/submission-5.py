class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        slow = nums[0]
        fast = nums[0]

        # assuming there always is an awnser
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            # we came from the same place
            if slow == fast:
                break
        
        slow2 = nums[0]

        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]
        
        return slow
        

            


        
        

        