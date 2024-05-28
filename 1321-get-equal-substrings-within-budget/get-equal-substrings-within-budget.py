class Solution:
    def equalSubstring(self, s: str, t: str, max_cost: int) -> int:
        window_start = window_end = ans = cur_ans = 0
        while window_start < len(s):
            cur_ans += abs(ord(s[window_start]) - ord(t[window_start]))
            while window_end <= window_start and cur_ans > max_cost:
                cur_ans -= abs(ord(s[window_end]) - ord(t[window_end]))
                window_end += 1
            ans = max(ans, window_start - window_end + 1)
            window_start += 1
        return ans