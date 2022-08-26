class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_sub_s = ""
        max_len = 0
        for i in range(len(s)):
            # odd length
            l, r = i, i
            while(l>=0 and r<len(s) and s[r] == s[l]):
                if (r - l + 1) > max_len:
                    max_sub_s = s[l:r+1]
                    max_len = r - l + 1
                r += 1
                l -= 1
            # even length
            l, r = i, i+1
            while(l>=0 and r<len(s) and s[r] == s[l]):
                if (r - l + 1) > max_len:
                    max_sub_s = s[l:r+1]
                    max_len = r - l + 1
                r += 1
                l -= 1
        return max_sub_s