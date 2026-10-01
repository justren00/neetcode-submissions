class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def calculateHours(piles, rate):
            res = 0
            for pile in piles:
                res += math.ceil(pile/rate)

            return res 

        l, r = 1, max(piles) 
        res = max(piles)

        while l <= r:
            rate = (l + r) // 2
            hours = calculateHours(piles, rate)

            if hours > h:
                l = rate + 1
            else:
                res = min(res, rate)
                r = rate - 1

        return res

        