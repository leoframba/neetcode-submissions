from typing import List
from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board),  len(board[0])

        q = deque()

        # big O R * C
        # find all 'o' on the edge ie not surroundable
        for r in range(rows):
            for c in range(cols):
                # if we are on the edge of the board and we find an 'o'
                if (r == 0 or r == rows -1 or c == 0 or c == cols - 1) and board[r][c] == 'O' :
                    board[r][c] = '#'
                    q.append((r, c))

        # R * C
        # bfs using q
        while q:
            r, c = q.popleft()

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc

                # bounds check
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == 'O':
                    board[nr][nc] = '#'
                    q.append((nr, nc))
            
        # R * C
        # capture any surrounded regions. We have previously marked un-surroundable regions with the marker # so convert those back to o
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                       board[r][c] = 'X'
                if board[r][c] == '#':
                       board[r][c] = 'O'
        return
        