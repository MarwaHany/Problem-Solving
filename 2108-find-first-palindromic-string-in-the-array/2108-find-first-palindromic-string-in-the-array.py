class Solution:
    def check_palindrome(self, word):
        l, r = 0, len(word)-1 
        while(l< r):
            if word[l] != word[r]:
                return False
            l+= 1
            r -= 1
        return True
            
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if self.check_palindrome(word):
                return word
        return ""