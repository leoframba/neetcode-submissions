class Solution:
            
    def getNeighbors(self, board: List[List[str]], y, x):
        neighbors = []
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dy, dx in directions:
            ny, nx = y + dy, x + dx

            if 0 <= ny < len(board) and 0 <= nx < len(board[0]):
                neighbors.append((ny, nx))
        return neighbors


    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = {}
        for w in words:
            node = root
            for c in w:
                node = node.setdefault(c, {})
            node['*'] = w 

        rows, cols = len(board), len(board[0])
        res = []

        def dfs(r, c, parent):
            char = board[r][c]
            curr_node = parent[char]
            
            # Check for word completion
            if '*' in curr_node:
                res.append(curr_node.pop('*'))
            
            # Mark cell as visited
            board[r][c] = '#'
            
            # Explore neighbors
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] in curr_node:
                    dfs(nr, nc, curr_node)
            
            # Backtrack
            board[r][c] = char
            
            # Optimization: prune only if the node is truly empty
            if not curr_node:
                parent.pop(char)
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] in root:
                    dfs(r, c, root)
        return res