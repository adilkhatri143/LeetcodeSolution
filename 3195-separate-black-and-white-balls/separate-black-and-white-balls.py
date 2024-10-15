class Solution:
    def minimumSteps(self, s: str) -> int:
        white_ball = min_swap = 0
        for ch in s:
            if ch == "1":
                white_ball += 1
            else:
                min_swap += white_ball
        return min_swap