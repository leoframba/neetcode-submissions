class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
            
        front, rear = 0, len(height) - 1
        left_max, right_max = height[front], height[rear]
        res = 0
        
        while front < rear:
            # We always process the side with the lower maximum height
            if left_max < right_max:
                front += 1
                # Update the max or add the trapped water
                left_max = max(left_max, height[front])
                res += left_max - height[front]
            else:
                rear -= 1
                # Update the max or add the trapped water
                right_max = max(right_max, height[rear])
                res += right_max - height[rear]
                
        return res
                
            


            

            

            

            

        
        