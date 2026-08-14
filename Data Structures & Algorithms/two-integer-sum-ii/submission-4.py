import bisect

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers) - 1, -1, -1):
            # if numbers[i] >= target:
            #     continue
            diff = target - numbers[i]

            b = bisect.bisect_left(numbers[:i], diff)
            if b != len(numbers) and numbers[b] == diff:
                return [b + 1, i + 1]
                
            
            
            # point = 0
            
            # while numbers[point] < diff:
            #     point += 1
            
            # if numbers[point] == diff:
            #     return [point + 1, i + 1]
        return []


        


        