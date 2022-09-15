class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        # find the first element from the end that is not an odd number
        j = len(nums) - 1
        if len(nums) > 1:
            while j > 0 and nums[j]%2!=0:
                j -= 1
        i = 0
        while i < j:
            try:
                if nums[i]%2 != 0:
                    nums[j], nums[i] = nums[i], nums[j]
                    j -= 1
                    while(nums[j]%2!=0):
                        j-=1
                while nums[i]%2==0:
                    i+=1
            except:
                break
        return nums