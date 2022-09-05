class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum_res = 0
        org_sum = 0
        for i in range(len(nums)+1):
            org_sum += i
        for i in nums:
            sum_res += i
        return org_sum - sum_res
            
        