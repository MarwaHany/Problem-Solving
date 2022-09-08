class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        # if the character ch does not exist in do nothing
        word_len = len(word)
        if ch not in word:
            return word
        if word_len == 1:
            return word
        # else start processing
        # first occurance of ch
        end = word.index(ch)
        new = ["" for i in range(end+1)]
        l, r = 0, end
        while l <= r:
            new[l], new[r] = word[r], word[l]
            r -= 1
            l += 1
        new = "".join(new)
        try:
            new += word[end+1:]
        except:
            pass
        return new
        
        