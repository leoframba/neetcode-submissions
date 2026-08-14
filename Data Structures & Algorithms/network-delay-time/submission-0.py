from typing import List
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #dijkstra

        # create the adj list
        adj = {i: [] for i in range(n)}
        for u, v, t in times: # each node hase u -> v in t time
            adj[u - 1].append((v - 1, t)) # note if graph is undirected u must also add the return edge
        
        distances = {i: float('inf') for i in range(n)}
        distances[k - 1] = 0 # the distance to/from the strating node is 0

        min_heap = [(0, k - 1)] # (distance for minheap sort, node)

        while min_heap:
            curr_distance, u = heapq.heappop(min_heap)

            if curr_distance > distances[u]:
                continue

            for v, time in adj[u]:
                new_distance = curr_distance + time

                if new_distance < distances[v]:
                    distances[v] = new_distance
                    heapq.heappush(min_heap, (new_distance, v))
        
        print(distances)
        max_val = max(distances.values())
        return -1 if max_val == float('inf') else max_val

