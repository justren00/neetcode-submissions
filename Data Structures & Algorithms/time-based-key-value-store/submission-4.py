class TimeMap:

    def __init__(self):
        self.hashMap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashMap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        stamps = self.hashMap.get(key, [])
        l,r = 0, len(stamps) - 1
        res = ""

        while l <= r:
            m = (l + r) // 2
            
            if stamps[m][0] > timestamp:
                r = m - 1
            else:
                res = stamps[m][1]
                l = m + 1
        
        return res


        
