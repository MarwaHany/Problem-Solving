class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        #[16, 1] [0,9,100]
        #  l           r
        res = []
        if len(nums) == 1:
            return [nums[0]**2]
        elif nums[0] < 0: # merge two sorted lists
            # get the first positive number
            r = 0
            while(r < len(nums) - 1 and nums[r]<0):
                r = r+1
            l = r - 1
            # start merging two sorted arrays
            while r < len(nums) and l >= 0:
                if nums[r]**2 < nums[l]**2:
                    res.append(nums[r]**2)
                    r += 1
                else:
                    res.append(nums[l]**2)
                    l -= 1
            while r<len(nums):
                res.append(nums[r]**2)
                r += 1
            while l >= 0:
                res.append(nums[l]**2)
                l -= 1
        return res if res else [num**2 for num in nums]
                
            
        
                
                
                