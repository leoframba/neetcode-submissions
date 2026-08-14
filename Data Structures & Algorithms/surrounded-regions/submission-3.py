from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:

        # empty board
        if not board or not board[0]:
            return None
        
        rows, cols = len(board), len(board[0])

        # Approach - Start from edges and find any O's
        # From those tiles we preform a bfs/dfs and look for any safe os

        # Nodes that aren't surroundable
        safe = set()

        # Start by adding any Os at the edges
        # row 0 + -1
        for c in range(cols):
            if board[0][c] == 'O':
                safe.add((0, c))
            if board[-1][c] == 'O':
                safe.add((rows - 1, c))
        # cols
        for r in range(rows):
            if board[r][0] == 'O':
                safe.add((r, 0))
            if board[r][-1] == 'O':
                safe.add((r, cols - 1))
        
        q = deque(safe)
        while q:
            r, c = q.popleft()

            # search
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc

                #validte new location
                is_valid = (
                    0 <= nr < rows and 0 <= nc < cols # inbounds
                    and board[nr][nc] == 'O' # has to be an 0
                    and (nr, nc) not in safe # has to be new
                )

                if is_valid:
                    safe.add((nr, nc))
                    q.append((nr, nc))
        
        # Once we have found all safe tiles - Capture non safe
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O' and (r, c) not in safe:
                    board[r][c] = 'X'
        
        return None

        
        