class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        length = min(len(word1), len(word2))
        word = ""
        for i in range(length):
            word += word1[i] + word2[i]
        return word+ word1[length:] + word2[length:]
        