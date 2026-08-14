class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        res = [['.'] * n for _ in range(n)]
        result = []

        col_set = set()
        neg_diag = set()
        pos_diag = set()

        def is_safe(r, c):
            # check for other queens prev placed
            
            #check col
            # for i in range(r - 1, -1, -1):
            #     if res[i][c] == 'Q':
            #         return False
            if c in col_set:
                return False
                
            # check - diag
            # rid, cid = r - 1, c - 1
            # while 0 <= rid < n and 0 <= cid < n:
            #     if res[rid][cid] == 'Q':
            #         return False
            #     rid -= 1
            #     cid -= 1
            if r - c in neg_diag:
                return False
            
            # check + diag
            # rid, cid = r - 1, c + 1
            # while 0 <= rid < n and 0 <= cid < n:
            #     if res[rid][cid] == 'Q':
            #         return False
            #     rid -= 1
            #     cid += 1
            if r + c in pos_diag:
                return False

            return True



        def backtrack(r):
            # goal - row = n
            if r == n:
                result.append(["".join(row) for row in res])
                return
            
            for i in range(n):
                # attempt to place a queen of each col
                if is_safe(r, i):
                    # set queen
                    res[r][i] = 'Q'
                    col_set.add(i)
                    neg_diag.add(r - i)
                    pos_diag.add(r + i)

                    # explore
                    backtrack(r + 1)
                    
                    # backtrack remove queen
                    res[r][i] = '.'
                    col_set.remove(i)
                    neg_diag.remove(r - i)
                    pos_diag.remove(r + i)

        backtrack(0)
        return result
                
            


        