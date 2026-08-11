class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lo = 1
        hi = len(numbers)

        while lo < hi:
            sum = numbers[lo - 1] + numbers[hi - 1]
            if sum == target:
                return [lo, hi]
            elif sum > target:
                hi = hi - 1
            else:
                lo = lo + 1
