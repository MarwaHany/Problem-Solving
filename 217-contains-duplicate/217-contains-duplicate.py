from collections import defaultdict
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hashMap = defaultdict(int)
        for i in nums:
            if hashMap[i]:
                del hashMap
                return True
            else:
                hashMap[i] += 1
        del hashMap
        return False
        