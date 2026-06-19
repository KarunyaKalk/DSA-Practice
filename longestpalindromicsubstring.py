class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        def expand_around_center(l: int, r: int) -> str:
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l + 1 : r]
        
        longest = ""
        for i in range(len(s)):
            p1 = expand_around_center(i, i)
            p2 = expand_around_center(i, i + 1)
            longest = max(longest, p1, p2, key=len)
            
        return longest