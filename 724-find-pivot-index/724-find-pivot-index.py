class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # for i in range(len(nums)):
        #     if sum(nums[:i]) == sum(nums[i+1:]):
        #         return i
        # return -1
        # Optimized solution
        nums_sum = sum(nums)
        left_handside_sum = 0
        
        for index, num in enumerate(nums):
            if num+2*left_handside_sum == nums_sum:
                return index
            else:
                left_handside_sum += num
        return -1