class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # Step 1: Ensure nums1 is the smaller array to optimize binary search
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        
        m, n = len(nums1), len(nums2)
        low, high = 0, m
        half_len = (m + n + 1) // 2
        
        # Step 2: Binary search for the correct partition index in nums1
        while low <= high:
            i = (low + high) // 2
            j = half_len - i
            
            # Step 3: Handle boundary conditions with infinity guards
            left1 = nums1[i - 1] if i > 0 else float('-inf')
            right1 = nums1[i] if i < m else float('inf')
            
            left2 = nums2[j - 1] if j > 0 else float('-inf')
            right2 = nums2[j] if j < n else float('inf')
            
            # Step 4: Check if we have partitioned the arrays correctly
            if left1 <= right2 and left2 <= right1:
                # If the total number of elements is odd
                if (m + n) % 2 == 1:
                    return float(max(left1, left2))
                # If the total number of elements is even
                return (max(left1, left2) + min(right1, right2)) / 2.0
            
            elif left1 > right2:
                # nums1's left element is too big, move partition i to the left
                high = i - 1
            else:
                # nums2's left element is too big, move partition i to the right
                low = i + 1
                
        return 0.0