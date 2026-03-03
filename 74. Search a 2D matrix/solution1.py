class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        l, r = 0, ROWS - 1
        mid = 0

        while l <= r:
            mid = (l + r) // 2
            if target < matrix[mid][0]:
                r = mid - 1
            elif target > matrix[mid][-1]:
                l = mid + 1
            else:
                break
        if l > r:
            return False
        
        l, r = 0, COLS - 1
        while l <= r:
            mid2 = (l + r) // 2
            if target < matrix[mid][mid2]:
                r = mid2 - 1
            elif target > matrix[mid][mid2]:
                l = mid2 + 1
            else:
                return True
        return False