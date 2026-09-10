class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        # basic merge sort implementation

        def helper(nums: List[int]):
            # base case
            n = len(nums)
            if n <= 1:
                return nums
            
            mid = n // 2

            left = helper(nums[:mid])
            right = helper(nums[mid:])

            res = []
            i = j = 0

            # Compare from the FRONT (smallest to largest)
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    res.append(left[i])
                    i += 1
                else:
                    res.append(right[j])
                    j += 1

            # Append remaining elements
            res.extend(left[i:])
            res.extend(right[j:])
            return res

        return helper(nums) 
        