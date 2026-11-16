class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp = [float('-infinity')] * (len(nums) + 1) 
        dp[0] = 1 
        minEnd = 1 

        for i in range(1, len(nums) + 1):
            dp[i] = max(nums[i - 1], dp[i - 1] * nums[i - 1], minEnd * nums[i- 1])
            minEnd = min(nums[i - 1], dp[i - 1] * nums[i - 1], minEnd * nums[i- 1]) 

        return max(dp[1 : len(nums) + 1])