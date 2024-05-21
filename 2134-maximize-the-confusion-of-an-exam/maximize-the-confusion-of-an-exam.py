class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        char_to_count = dict()
        max_freq = window_end = max_len = 0
        for window_start in range(len(answerKey)):
            char_to_count[answerKey[window_start]] = char_to_count.get(answerKey[window_start], 0) + 1
            max_freq = max(max_freq, char_to_count[answerKey[window_start]])
            if window_start - window_end + 1 - max_freq > k:
                max_len = max(max_len, window_start - window_end - k)
                char_to_count[answerKey[window_end]] = char_to_count.get(answerKey[window_end]) - 1
                window_end += 1
        return max(max_len, window_start - window_end + 1)
