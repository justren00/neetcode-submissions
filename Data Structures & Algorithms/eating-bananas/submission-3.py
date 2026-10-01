class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def calculateHours(piles, rate):
            res = 0
            for pile in piles:
                res += math.ceil(pile/rate)

            return res 

        l, r = 1, max(piles) 
        res = 0
        best = 0

        while l <= r:
            rate = (l + r) // 2
            hours = calculateHours(piles, rate)

            if hours > h:
                l = rate + 1
            else:
                if hours >= best:
                    best = hours 
                    res = rate 

                r = rate - 1

        return res

        