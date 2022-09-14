class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        try:
            return s.strip()[::-1].index(" ")
        except:
            return len(s.strip()[::-1])
        
        