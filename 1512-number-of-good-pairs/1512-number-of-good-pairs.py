class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        nums_map = {}
        res = []
        for i in range(len(nums)):
            if nums_map.get(nums[i]) is None:
                nums_map[nums[i]] = [i]
            else:
                nums_map[nums[i]].append(i)
                j = 0
                while(j < len(nums_map[nums[i]])):
                    if nums_map[nums[i]][j] != i:
                        res.append([nums_map[nums[i]][j], i])
                    j+= 1
        return len(res)
    