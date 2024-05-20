class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        window_start = window_end = 0
        char_to_count = dict() 
        set_count = 0
        for window_start in range(len(s)):
            if window_start < 3:
                char_to_count[s[window_start]] = char_to_count.get(s[window_start], 0) + 1
            else:
                char_to_count[s[window_end]] = char_to_count.get(s[window_end]) - 1
                if char_to_count[s[window_end]] == 0:
                    char_to_count.pop(s[window_end])
                window_end += 1
                char_to_count[s[window_start]] = char_to_count.get(s[window_start], 0) + 1
            if len(char_to_count) == 3:
                set_count += 1
        return set_count


