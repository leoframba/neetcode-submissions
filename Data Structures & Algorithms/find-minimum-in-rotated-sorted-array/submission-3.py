class Solution:
    def findMin(self, nums: List[int]) -> int:
        # the min number is always going to be the number after a larger val
        # ie if the if we ever see two numbers in non ascending order we have found our min

        #binary sort - but we also need to track the end values to determine which direction to look
        n = len(nums)
        left = 0
        right = n - 1

        while left <= right:
            mid = (left + right) // 2

            lval = nums[left]
            rval = nums[right]
            midval = nums[mid]

            # eliminate a half
            # if the rval is greater we can eliminate every index pas mid
            if midval < rval:
                right = mid
            elif midval > rval:
                left = mid + 1
            else:
                return midval
        return None
                



             
            
        
        return None
