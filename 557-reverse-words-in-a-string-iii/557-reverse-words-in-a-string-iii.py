class Solution:
    def reverseWords(self, s: str) -> str:
        reversed_s = ""
        words = s.split()
        length = len(words)
        for i in range(length):
            words[i] = words[i][::-1]
            reversed_s += words[i]
            if i != (length - 1):
                reversed_s += " "
        return reversed_s
            
                
        
            
        