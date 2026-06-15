from typing import List

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        # Initialize your boundaries
        l, h = 0, len(arr) - 1
        
        # Loop until the pointers converge
        while l < h:
            mid = l + (h - l) // 2  # Prevents potential integer overflow
            
            if arr[mid] < arr[mid + 1]:
                # We are climbing up; peak is to the right
                l = mid + 1
            else:
                # We are climbing down; mid could be the peak or peak is to the left
                h = mid
                
        # When l == h, they are pointing exactly at the peak index
        return l