class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        c = 0
        # [0,1,4,6,7,10]
        hashmap = {nums[i]: i for i in range(len(nums))}
        c = 0
        for i in range(len(nums)):
            j = hashmap.get(nums[i] + diff)
            if not j or j <= i: 
                continue
            k = hashmap.get(nums[j] + diff)
            if not k or k <= j:
                continue
            c += 1
        return c
                