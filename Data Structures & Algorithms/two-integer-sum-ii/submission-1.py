class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        h, t = 0, len(numbers) - 1 #cratingo head and tial pointer

        while h < t: # converge pointers
            cur = numbers[h] + numbers[t]
            if cur == target:
                return [h + 1, t + 1]
            if cur > target:
                t -= 1
            if cur < target:
                h += 1
        return []


        