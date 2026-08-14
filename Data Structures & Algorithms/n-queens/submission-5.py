class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        # need a validation check
        # is there a queen already in row/col/diag


        rows, cols = n, n


        v_c = set()
        v_posd = set()
        v_negd = set()

        board = [['.'] * n for _ in range(n)]
        res = []
        q_ct = 0
        def setQueen(r: int):
            nonlocal q_ct
            # walls

            # valid - if we have placed n queens
            if q_ct == n:
                res.append([''.join(r) for r in board])
            
            for c in range(cols):
                #attempt to place a queen
                # is current r/c valid for a queen
                # we are placing from top down so we only need to check up
                posd = r - c
                negd = r + c

                # validation
                valid_col = c not in v_c
                valid_diag = posd not in v_posd and negd not in v_negd
                valid = valid_col and valid_diag
                
                if valid:
                    # set queen
                    board[r][c] = 'Q'
                    v_c.add(c) # this col is now visited and cant be used by future queens
                    v_posd.add(posd)
                    v_negd.add(negd)
                    
                    # move to the next row
                    q_ct += 1
                    setQueen(r + 1)

                    #back track
                    q_ct -= 1
                    board[r][c] = '.'
                    v_c.remove(c) # this col is now visited and cant be used by future queens
                    v_posd.remove(posd)
                    v_negd.remove(negd)
            
            return
        
        setQueen(0)
        return res
                

        