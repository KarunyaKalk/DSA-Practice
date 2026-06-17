class Solution:
    def isValid(self, s: str) -> bool:
        # 1. Create a map for easy lookups
        # The closing bracket is the key, opening is the value
        bracket_map = {")": "(", "}": "{", "]": "["}
        
        # 2. Initialize our stack using a standard Python list
        stack = []
        
        # 3. Iterate through every character in the string
        for char in s:
            # If the character is a closing bracket
            if char in bracket_map:
                # Pop the top element if stack isn't empty, otherwise use a dummy value '#'
                top_element = stack.pop() if stack else '#'
                
                # If the mapping doesn't match the popped element, it's invalid
                if bracket_map[char] != top_element:
                    return False
            else:
                # It's an opening bracket, push it onto the stack
                stack.append(char)
        
        # 4. If the stack is empty, all brackets were matched perfectly
        return not stack