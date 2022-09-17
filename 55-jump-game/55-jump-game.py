class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        step = 1
        flag = True
        for i in range(len(nums)-2,-1,-1):
            if nums[i] and nums[i] >= step:
                step = 1
                flag = True
            else:
                flag = False
                step += 1
        return flag
                