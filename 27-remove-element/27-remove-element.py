class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j = 0
        count = len(nums)
        while j < len(nums):
            if nums[j] == val:
                nums.remove(val)
                j = 0
                count -= 1
            else:
                j += 1
        return count