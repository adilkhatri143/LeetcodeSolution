class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1
        low = min(bloomDay)
        high = max(bloomDay)
        days = -1
        while low <= high:
            mid = (low + high) // 2
            count = 0
            bouquets = 0
            for i in range(len(bloomDay)):
                if bloomDay[i] <= mid:
                    count += 1
                    if count == k:
                        count = 0
                        bouquets += 1
                else:
                    count = 0
            if bouquets >= m:
                days = mid
                high = mid - 1
            else:
                low = mid + 1
        return days
             
                