class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        # We are going to treat the matrix as one big list to preform bsearch
        # we need a way to convert a flat idx to matrix r/c

        # matrix -> flat
        # (r * Clen) + c -- matrix[1][2] in a 3x3 = 1 * 3 + 2 = 5 bc row 0 is 0, 1, 2 row 1 is 3, 4, 5

        # flat -> matrix
        # idx // C + idx % C -- 5 -> matrix[1][2] in a 3x3 -- 5 // 3 = 1 and 5 % 3 = 2 = matrix[1][2]

        n = (rows * cols) - 1
        right = n
        left = 0

        # binary search with conversions
        while left <= right:

            # find the mid
            mid = (right + left) // 2
            r, c = mid // cols,  mid % cols

            if target == matrix[r][c]:
                return True
            elif target > matrix[r][c]:
                left = mid + 1
            elif target < matrix[r][c]:
                right = mid - 1
        
        return False



        