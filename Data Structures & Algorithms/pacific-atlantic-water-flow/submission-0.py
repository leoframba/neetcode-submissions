from typing import List
from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        
        # create two sets that will hold which nodes each ocean can reach
        # each set starts with the nodes that border their respective ocean
        p_set = set()
        # first row
        for c in range(cols):
            p_set.add((0, c))
        # first col
        for r in range(rows):
            p_set.add((r, 0))

        a_set = set()
        # last row
        for c in range(cols):
            a_set.add((rows - 1, c))
        for r in range(rows):
            a_set.add((r, cols - 1))

        # create q and add all of the p set as we'll handlt those frst
        q = deque()
        for e in p_set:
            q.append(e)

        while q:
            r, c =  q.popleft()

            # look at neighbors -> can i reach a node that isnt already in out set
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc

                # we need to check the new neighbor
                # is it in bounds?
                # is it a node that isnt already in our set
                # can we get to it >=
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in p_set and heights[nr][nc] >= heights[r][c]:
                    p_set.add((nr, nc))
                    q.append((nr, nc))
        
        # once we are done with p we will do the same for A
        for e in a_set:
            q.append(e)

        while q:
            r, c =  q.popleft()

            # look at neighbors -> can i reach a node that isnt already in out set
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc

                # we need to check the new neighbor
                # is it in bounds?
                # is it a node that isnt already in our set
                # can we get to it >=
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in a_set and heights[nr][nc] >= heights[r][c]:
                    a_set.add((nr, nc))
                    q.append((nr, nc))
        
        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in p_set and (r , c) in a_set:
                    res.append([r, c])
        return res