class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """ 
        input: list of integers 
        output: true if we can reach las pos false
        if not  
        questions: 
        - if nums is empty, is it true or false 

        Brute Force: Try every possible path. 
        Time Complexity: O(largest step ^ n)
        """ 

        goal = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            while nums[i] > 0 and nums[i] + i > goal:
                nums[i] -= 1 

            if nums[i] + i == goal:
                goal = i 

        return True if goal == 0 else False