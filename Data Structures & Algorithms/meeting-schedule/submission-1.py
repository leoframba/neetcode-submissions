"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        n = len(intervals)
        if n <= 1:
            return True

        intervals = sorted(intervals, key=lambda interval: interval.end)

        last_end = intervals[0].end

        for i in range(1, n):
            if intervals[i].start < last_end:
                return False
            
            last_end = intervals[i].end
        
        return True
