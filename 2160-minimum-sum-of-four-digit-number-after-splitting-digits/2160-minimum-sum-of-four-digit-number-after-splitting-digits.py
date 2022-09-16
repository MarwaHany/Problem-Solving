class Solution:
    def minimumSum(self, num: int) -> int:
        nums = []
        while(num):
            nums.append(num%10)
            num = num//10
        nums.sort()
        num1 = nums.pop(0)*10 + nums.pop()
        num2 = nums.pop(0)*10 + nums.pop()
        print(num1, num2)
        return num1 + num2
        
            
            
            
        