from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        
        # We loop while low < high (not low <= high)
        # because we are narrowing down to a single element.
        while low < high:
            mid = (low + high) // 2
            
            # Scenario A: The mid element is larger than the high element.
            # The minimum must be in the right un-sorted portion.
            if nums[mid] > nums[high]:
                low = mid + 1
            
            # Scenario B: The mid element is smaller than or equal to high.
            # The mid itself could be the minimum, or it's to the left.
            else:
                high = mid
                
        # When low == high, they both point to the minimum element.
        return nums[low]