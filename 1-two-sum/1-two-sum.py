from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_mapper = defaultdict(list)
        for i in range(len(nums)):
            index_mapper[nums[i]].append(i)
        nums.sort()
        low = 0;
        high = len(nums) - 1;
        while low < high:
            res = nums[low]+nums[high]
            if  res == target:
                return [index_mapper[nums[low]].pop(),index_mapper[nums[high]].pop()]
            else:
                if res > target:
                    high -= 1
                else:
                    low += 1
        
        
            
    
            