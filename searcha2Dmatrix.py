from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
            
        ROWS = len(matrix)
        COLS = len(matrix[0])
        
        low = 0
        high = (ROWS * COLS) - 1
        
        while low <= high:
            mid = (low + high) // 2
            
            # Convert 1D virtual index to 2D matrix coordinates
            row = mid // COLS
            col = mid % COLS
            
            mid_element = matrix[row][col]
            
            if mid_element == target:
                return True
            elif mid_element < target:
                low = mid + 1
            else:
                high = mid - 1
                
        return False