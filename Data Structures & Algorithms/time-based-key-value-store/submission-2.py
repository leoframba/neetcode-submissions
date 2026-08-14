class TimeMap:

    def __init__(self):
        self.myMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        res = self.myMap.get(key)
        if res:
            res[timestamp] = value
        else:
            self.myMap[key] = {timestamp : value}
        

    def get(self, key: str, timestamp: int) -> str:
        res = self.myMap.get(key)
        if not res:
            return ""
        
        v = res.get(timestamp)
        if v:
            return v
        
        key_list = list(res.keys())
        f = 0
        r = len(key_list) - 1

        while f <= r:
            m = (f + r) // 2
            c = key_list[m]

            if c > timestamp:
                r = m - 1
            else:
                f = m + 1
        
        if key_list[r] > timestamp:
            return ""
        else:
            return res.get(key_list[r])
            




        
        
