from functools import cache

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        
        @cache
        def solve(i: int, j: int) -> int:
            # Base Case 1: If the start pointer crosses the end pointer, length is 0
            if i > j:
                return 0
            
            # Base Case 2: If pointers point to the same character, it's a palindrome of length 1
            if i == j:
                return 1
            
            # Scenario 1: Characters match
            if s[i] == s[j]:
                return 2 + solve(i + 1, j - 1)
            
            # Scenario 2: Characters don't match, take the best outcome of skipping either side
            return max(solve(i + 1, j), solve(i, j - 1))
        
        # Call the helper function spanning the entire string
        return solve(0, len(s) - 1)