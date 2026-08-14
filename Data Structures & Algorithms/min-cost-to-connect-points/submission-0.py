import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        def calc_dist(a, b):
            return abs(a[0] - b[0]) + abs(a[1] - b[1])
        
        #build an adj list
        adj = {}
        for i in range(len(points)):
            p1 = tuple(points[i])
            adj.setdefault(i, [])
            for j in range(len(points)):
                if j == i: continue
                p2 = tuple(points[j]) 
                adj[i].append((calc_dist(p1, p2), j))
        
        res = 0
        visited = set()
        min_heap = [(0, 0)]

        while len(visited) < n:
            dist, p = heapq.heappop(min_heap)

            # if we have already conencted the node we dont need to revisit
            if p in visited: 
                continue

            # if we havent visited connect + add distance
            res += dist
            visited.add(p)

            for next_d, next_p in adj[p]:
                if next_p not in visited:
                    heapq.heappush(min_heap, (next_d, next_p)) # only push the next cost vs total in dijkstras

        return res