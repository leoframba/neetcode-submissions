class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # use sets to detect dupes
        # iterate over the board and place values into sets
        #inpt check
        if not board or not board[0]:
            return False

        rows, cols = len(board), len(board[0])

        row_sets = [set() for _ in range(9)]
        col_sets = [set() for _ in range(9)]
        grid_sets = [set() for _ in range(9)]

        for r in range(rows):
            for c in range(cols):
                # each item needs to go in a row/col/sub-box

                val = board[r][c]
                if val == '.':
                    continue
                grid = (r // 3) * 3 + (c // 3)
                # row
                if (
                    val in row_sets[r] or 
                    val in col_sets[c] or 
                    val in grid_sets[grid]
                ):  return False

                # add to sets
                row_sets[r].add(val)
                col_sets[c].add(val)
                grid_sets[grid].add(val)
        
        return True
                

        