class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])
        lo, hi = 0, n - 1

        while lo <= hi:
            row = (lo + hi) // 2

            if target > matrix[row][m - 1]:
                lo = row + 1
            elif target < matrix[row][0]:
                hi = row - 1
            else:
                break

        if not (lo <= hi):
            return False

        row = (lo + hi) // 2

        l, r = 0, m - 1
        while l <= r:
            m = (l + r) // 2

            if matrix[row][m] > target:
                r = m - 1
            elif matrix[row][m] < target:
                l = m + 1
            else:
                return True
        
        return False
        