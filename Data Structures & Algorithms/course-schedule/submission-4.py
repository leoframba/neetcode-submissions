from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # edge - only one course
        if numCourses == 0:
            return True
        # edge - no reqs = everything can be taken
        if not prerequisites:
            return True    
        # topological sort

        # Create a map
        # course -> courses that rely on this course

        req_count = [0 for i in range(numCourses)]
        depends = {i: [] for i in range(numCourses)}
        for prereq, course in prerequisites:
            if prereq == course:
                return False
            depends[prereq].append(course)
            req_count[course] += 1
        

        # Our init state is courses that have no preq
        q = deque(
            i
            for i, v in enumerate(req_count)
            if v == 0
        )

        while q:
            pre = q.popleft()

            for course in depends[pre]:
                req_count[course] -= 1
                if req_count[course] == 0:
                    q.append(course)
        
        return max(req_count) == 0

        