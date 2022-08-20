class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        nums.sort(reverse=True)
        counts = Counter(nums)
        return [i[0] for i in counts.most_common(k)]