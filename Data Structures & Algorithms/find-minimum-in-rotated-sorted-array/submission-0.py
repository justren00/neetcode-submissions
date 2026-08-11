class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1

        while lo < hi:
            m = (lo + hi) // 2

            if nums[m] < nums[hi]:
                hi = m
            else:
                lo = m + 1

            print(lo)
            
        return nums[lo]
# 5 0 1 2 3 4

# 1 2 3 4 5 6