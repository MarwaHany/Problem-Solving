class Solution:
    def arrangeCoins(self, n: int) -> int:
        i = 1
        n = n - 1
        while(n > i):
            i += 1
            n = n - i
        return i
        