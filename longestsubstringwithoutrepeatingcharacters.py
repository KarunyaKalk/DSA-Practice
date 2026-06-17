class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        left = 0
        char_map = {}
        
        for right, char in enumerate(s):
            # If the character is a duplicate inside the current window
            if char in char_map and char_map[char] >= left:
                left = char_map[char] + 1
            
            # Record/Update the character's latest index
            char_map[char] = right
            
            # Update the maximum length found so far
            max_len = max(max_len, right - left + 1)
            
        return max_len