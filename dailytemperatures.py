from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # 1. Initialize the result array with 0s
        n = len(temperatures)
        answer = [0] * n
        
        # 2. Stack to keep track of the indices
        stack = []
        
        # 3. Iterate through the array using indices
        for current_day, current_temp in enumerate(temperatures):
            
            # While stack is not empty and current temp is warmer than the stack's top temp
            while stack and current_temp > temperatures[stack[-1]]:
                prev_day = stack.pop()
                # Calculate the days waited
                answer[prev_day] = current_day - prev_day
            
            # Append the current day's index to the stack
            stack.append(current_day)
            
        return answer