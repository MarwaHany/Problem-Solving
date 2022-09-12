class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """ 
        Do not return anything, modify nums in-place instead.
        """
        # return nums if you found only one element in it
        if len(nums) == 1:
            return nums
        # search for the first inflection point from the end
        n = range(len(nums)-1)
        inflpt_index = None
        for i in n[::-1]:
            if nums[i] < nums[i+1]:
                inflpt_index = i
                break
        if inflpt_index is None:
            nums[::] = nums[::-1]
            return
        else:
            min_diff = 101
            swap_with = inflpt_index+1
            for i in range(len(nums))[inflpt_index:]:
                if (
                    nums[i]-nums[inflpt_index] > 0 
                and nums[i]-nums[inflpt_index] < min_diff
                ):
                    swap_with = i
                    min_diff = nums[i]-nums[inflpt_index]
        nums[inflpt_index], nums[swap_with] = nums[swap_with], nums[inflpt_index]
        nums[inflpt_index+1:] = sorted(nums[inflpt_index+1:])
        
        