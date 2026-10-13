class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        one, two = 0, 0
        for i in range(1, len(nums)):
            temp = two
            two = max(one + nums[i], two)
            one = temp 

        three, four = 0, 0
        for i in range(len(nums) - 1):
            temp = four
            four = max(three + nums[i], four)
            three = temp 

        return max(two, four)