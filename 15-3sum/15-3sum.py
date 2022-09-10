from collections import defaultdict
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        res_keys = {}
        nums.sort() # [-4,-1,-1,0,2]
        nums_len = len(nums)
        for i in range(nums_len - 2):
            l, r = i + 1, nums_len - 1
            target = 0 - nums[i]
            while(l < r):
                if nums[l] + nums[r] == target and res_keys.get((nums[i], nums[l], nums[r])) is None:
                    res.append([nums[i], nums[l], nums[r]])
                    res_keys[(nums[i], nums[l], nums[r])] = True
                    l += 1
                    r -= 1
                elif nums[l] + nums[r] < target:
                    l+=1
                else:
                    r-=1
        return res
                
               
        