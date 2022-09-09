class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, j = 0, 1
        while j<len(nums): # 6
            if not nums[j]:
                if nums[i]:
                    i += 1
                j += 1
            elif not nums[i]:
                if nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                    j += 1
            else:
                i += 1
                j += 1
        return nums
                
                
            