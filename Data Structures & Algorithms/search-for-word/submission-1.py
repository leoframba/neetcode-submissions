class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        
        def dfs(r, c, index) -> bool:
            char = board[r][c]

            # catch we have found the word
            if index == len(word):
                return True

            # get neighbors
            directions = (-1, 0), (1, 0), (0, -1), (0, 1) # down, up, left, right
            neighbors = []
            for dr, dc in directions:
                new_r, new_c = r + dr, c + dc
                # check that we are still in bounds
                if 0 <= new_r < rows and 0 <= new_c < cols:
                    neighbors.append((new_r, new_c))
            
            # Temp set visited flag
            board[r][c] = '#'
            
            # go tohrough the neighbors and see if we match the next char
            for nr, nc in neighbors:
                if board[nr][nc] == word[index]:
                    if dfs(nr, nc, index + 1):
                        return True
                
            board[r][c] = char
            
            return False

            

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if dfs(r, c, 1):
                        return True
        return False