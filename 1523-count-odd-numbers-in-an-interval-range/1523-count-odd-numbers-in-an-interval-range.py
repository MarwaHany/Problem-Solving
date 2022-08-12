class Solution(object):
    def countOdds(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        count = 0
        # idea :: from 1 -> 10 there is 5 odd numbers 
        if not low%2 and not high%2:
            count += 1
        else:
            count += 1 if low %2 != 0 else 0
            count += 1 if high %2 != 0 else 0
        count += int((high - low-1)/2)
        return count
        