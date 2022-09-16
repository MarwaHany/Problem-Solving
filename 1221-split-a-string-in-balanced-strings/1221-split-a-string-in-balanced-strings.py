class Solution:
    def balancedStringSplit(self, s: str) -> int:
        balanced_count = 0
        count = 0
        for i in range(len(s)):
            if s[i] == "R":
                count += 1
            else:
                count -= 1
            if not count:
                balanced_count += 1
        return balanced_count
                
            
            