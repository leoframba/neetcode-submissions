from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Append a 0 to force the stack to empty at the end
        heights.append(0)
        stack = [] # Will store indices of the bars
        max_area = 0
        
        for i, h in enumerate(heights):
            # If we find a shorter bar, it's the right boundary for the stack's top
            while stack and h < heights[stack[-1]]:
                # The popped bar is the bottleneck height
                bottleneck_height = heights[stack.pop()]
                
                # Calculate the width
                # If stack is empty, the rectangle extends all the way to index 0
                if not stack:
                    width = i
                else:
                    # Width is current index (right boundary) - new stack top (left boundary) - 1
                    width = i - stack[-1] - 1
                    
                # Update max area
                max_area = max(max_area, bottleneck_height * width)
            
            # Push the current index to the stack
            stack.append(i)
            
        return max_area