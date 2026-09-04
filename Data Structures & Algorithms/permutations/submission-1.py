class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(cur, chosen):
            if len(cur) == len(nums):
                res.append(cur.copy())
                return 

            for i in range(len(nums)):
                if chosen[i] == True:
                    continue 

                cur.append(nums[i])
                chosen[i] = True 
                dfs(cur, chosen)
                cur.pop()
                chosen[i] = False


        dfs([], [False] * len(nums))
        return res