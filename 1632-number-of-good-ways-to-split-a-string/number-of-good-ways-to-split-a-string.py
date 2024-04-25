class Solution:
    def numSplits(self, s: str) -> int:
        left_char_to_count = dict()
        right_char_to_count = dict()
        for i in range(len(s)):
            right_char_to_count[s[i]] = right_char_to_count.get(s[i], 0) + 1
        count = 0
        for i in range(len(s)):
            left_char_to_count[s[i]] = left_char_to_count.get(s[i], 0) + 1
            right_char_to_count[s[i]] = right_char_to_count.get(s[i]) - 1
            if right_char_to_count[s[i]] == 0:
                right_char_to_count.pop(s[i])
            if len(left_char_to_count) == len(right_char_to_count):
                count += 1
        return count