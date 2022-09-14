class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if len(s) == 1:
            return 1
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
                continue
            else:
                return 2
        return 1
            