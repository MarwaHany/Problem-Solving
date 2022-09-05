class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # if it was zeros list then return it as it is
        non_zeros = []
        if not any(nums):
            return nums
        for i in range(len(nums)):
            if nums[i] != 0:
                non_zeros.append(nums[i])
        non_zero_len = len(non_zeros)
        for i in range(len(nums)):
            if i >= non_zero_len:
                nums[i] = 0
            else:
                nums[i] = non_zeros[i]
        
        
                