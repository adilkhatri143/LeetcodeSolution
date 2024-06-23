from collections import deque
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        min_deque = deque()
        max_deque = deque()
        left = right = answer = 0
        while right < len(nums):
            while min_deque and min_deque[-1] > nums[right]:
                min_deque.pop()
            min_deque.append(nums[right])

            while max_deque and max_deque[-1] < nums[right]:
                max_deque.pop()
            max_deque.append(nums[right])

            while abs(min_deque[0] - max_deque[0]) > limit:
                if min_deque[0] == nums[left]:
                    min_deque.popleft()
                if max_deque[0] == nums[left]:
                    max_deque.popleft()
                left += 1    
        
            answer = max(answer, right - left + 1)
            right += 1
        return answer
