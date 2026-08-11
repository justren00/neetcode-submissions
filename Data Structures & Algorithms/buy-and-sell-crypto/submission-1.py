class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_max = 0 

        if len(prices) == 1:
            return 0

        start, end = 0, 1

        while end < len(prices): 
            profit = prices[end] - prices[start] 

            if profit < 0:
                start = end
                end += 1
            else:
                if profit > curr_max:
                    curr_max = profit
                
                end += 1
        
        return curr_max
