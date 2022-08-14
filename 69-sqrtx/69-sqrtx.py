class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        low = 0
        high = x - 1
        mid = 0
        if x in [0,1]:
            return x
        if x == 2:
            return 1
        while low < high:
            mid = (low + high)/2
            sqr_mid = mid * mid
            if sqr_mid == x or ((mid+1)*(mid+1) > x) and (sqr_mid < x):
                del low
                del high
                del sqr_mid
                return mid
            elif ((mid-1)*(mid-1) < x) and (sqr_mid > x):
                del low
                del high
                del sqr_mid
                return mid - 1
            elif sqr_mid > x:
                high = mid
            else:
                low = mid + 1