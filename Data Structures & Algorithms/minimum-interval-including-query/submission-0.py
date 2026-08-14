class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        
        # brute force for each query iterate through intervals to find the best match
        # note the we would need to find all intervals that could contain the query and find the smallest of the valid
        # problem = iterative search takes n so could reach up to q * n

        # build a new data struct where i can avoid n look up cost

        # dict ? - Key = query # : value = [all valid intervals]

        # start by sorting intervals by their window size
        intervals = sorted(intervals, key = lambda interval: interval[1] - interval[0]) # O(n log n)

        # when we append an interval they will be sorted by window size O(n)
        interval_dict = {}
        for i in range(len(intervals)):
            start, end = intervals[i]
            
            # potential optimization ignore overlaps - if we've already handled a certain query we dont need to look at it again
            for j in range(start, end + 1):
                if j not in interval_dict:
                    # interval_len = end - start + 1
                    # interval_dict.setdefault(j, []).append(interval_len)
                    interval_dict[j] = end - start + 1
        
        # proccess queries O(q)
        res = []
        for q in queries:
            if q in interval_dict:
                res.append(interval_dict[q])
            else:
                res.append(-1)
        
        return res



