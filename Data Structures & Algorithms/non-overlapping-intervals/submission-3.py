class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        n = len(intervals)
        if n <= 1:
            return 0
        
        intervals = sorted(intervals, key=lambda item: item[0])
        print(intervals)
        last = 0
        res = 0
        for i in range(1, n):
            # look if there's overlap
            if intervals[last][1] > intervals[i][0]:
                res += 1
                # keep the one with the smaller end
                # w1 = intervals[i][1] -  intervals[i][0]  
                # w2 = intervals[last][1] - intervals[last][0]
                # if w2 > w1:
                #     last = i
                if intervals[last][1] > intervals[i][1]:
                    last = i
            else:
                last = i
        
        return res

        