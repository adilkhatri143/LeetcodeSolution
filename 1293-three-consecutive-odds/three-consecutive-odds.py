class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        odd_count = 0
        for i in range(3):
            odd_count += arr[i] % 2
        if odd_count == 3:
            return True
        for i in range(3, len(arr)):
            odd_count -= arr[i - 3] % 2
            odd_count += arr[i] % 2
            if odd_count == 3:
                return True
        return False
