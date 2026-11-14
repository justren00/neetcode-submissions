class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i, n in enumerate(nums):
            if i > 0 and n == nums[i - 1]:
                continue 

            l = i + 1
            r = len(nums) - 1
            target = -1 * n
            while l < r:
                curr = nums[l] + nums[r]
                if curr < target:
                    l += 1
                elif curr > target:
                    r -= 1
                else: 
                    res.append([n, nums[l] , nums[r]])
                    l += 1
                    r -= 1

                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1 

        return res

                