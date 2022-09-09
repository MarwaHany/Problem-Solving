from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = Counter(s)
        for char, c in count.items():
            if c == 1:
                return s.index(char)
        return -1