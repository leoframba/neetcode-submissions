class Solution:
    def maxArea(self, heights: List[int]) -> int:

        max = 0
        rear = len(heights) - 1
        for i in range(len(heights)):
            for j in range(i + 1, len(heights)):
                curr = (j - i) * min(heights[j], heights[i])
                if curr > max:
                    max = curr
        return max
            
        