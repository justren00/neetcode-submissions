class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(state, i):
            if i == len(nums):
                res.append(state.copy())
                return 

            state.append(nums[i])
            dfs(state, i + 1)
            state.pop()
            dfs(state, i + 1) 

        dfs([], 0)
        return res 

            