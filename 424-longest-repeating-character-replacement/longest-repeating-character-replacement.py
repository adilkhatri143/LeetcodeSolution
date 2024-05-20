class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_to_count = dict()
        max_len, window_start, max_freq = 0, 0, 0
        for window_end in range(len(s)):
            char_to_count[s[window_end]] = char_to_count.get(s[window_end], 0) + 1
            max_freq = max(max_freq, char_to_count[s[window_end]])
            if window_end - window_start + 1 - max_freq > k:
                max_len = max(max_len, window_end - window_start)
                char_to_count[s[window_start]] = char_to_count.get(s[window_start]) - 1
                window_start += 1
        return max(max_len, window_end - window_start + 1)