class Solution:
    def minimumPushes(self, word: str) -> int:
        alphabet_count = [0 for i in range(26)]
        for ch in word:
            alphabet_count[ord(ch) - 97] += 1
        alphabet_count.sort(reverse=True)
        print(alphabet_count)
        answer = diff_alpha = 0
        multiple = 1
        for val in alphabet_count:
            if val == 0:
                break
            answer += (val * multiple)
            diff_alpha += 1
            if diff_alpha % 8 == 0:
                multiple += 1
        return answer
        