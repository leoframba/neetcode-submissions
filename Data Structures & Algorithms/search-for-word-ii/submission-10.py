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
        # make the trie
        root = {}
        for w in words: # insert words
            node = root
            for c in w: # letter by letter
                node = node.setdefault(c, {})
            node['*'] = w # add a field for the complete word

        rows, cols = len(board), len(board[0])
        res = []

        def dfs(r, c, parent):
            char = board[r][c]
            curr_node = parent[char]

            if '*' in curr_node:
                res.append(curr_node.pop('*'))
            
            board[r][c] = '*'

            neighbors = self.getNeighbors(board, r, c)
            for n in neighbors:
                if board[n[0]][n[1]] in curr_node:
                    dfs(n[0], n[1], curr_node)
            
            board[r][c] = char

            # if not curr_node:
            #     parent.pop(char)
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] in root:
                    dfs(r, c, root)
        return res