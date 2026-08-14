class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        res = [['.'] * n for _ in range(n)]
        result = []

        def is_safe(r, c):
            # check for other queens prev placed
            
            #check col
            for i in range(r - 1, -1, -1):
                if res[i][c] == 'Q':
                    return False
                
            # check - diag
            rid, cid = r - 1, c - 1
            while 0 <= rid < n and 0 <= cid < n:
                if res[rid][cid] == 'Q':
                    return False
                rid -= 1
                cid -= 1
            
            # check + diag
            rid, cid = r - 1, c + 1
            while 0 <= rid < n and 0 <= cid < n:
                if res[rid][cid] == 'Q':
                    return False
                rid -= 1
                cid += 1

            return True



        def backtrack(r, c):
            # goal - row = n
            if r == n:
                x = []
                for row in res:
                    x.append("".join(row))
                result.append(x)
                return
            
            for i in range(n):
                # attempt to place a queen of each col
                if is_safe(r, i):
                    res[r][i] = 'Q'
                    backtrack(r + 1, 0)
                res[r][i] = '.'

        backtrack(0, 0)
        return result
                
            


        