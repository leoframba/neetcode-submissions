from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = [0] * numCourses
        adj = {}
        # add all courses
        for course in range(numCourses):
            adj[course] = []
        # add all prereqs
        for pre in prerequisites:
            course = pre[0]
            req = pre[1]

            adj[course].append(req)

        def has_cycle(course_num):
            state = visited[course_num]

            if state == 1: # cycle has been found
                return True
            if state == 2: # already passed cycle check prev we can skip
                return False
            
            # state must be 0 -- preform cycle check
            
            #set the state to visiting
            visited[course_num] = 1

            if course_num in adj: # check if we have pre reqs
                # check adj
                for n in adj[course_num]:
                    if has_cycle(n):
                        return True
            
            visited[course_num] = 2
            return False
                


        for i in range(numCourses):
            if visited[i] == 0: #has not been visited run cycle check
                if has_cycle(i):
                    return False
        
        return True
            
        


        
        