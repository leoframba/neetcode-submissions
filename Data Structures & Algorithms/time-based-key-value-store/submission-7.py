class TimeMap:

    def __init__(self):
        self.val_map = {}

        
    # maintain a ordered list of timestamps vs 
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.val_map[(key, timestamp)] = value
        return None
        

    def get(self, key: str, timestamp: int) -> str:
        items = self.val_map.keys()
        
        res = ("", -1)
        for k, t in items:
            if t <= timestamp and k == key and t > res[1]:
                res = (k, t)
        
        return "" if res not in self.val_map else self.val_map[res]

        
