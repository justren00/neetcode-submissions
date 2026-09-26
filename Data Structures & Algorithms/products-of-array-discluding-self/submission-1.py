class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1] * len(nums)
        suf = [1] * len(nums)

        for i in range(1, len(nums)):
            pre[i] = nums[i - 1] * pre[i - 1]

        for i in range(len(nums) - 2, -1, -1):
            suf[i] = nums[i + 1] * suf[i + 1] 

        res = []
        for i in range(len(nums)):
            res.append(pre[i] * suf[i])

        return res
       