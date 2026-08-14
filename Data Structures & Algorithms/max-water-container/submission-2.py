class Solution:
    def maxArea(self, heights: List[int]) -> int:

        res = 0
        rear = len(heights) - 1
        front = 0

        while front < rear:
            
            fh = heights[front]
            rh = heights[rear]
            mh = min(heights[front], heights[rear])
            maxh = max(heights[front], heights[rear])
            
            curr = (rear - front) * mh
            hyp =  maxh * (rear - front - 1) 
            
            if curr > res:
                res = curr

            if res > hyp:
                rear -= 1
                front += 1
                while rear > front and rh > heights[rear]:
                    rear -= 1
                while rear > front and fh > heights[front]:
                    front += 1
            elif heights[front] > heights[rear]:
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
        return res
            
        