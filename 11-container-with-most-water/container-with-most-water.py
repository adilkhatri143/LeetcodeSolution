class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        answer = 0
        while left < right:
            if height[left] < height[right]:
                answer = max(answer, height[left] * (right - left))
                left += 1
            else:
                answer = max(answer, height[right] * (right - left))
                right -= 1
        return answer