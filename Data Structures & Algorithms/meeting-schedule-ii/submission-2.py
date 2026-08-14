"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
from collections import deque
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        n = len(intervals)
        if n <= 1:
            return n
        

        intervals = sorted(intervals, key=lambda interval: interval.start)
        
        # iter throught times. If we find an overlap we need to 

        # ? is at any given point what is the max amount of overlapping times

        #brute force would be at any given time look through every other time to count overlaps and take max - n^2

        # we potentially do this in a single pass by tracking at any given point the # of rooms + the current start/end

        q = [] # track the current rooms in use
        res = 0
        for i in range(n):
            start, end = intervals[i].start, intervals[i].end

            # pop all rooms that have ended by the time the curr metting starts
            # while q and start >= q[0].end:
            #     q.popleft()
            # q.append(intervals[i])
            # res = max(res, len(q))
            while q and start >= q[0][0]:
                heapq.heappop(q)
            
            heapq.heappush(q, (end, start))
            res = max(res, len(q))
        
        return res




