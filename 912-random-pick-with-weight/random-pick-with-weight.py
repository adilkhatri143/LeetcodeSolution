import random
class Solution:
    def __init__(self, w: List[int]):
        self.cummulative_sum = []
        self.total_sum = 0
        for idx, val in enumerate(w):
            self.total_sum += val
            self.cummulative_sum.append(self.total_sum)

    def pickIndex(self) -> int:
        randval = random.randint(1, self.total_sum)
        left, right = 0, len(self.cummulative_sum) - 1
        while left < right:
            mid = (left + right) // 2
            if randval <= self.cummulative_sum[mid]:
                right = mid
            else:
                left = mid + 1
        return left


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()