class Solution:
    def trap(self, height: List[int]) -> int:
        left_pointer = 0
        right_pointer = len(height) - 1
        max_left_height = height[left_pointer]
        max_right_height = height[right_pointer]
        answer = 0
        while left_pointer <= right_pointer:
            if height[left_pointer] < height[right_pointer]:
                max_left_height = max(max_left_height, height[left_pointer])
                answer += max(0, max_left_height - height[left_pointer])
                left_pointer += 1
            else:
                max_right_height = max(max_right_height, height[right_pointer])
                answer += max(0, max_right_height - height[right_pointer])
                right_pointer -= 1
        return answer