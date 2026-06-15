class Solution:
    def arrangeCoins(self, n: int) -> int:
        l, h = 1, n
        while l < h:
            m = (l + h + 1) // 2
            if m * (m + 1) // 2 <= n:
                l = m  # Changed '1' to 'l'
            else:
                h = m - 1
        return l  # Changed '1' to 'l'