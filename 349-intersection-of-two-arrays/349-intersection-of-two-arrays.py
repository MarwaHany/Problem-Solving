class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        i, j = 0, 0
        common = []
        # since we want the intersection point of these
        # two lists; then we will only care about the 
        # part where i and j are pointing on something 
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
        return set(common)
                
                