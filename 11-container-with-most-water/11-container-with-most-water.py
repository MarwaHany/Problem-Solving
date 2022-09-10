class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        l, r = 0, len(height) - 1 
        while(l < r):
            w = r - l
            h = height[r] if height[r] < height[l] else height[l]
            max_area = max(max_area, w * h)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_area