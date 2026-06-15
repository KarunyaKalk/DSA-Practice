class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # Step 1: Initialize the boundary pointers
        left, right = 1, num
        
        # Step 2: Loop while the search space is valid
        while left <= right:
            # Step 3: Find the middle element
            mid = (left + right) // 2
            square = mid * mid
            
            # Step 4: Check our three conditions
            if square == num:
                return True
            elif square > num:
                right = mid - 1  # Look in the lower half
            else:
                left = mid + 1   # Look in the upper half
                
        # Step 5: If the loop finishes without finding a match
        return False