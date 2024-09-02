class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        total = sum(chalk)
        rem = k % total
        if rem == 0: return 0
        for idx, val in enumerate(chalk):
            if val > rem:
                return idx
            rem -= val
        return 0

