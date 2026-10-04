class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        one, two = 0, 0

        for i in range(len(cost) - 1, -1, -1):
            temp = one
            one = min(one, two) + cost[i]
            two = temp 

        return min(one, two)
