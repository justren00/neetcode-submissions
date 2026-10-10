class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(subset, remain):
            if len(subset) == len(nums):
                res.append(subset.copy())
                return 

            for i in range(len(remain)):
                if remain[i] == True:
                    subset.append(nums[i])
                    remain[i] = False
                    dfs(subset, remain)
                    subset.pop()
                    remain[i] = True 
        dfs([], [True] * len(nums))
        return res