import bisect
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        # invalid input we need at least 2 elements
        if n <= 1:
            return None
        
        # nums is sorted so we can use binary search
        # iterate through the array and preform binary search for the remainder

        # at anmy given num if the target - num > num there is no solution because numbers are sorted

        #brute force - O(n^2) worst case we need to loop through the entire numbers n times
        for i in range(n): 
            ni = numbers[i]
            # target 3 i of 2 = 3 - 2 = 1 we cannnot find 1 if we are at 2
            if target - ni <= ni:
                break
            target_idx = bisect.bisect_left(numbers, target - ni)
            if i < target_idx < n and numbers[target_idx] == target - ni:
                return [i + 1, target_idx + 1]
        
        return None