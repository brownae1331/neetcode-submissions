class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        totalArea = 0
        maxL, maxR = 0, 0
        while l < r:
            maxL = max(maxL, height[l])
            maxR = max(maxR, height[r])
            if maxL <= maxR:
                l += 1
                totalArea += 0 if maxL - height[l] < 0 else maxL - height[l]
            else:
                r -= 1
                totalArea += 0 if maxR - height[r] < 0 else maxR - height[r]
        return totalArea