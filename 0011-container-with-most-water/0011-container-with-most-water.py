class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1

        best = min(height[left], height[right]) * (right - left)

        while left < right:
            area = min(height[left], height[right]) * (right - left)

            best = max(area, best)

            if height[left] < height[right]:
                left += 1
            elif height[right] < height[left]:
                right -= 1
            else:
                left += 1
        return best
        