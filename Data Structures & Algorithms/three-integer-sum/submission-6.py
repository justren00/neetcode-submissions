class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """ 
        1st important observation: a + b + c = 0 --> a + b = -c 
        2nd important observation: a + b = -c is just 2Sum
        3rd important observation: If I just used the regular 2Sum apporach
            (i.e. using a hasmap), the time complexity would be O(n^2). I can 
            get a more optimal solution if I sort nums and use the 2Sum II
            approach  
        """ 

        nums.sort()
        res = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j, k = i + 1, len(nums) - 1
            target = -1 * nums[i]

            while j < k:
                curSum = nums[j] + nums[k]
                if curSum < target:
                    j += 1
                elif curSum > target:
                    k -= 1
                else:
                    res.append([nums[i], nums[j], nums[k]]) 
                    j += 1
                    while j < len(nums) and nums[j] == nums[j - 1]:
                        j += 1
                    k -= 1
                    while k > 0 and nums[k] == nums[k + 1]:
                        k -= 1


        return res

