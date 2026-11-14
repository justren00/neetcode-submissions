class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        suffix = 1 
        res = [0] * len(nums)

        for index, num in enumerate(nums):
            res[index] = suffix
            suffix *= num 

        prefix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= prefix 
            prefix *= nums[i]

        return res
