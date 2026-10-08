class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = float('-inf')
        curSum = 0

        for r in range(len(nums)):
            if curSum < 0:
                curSum = nums[r]
            else:
                curSum = curSum + nums[r]
            maxSum = max(curSum, maxSum)

        return maxSum        