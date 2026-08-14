from typing import List
from collections import deque

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        # Build an adj dict to handle neighbors bsed on routes
        # JFK: [SEA, HOU]
        # HOU: [JFK]
        # 
        adj = {}
        for a, b in tickets:
            adj.setdefault(a, []).append(b)
            adj.setdefault(b, [])

        # sort in reverse order so we can pop end o1
        for k in adj:
            adj[k].sort(reverse=True)

        # We always start the itinerary from JFK
        START = "JFK"
        res = []
        current_path = [START]

        # DFS approach because we need to finish a trip before starting another

        # we need to prevent the looping - edit adj dict to remove ticket once its been used
        def dfs(curr):
            #  if we hit a dead end we append to result
            
            while adj[curr]:
                next = adj[curr].pop() # due to the reverse sort this should always be the smallest val
                current_path.append(next)
                dfs(next)
            res.append(current_path.pop())
            return

         

        dfs(START)
        return res[::-1]