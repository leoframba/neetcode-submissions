class Solution:
    def search(self, nums: List[int], target: int) -> int:

        n = len(nums)
        left = 0
        right = n - 1

        while left <= right:
            mid = (left + right) // 2
            mid_val = nums[mid]

            if mid_val == target:
                return mid
            
            #which side of the list is sorted + contains our target
            r_val = nums[right]
            l_val = nums[left]

            # the left side is properly sorted in asc
            if l_val <= mid_val:
                # check if our target is between these vals
                if l_val <= target < mid_val:
                    #our target is within this range - choose left side move right pointer
                    right = mid - 1
                else:
                    # our targt is not here we can discard this side
                    left = mid + 1
            else:
                # the left val is > than the mid so the right side is sorted in asc
                #check if target is here
                if mid_val < target <= r_val:
                    left = mid + 1
                else:
                    # not here
                    right = mid - 1
        
        # not found
        return -1
        