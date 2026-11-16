class Solution:
    def rob(self, nums: List[int]) -> int:
        one, two = 0, 0 # base case 
        # one = dp[i - 2]
        # two = dp[i - 1]
        for num in nums:
            temp = two 
            two = max(one + num, two) # two is the current
            one = temp 
        return two 