from collections import Counter
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        # Look for first match
        # Once first match found we need to dfs but keep track of a visited to prevent cycles
        # visited or alter grid for in place




        # Edge cases
        #empty grid
        if not board:
            return False
        # empty word
        if not word:
            return True
        rows, cols = len(board), len(board[0])
        wordLen = len(word)

        board_counts = Counter(
            board[r][c] 
            for r in range(rows)
            for c in range(cols)
        )
        word_counts = Counter(word)
        if board_counts < word_counts:
            return False
        
        #Start from rear or front?
        if board_counts[word[0]] > board_counts[word[-1]]:
            word = word[::-1]


        def dfs(r: int, c: int, i) -> bool:
            # wall
            # found the word
            if i == len(word):
                return True
            # out of bounds
            out_of_bounds = r < 0 or r >= rows or c < 0 or c >= cols
            if out_of_bounds or word[i] != board[r][c]:
                return False
            
            # in bounds
            # Set current node to visited
            temp = board[r][c]
            board[r][c] = '#'

            # look at all directions
            look = (
                dfs(r + 1, c, i + 1) or
                dfs(r - 1, c, i + 1) or
                dfs(r, c + 1, i + 1) or
                dfs(r, c - 1, i + 1)
            )

            #back track
            board[r][c] = temp

            return look

        # Look for first match
        for r in range(rows):
            for c in range(cols):
                curr = board[r][c]
                if curr == word[0] and dfs(r, c, 0):
                    return True

        # WE did not find the word
        return False
        