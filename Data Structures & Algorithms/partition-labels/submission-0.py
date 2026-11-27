class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        counts = Counter(s)
        res = []
        curLen = 0
        seen = set()

        for ch in s:
            curLen += 1 
            if ch not in seen: 
                seen.add(ch) 
            
            counts[ch] -= 1 
            if counts[ch] == 0:
                seen.remove(ch)

            if not seen:
                res.append(curLen)
                curLen = 0 

        return res 

    