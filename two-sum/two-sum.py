from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapper = defaultdict(list)
        for i in range(len(nums)):
            mapper[nums[i]].append(i)
        for i in range(len(nums)):
            index = mapper[nums[i]].pop()
            diff = target - nums[i]
            if bool(mapper.get(diff)):
                return [index, mapper.get(diff)[-1]]
                
                
            