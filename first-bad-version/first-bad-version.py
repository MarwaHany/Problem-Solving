# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        if n == 1:
            return 1 if isBadVersion(n) else -1
        left, right= 1, n
        while left < right :
            middle = (left + right)//2
            if not isBadVersion(middle):
                left = middle + 1
            else:
                right = middle
        return left
                
        