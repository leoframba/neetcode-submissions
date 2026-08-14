class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # sorted we can use two pointers
        n = len(numbers)
        # invalid input
        if n <= 1:
            return None

        left, right = 0, n - 1

        # wall - Bc theres always an awnser wall would be find it
        # but if we are working with production code we might not always find it soo
        # wall = left < right

        while left < right:
            curr = numbers[left] + numbers[right]
            if curr == target:
                return [left + 1, right + 1]
            elif curr < target:
                left += 1
            else: # curr > target
                right -= 1
        
        return None
        