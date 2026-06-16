class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)
        
        # If needle is longer than haystack, it's impossible to match
        if m > n:
            return -1
            
        # Loop through haystack up to the last possible starting point
        for i in range(n - m + 1):
            # Check if the substring matches the needle
            if haystack[i : i + m] == needle:
                # Return the starting index of the first match
                return i
                
        return -1