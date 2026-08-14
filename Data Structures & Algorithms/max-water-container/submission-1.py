class Solution:
    def maxArea(self, heights: List[int]) -> int:

        max = 0
        rear = len(heights) - 1
        front = 0

        while front < rear:
            
            fh = heights[front]
            rh = heights[rear]
            mh = min(heights[front], heights[rear])
            
            curr = (rear - front) * mh
            
            if curr > max:
                max = curr

            if heights[front] > heights[rear]:
                rear -= 1
                while rear > front and rh > heights[rear]:
                    rear -= 1
            else:
                front += 1
                while rear > front and fh > heights[front]:
                    front += 1
                



            
            
            


        # for i in range(len(heights)):
        #     for j in range(i + 1, len(heights)):
        #         curr = (j - i) * min(heights[j], heights[i])
        #         if curr > max:
        #             max = curr
        return max
            
        