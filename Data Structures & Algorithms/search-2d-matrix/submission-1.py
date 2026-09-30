class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        t, b = 0, len(matrix) - 1
        l, r = 0, len(matrix[0]) - 1

        row = -1

        while t <= b:
            mid = (t + b) // 2 

            if target >= matrix[mid][0] and target <= matrix[mid][-1]:
                row = mid 
                break 
            if target < matrix[mid][0]:
                b = mid - 1
            if target > matrix[mid][-1]:
                t = mid + 1

        if row == -1:
            return False 

        while l <= r:
            mid = (l + r) // 2

            if target > matrix[row][mid]:
                l = mid + 1
            elif target < matrix[row][mid]:
                r = mid - 1
            else:
                return True 

        return False



            
        