class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        prev2 = nums[0]
        prev = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            temp = prev 
            prev = max(prev, prev2 + nums[i])
            prev2 = temp 

        return prev
