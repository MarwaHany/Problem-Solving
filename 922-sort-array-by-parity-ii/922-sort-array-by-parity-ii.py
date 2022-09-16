class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        odd_index = 1
        while(odd_index < len(nums) and nums[odd_index]%2):
            odd_index += 2
        if odd_index < len(nums):
            for i in range(0,len(nums),2): # loop on even indeces
                # if the number is not even then switch b
                if nums[i]%2:
                    nums[odd_index],nums[i] = nums[i],nums[odd_index]
                try:
                    while(nums[odd_index]%2):
                        odd_index += 2
                except:
                    break
        return nums