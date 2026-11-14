class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        incomplete = {}

        for index, value in enumerate(nums):
            if value in incomplete: 
                return [incomplete[value], index]
            
            incomplete[target - value] = index 

        