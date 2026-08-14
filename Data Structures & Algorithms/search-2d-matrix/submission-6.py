import bisect
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # find the row
        row = bisect.bisect_left([item[0] for item in matrix], target)
        if 0 <= row < len(matrix) and matrix[row][0] == target:
            return True

        #search cols
        if 0 < row <= len(matrix):
            col = bisect.bisect_left(matrix[row - 1], target)
            return 0 <= col < len(matrix[row - 1]) and matrix[row - 1][col] == target
        
        return False


        