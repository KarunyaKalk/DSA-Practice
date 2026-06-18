from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # 1. Add a sentinel/dummy value 0 to the end to flush out the stack at the finish line
        heights.append(0)
        stack = [] # Will store indices
        max_area = 0
        
        # 2. Iterate through every bar using its index
        for i, h in enumerate(heights):
            
            # While the current bar is shorter than the bar at the top of the stack
            while stack and h < heights[stack[-1]]:
                # The bar we are calculating the area for
                height_index = stack.pop()
                bar_height = heights[height_index]
                
                # If stack is empty, it means this bar was the shortest seen so far,
                # so its left boundary is effectively the start of the histogram (-1).
                # Otherwise, the new top of the stack is its left boundary.
                left_boundary = stack[-1] if stack else -1
                right_boundary = i
                
                width = right_boundary - left_boundary - 1
                current_area = bar_height * width
                
                # Track the maximum area seen so far
                max_area = max(max_area, current_area)
                
            # Push the current index onto the stack
            stack.append(i)
            
        return max_area