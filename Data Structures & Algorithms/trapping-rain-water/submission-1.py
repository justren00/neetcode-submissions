class Solution:
    def trap(self, height: List[int]) -> int:
        left = [0] * len(height)
        right = [0] * len(height)

        maxLeft = 0
        maxRight = 0 

        for i in range(len(height)):
            maxLeft = max(maxLeft, height[i])
            left[i] = maxLeft

        for i in range(len(height) - 1, -1 , -1):
            maxRight = max(maxRight, height[i])
            right[i] = maxRight
        
        res = 0
        for i in range(len(height)):
            res += min(left[i], right[i]) - height[i]

        return res