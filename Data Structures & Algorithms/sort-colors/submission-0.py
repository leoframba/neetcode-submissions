import random

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def quick(arr, low, high):
            if low >= high:
                return nums

            # pick pivot
            pivot_idx = random.randint(low, high)
            pivot = nums[pivot_idx]

            nums[pivot_idx], nums[low] = nums[low], nums[pivot_idx]

            lt = low
            gt = high
            i = low + 1

            while i <= gt:
                if nums[i] < pivot:
                    nums[i], nums[lt] = nums[lt], nums[i]
                    lt += 1
                    i += 1
                elif nums[i] > pivot:
                    nums[i], nums[gt] = nums[gt], nums[i]
                    gt -= 1
                else:
                    i += 1
            
            quick(nums, low, lt - 1)
            quick(nums, gt + 1, high)
            return nums
        
        return quick(nums, 0, len(nums) - 1)