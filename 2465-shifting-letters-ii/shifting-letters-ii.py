class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        prefix_sum_for_shift = [0] * (len(s) + 1)
        for start, end, direction in shifts:
            if direction == 1:
                prefix_sum_for_shift[start] += 1
                prefix_sum_for_shift[end + 1] -= 1
            else:
                prefix_sum_for_shift[start] -= 1
                prefix_sum_for_shift[end + 1] += 1
        
        word = list(s)
        prefix_sum = 0
        for i in range(len(word)):
            prefix_sum += prefix_sum_for_shift[i]
            word[i] = chr(((ord(word[i]) + prefix_sum - 97) % 26) + 97)
        return "".join(word)
