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

        # brute force - back to back pointers
        for lidx in range(n - 1):
            for ridx in range(lidx + 1, n):
                
                l_height = heights[lidx]
                r_height = heights[ridx]

                curr = min(l_height, r_height) * (ridx - lidx)
                max_water = max(max_water, curr)
        
        return max_water







        