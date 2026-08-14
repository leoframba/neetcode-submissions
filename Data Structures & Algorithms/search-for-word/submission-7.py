class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        # iterate through the board to find matching start

        rows, cols = len(board), len(board[0])

        visited = set()
        def dfs(r, c, i):
            if i >= len(word):
                return True


            # check neighbors
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dx, c + dy
                if (nr, nc) in visited:
                    continue
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == word[i]:
                    visited.add((r, c))
                    if dfs(nr, nc, i + 1):
                        return True
                    visited.remove((r, c))
            
            return False

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if dfs(r, c, 1):
                        return True
                    visited.clear()
        
        return False
                    
        