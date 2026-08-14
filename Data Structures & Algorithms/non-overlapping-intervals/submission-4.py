class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) <= 1:
            return 0
        
        # Sort by END time instead of start time
        intervals.sort(key=lambda x: x[1])
        
        res = 0
        # Instead of tracking the index, just track the end time of the last valid interval
        last_end = intervals[0][1] 
        
        for i in range(1, len(intervals)):
            # If it overlaps, we MUST remove it (increment res)
            if intervals[i][0] < last_end:
                res += 1
            # If it doesn't overlap, it becomes our new baseline
            else:
                last_end = intervals[i][1]
                
        return res