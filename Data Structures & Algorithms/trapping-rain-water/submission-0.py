class Solution:
    def trap(self, height: List[int]) -> int:
        totalArea = 0
        for i in range(len(height)):
            maxLeftHeight = 0
            maxRightHeight = 0

            for l in range(i, -1, -1):
                maxLeftHeight = max(maxLeftHeight, height[l])
            for r in range(i, len(height)):
                maxRightHeight = max(maxRightHeight, height[r])

            totalArea += 0 if min(maxLeftHeight, maxRightHeight) - height[i] < 0 else min(maxLeftHeight, maxRightHeight) - height[i]

        return totalArea