from typing import List
from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i: [] for i in range(numCourses)}
        degrees = [0] * numCourses

        # populate the adj list
        # key = prereq and the value is all of the lists that require it
        for course, prereq in prerequisites:
            adj[prereq].append(course)
            # we increase the degree of a course each time we append it to a preq
            degrees[course] += 1
        

        q = deque(i for i in range(numCourses) if degrees[i] == 0)
        
        valid_classes = 0
        while q:
            curr = q.popleft()

            # proccess each class with 0 prereqs removing them from the reqs of other classes
            for next in adj[curr]:
                degrees[next] -= 1
                if degrees[next] == 0:
                    q.append(next)
            
            # each time we proccess a class with 0 prereqs it means its valid to take and we add it to our total.
            valid_classes += 1
        
        # if we can properly validate all of the courses we have a valid schedule
        return valid_classes == numCourses
   





        


        
        