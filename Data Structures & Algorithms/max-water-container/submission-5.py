class Solution:
    def maxArea(self, heights: List[int]) -> int:

        n= len(heights)
        # invalid inputs
        # we need at least 2 bars for a container:
        if n < 2:
            return 0

        # track our largest container
        max_water = 0

        #looks like a 2 pointer prob with each being the walls of the container

        # formula for curr container
        # curr = min(l_height, r_height) * (ridx - lidx)

        # ? where do we start the pointers
        #starting them back to back
        #vs
        #starting at ends

        # brute force - left right pointers
        left = 0
        right = n - 1
        while left < right:
            l_height = heights[left]
            r_height = heights[right]
            delta = right - left
            curr = min(l_height, r_height) * delta
            max_water = max(max_water, curr)

            # choice what pointer do we move
            #option 1 calc which move gives us the largest increase
            # move_left = min(heights[left + 1], r_height) * (delta - 1)
            # move_right = min(l_height, heights[right - 1]) * (delta - 1)
            # if move_left > move_right:
            #     left += 1
            # else:
            #     right -= 1
            # option 2 - move smaller of the two
            if l_height >= r_height:
                right -= 1
            else:
                left += 1
        
        return max_water







        