class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums.extend(sorted(set(nums),reverse=True))
        nums.reverse()
        return len(set(nums))