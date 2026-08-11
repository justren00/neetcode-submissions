class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}

        for i in range(len(nums)):
            diff = target - nums[i]

            if h.get(diff) != None: 
                return [h.get(diff), i]
            else:
                h[nums[i]] = i