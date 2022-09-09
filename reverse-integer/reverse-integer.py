class Solution:
    def reverse(self, x: int) -> int:
        power = len(str(abs(x)))-1
        res_x = 0
        neg = False if x >= 0 else True
        x = abs(x)
        while power >= 0:
            reminder = x % 10
            x = x//10
            res_x += reminder * 10**power
            power -= 1
        res_x = -1 * res_x if neg else res_x 
        return 0 if (res_x > (2**31 - 1) or res_x < -2**31) else res_x
            
            