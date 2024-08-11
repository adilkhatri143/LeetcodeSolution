class Solution:
    def can_eat(self, mid, piles, h):
        total_hour = 0
        for num in piles:
            if num <= mid:
                total_hour += 1
            else:
                total_hour += (math.ceil(num / mid))
            if total_hour > h:
                return False
        return True

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maximum = max(piles)
        if len(piles) == h:
            return maximum
        low = 1
        high = maximum
        answer = -1
        while low <= high:
            mid = (low + high) // 2
            if self.can_eat(mid, piles, h):
                answer = mid
                high = mid - 1
            else:
                low = mid + 1
        return answer