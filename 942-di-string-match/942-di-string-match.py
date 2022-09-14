class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        # I D I D
        # 0 1 0 0
        low, high = 0, len(s)
        res = [0 for i in range(high + 1)]
        for i in range(len(res) - 1):
            if s[i] == "I":
                res[i] = low
                low += 1
            else:
                res[i] = high
                high -= 1
        if s[-1] == "D":
            res[-1] = low
        else:
            res[-1] = high
        return res
                
                