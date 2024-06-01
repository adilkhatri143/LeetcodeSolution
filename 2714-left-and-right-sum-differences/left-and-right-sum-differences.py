class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        right_sum = left_sum = 0
        answer = list()
        for num in nums:
            right_sum += num
        for num in nums:
            right_sum -= num
            answer.append(abs(right_sum - left_sum))
            left_sum += num
        return answer
