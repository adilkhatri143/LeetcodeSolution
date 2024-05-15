class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        if len(cardPoints) == k:
            return sum(cardPoints)
        left, right = len(cardPoints) - k, len(cardPoints) - 1
        max_sum = cur_sum = sum(cardPoints[left: right + 1])
        for i in range(k):
            cur_sum -= cardPoints[left]
            left = (left + 1) % len(cardPoints)
            right = (right + 1) % len(cardPoints)
            cur_sum += cardPoints[right]
            max_sum = max(max_sum, cur_sum)
        return max_sum

