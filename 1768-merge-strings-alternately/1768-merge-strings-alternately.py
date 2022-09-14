class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        word = ""
        while i< (len(word1)+len(word2)):
            try:
                word += word1[i]
            except:
                pass
            try:
                word += word2[i]
            except:
                pass
            i += 1
        return word
        