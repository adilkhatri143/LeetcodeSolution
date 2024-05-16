class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel = {'a', 'e', 'i', 'o', 'u'}
        vowel_count = 0
        max_vowel_count = 0
        for i in range(k):
            if s[i] in vowel:
                vowel_count += 1
        max_vowel_count = max(max_vowel_count, vowel_count)
        for i in range(k, len(s)):
            if s[i - k] in vowel:
                vowel_count -= 1
            if s[i] in vowel:
                vowel_count += 1
            max_vowel_count = max(max_vowel_count, vowel_count)
        return max_vowel_count
