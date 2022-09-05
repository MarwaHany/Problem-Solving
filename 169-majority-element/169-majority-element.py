from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        majority_factor = n//2
        counter_map = defaultdict(int)
        for i in range(n):
            counter_map[nums[i]] += 1
            if counter_map[nums[i]] > majority_factor:
                return nums[i]
        return nums[i]
                