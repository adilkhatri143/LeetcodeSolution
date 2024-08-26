class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        window_end = ans = 0
        char_to_count = dict()
        for window_start in range(len(s)):
            char_to_count[s[window_start]] = char_to_count.get(s[window_start], 0) + 1
            while char_to_count[s[window_start]] > 2:
                char_to_count[s[window_end]] -= 1
                window_end += 1
            ans = max(ans, window_start - window_end + 1)
        return max(ans, window_start - window_end + 1)