class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        i, j = 0, 0
        common = []
        nums1.sort()
        nums2.sort()
        # since we are intersecting then we only care about the parts
        # where i and j are still in their arrays
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                common.append(nums1[i])
                i += 1
                j += 1
            else:
                if nums1[i] < nums2[j]:
                    i += 1
                elif nums2[j] < nums1[i]:
                    j += 1
        return common
            