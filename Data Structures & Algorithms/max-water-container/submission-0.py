class Solution:
    def maxArea(self, heights: List[int]) -> int:
        m = 0
        l, r = 0, len(heights) - 1

        while l < r:
            area = (r - l) * min(heights[l], heights[r]) 
            m = max(area, m)

            if heights[l] < heights[r]:
                l += 1
            elif  heights[r] < heights[l]:
                r -= 1
            else:
                l += 1
                r -= 1

        return m