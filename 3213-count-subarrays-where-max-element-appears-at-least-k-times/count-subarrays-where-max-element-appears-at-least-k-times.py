class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        max_element = max(nums)
        left = answer = max_element_count = 0
        for right in range(n):
            if nums[right] == max_element:
                max_element_count += 1
            while max_element_count >= k:
                answer += (n - right)
                if nums[left] == max_element:
                    max_element_count -= 1
                left += 1
        return answer