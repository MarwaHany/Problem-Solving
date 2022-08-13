class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x_str = str(x)
        if  x < 0 or (len(x_str) == 2 and x % 11 != 0):
            return False
        for i in range(len(x_str)//2):
            if x_str[i] != x_str[-(i+1)]:
                del x_str
                return False
        return True