class Solution:
    def arrangeCoins(self, n: int) -> int:
        # First approach
        # i = 1
        # n = n - 1
        # while(n > i):
        #     i += 1
        #     n = n - i
        # return i
        # Mathematical Approach (Faster)
        return int((-1+sqrt(1+8*n))//2)
        