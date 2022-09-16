class Solution:
    def maximum69Number (self, num: int) -> int:
        temp = num
        digits = []
        while(temp):
            digits.append(temp%10)
            temp = temp//10
        digits = digits[::-1]
        try:
            index = digits.index(6)
        except:
            return num
        digits[index] = 9
        res = 0
        digits = digits[::-1]
        for i in range(len(digits)):
            res += digits[i]*10**i
        return res
            
            
        