class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count_map = {}
        for i in nums:
            if count_map.get(i):
                return True
            else:
                count_map[i] = 1
        return False