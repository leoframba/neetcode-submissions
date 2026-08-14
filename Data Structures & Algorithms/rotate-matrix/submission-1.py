class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
    
        n = len(matrix)
        for r in range(n):
            for c in range(r, n):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]


        for r in range(n):
            matrix[r].reverse()
        