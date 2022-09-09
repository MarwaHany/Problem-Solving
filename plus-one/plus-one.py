class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = []
        # digits = 1 1 9
        carry = 1
        for digit in digits[::-1]: 
            sub_res = digit + carry
            if sub_res == 10:
                carry = 1
                sub_res = 0
            else:
                carry = 0
            result.append(sub_res)
        if carry == 1:
            result.append(carry)
        return result[::-1]    
        
            
        