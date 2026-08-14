class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals
            
        intervals.sort(key=lambda x: x[0])
        
        # This pointer tracks the index of our most recently "merged" interval
        write_idx = 0
        
        for i in range(1, len(intervals)):
            # Case 1: Overlap. Update the end time of the interval at our write_idx
            if intervals[write_idx][1] >= intervals[i][0]:
                intervals[write_idx][1] = max(intervals[write_idx][1], intervals[i][1])
                
            # Case 2: No overlap. Advance the write_idx, and overwrite the slot with the new interval
            else:
                write_idx += 1
                intervals[write_idx] = intervals[i]
                
        # Delete everything after our write_index to achieve true O(1) space in Python
        del intervals[write_idx + 1:]
        
        return intervals