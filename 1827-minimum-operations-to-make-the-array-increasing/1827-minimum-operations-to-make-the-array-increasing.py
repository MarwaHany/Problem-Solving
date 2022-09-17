class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # get max num
        max_num = max(nums)
        min_oper = 0 
        for i in range(1,len(nums)):
            if nums[i-1] >= nums[i]: 
                min_oper += (nums[i-1] + 1 - nums[i])
                nums[i]  = nums[i-1] + 1
        return min_oper
            
            
        