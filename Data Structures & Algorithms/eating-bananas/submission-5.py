class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        ''' 
        Given an eating rate of r, to find the amount of hours
        it takes to finish the piles:
            1.) for each pile, divide by the r and round up 
            2.) sum up the results 
        
        Do binary search on k, low is 1 and high is max(piles)
        Given a random rate:
            1.) find the amount of hours with that rate 
            2.) if hours > h, low = mid (rate too small)
            2.) otherwise, update res, high = mid 
        ''' 
        def hourCalculator(piles, r):
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / r)
            return hours 

        lo, hi = 1, max(piles) 
        res = max(piles)

        while lo <= hi: 
            m = (lo + hi) // 2 
            hours = hourCalculator(piles, m)

            if hours > h:
                lo = m + 1
            else:
                res = min(res, m) 
                hi = m - 1

        return res








        