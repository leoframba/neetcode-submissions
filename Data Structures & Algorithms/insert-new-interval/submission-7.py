import bisect
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        inters = {interval[0] : interval [1] for interval in intervals}
        
        flat = [item for sublist in intervals for item in sublist]

        start = bisect.bisect_left(flat, newInterval[0])
        end = bisect.bisect_left(flat, newInterval[1])

        print(start)
        print(end)

        # look at the insertion points

        # if a val is odd it conflicts with a current interval
        #place start
        
        front = flat[:start]
        if start % 2 == 0:
            front += [newInterval[0]]
        back = flat[end:]
        if end % 2 == 0:
            if end < len(flat) - 1 and flat[end] == newInterval[1]:
                back = flat[end + 1:]
            else:
                back = [newInterval[1]] + back

        res = front + back
        print(front)
        print(back)
        result = []
        for i in range(0, len(res), 2):
            result.append([res[i], res[i + 1]])
        return result         
        

        

        