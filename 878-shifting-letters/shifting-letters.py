class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        prefix_sum_shift = [0] * len(shifts)
        prefix_sum_shift[-1] = shifts[-1]
        for i in range(len(shifts) - 2, -1, -1):
            prefix_sum_shift[i] = (prefix_sum_shift[i + 1] + shifts[i]) % 26
        word = list(s)
        for i in range(len(shifts)):
            word[i] = chr((((ord(word[i]) - 97) + prefix_sum_shift[i]) % 26) + 97)
        return "".join(word)