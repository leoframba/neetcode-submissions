from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        # topo sort approach

        # we define a heights list to track each courses # of dependencies
        # if heights[i] == 0 we can take this course without and other pre
        heights = [0] * numCourses
        
        # For a given course key we hold a value array of all courses that are dependent on the key
        # Key = prereq : value: courses that need this prereq
        adj_map = {i: [] for i in range(numCourses)}

        #populate out data structs
        for c, pre in prerequisites:
            # Bad data case - a course cannot be its own prereq or it would be unreachable
            if c == pre:
                return []
            
            # c depends on pre so we add 1 to its heights
            heights[c] += 1

            # c depends on pre
            adj_map[pre].append(c)
        
        # We can only take courses with no prereqs
        q = deque(
            i 
            for i, val in enumerate(heights)
            if val == 0
        )

        # Relax courses until we can take everything or nothing more
        res = []
        while q:
            c = q.popleft()

            for adj in adj_map[c]:
                # We reduce their height as we have now taken this course
                heights[adj] -= 1
                if heights[adj] == 0: # We have taken all the prereqs to take this course
                    q.append(adj)
            
            res.append(c) # Add to our order
        
        # If we have a full schedule we have a valid res else we cannot take all courses
        if len(res) == numCourses:
            return res
        else:
            return []



