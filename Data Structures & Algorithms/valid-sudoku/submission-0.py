class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        #create sets for each row/col/subbox
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        sub = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                
                # skip we dont care about empty
                if board[r][c] == ".":
                    continue

                #calc sub
                sub_r = 3 * (r // 3) #7 -> 6
                sub_c = (c // 3) #2 -> 0
                sub_box = sub_r + sub_c
                
                # check for dupes in row/col/sub
                cur = board[r][c]
                if cur in row[r] or cur in col[c] or cur in sub[sub_box]:
                    print(f"r: {r}, c: {c}, sub: {sub_box}")
                    return False

                # adde values to set
                row[r].add(cur)
                col[c].add(cur)
                sub[sub_box].add(cur)

        return True


                
