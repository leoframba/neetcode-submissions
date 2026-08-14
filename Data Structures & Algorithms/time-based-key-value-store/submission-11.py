import bisect
class TimeMap:

    def __init__(self):
        self.m = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.m.setdefault(key, []).append((timestamp, value))
        return None
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.m:
            return ""
        
        entries = self.m[key]

        #entries are naturally sorted by time stamp
        cut = bisect.bisect_left(entries, timestamp + 1, key= lambda item: item[0])

        # check bounds
        if 0 < cut <= len(entries):
            return entries[cut - 1][1]
        else:
            return ""
