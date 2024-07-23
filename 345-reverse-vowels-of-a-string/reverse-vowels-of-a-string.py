class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        ch = list(s)
        i, j = 0, len(ch) - 1
        while i < j:
            if ch[i] not in vowel:
                i += 1
            elif ch[j] not in vowel:
                j -= 1
            else:
                ch[i], ch[j] = ch[j], ch[i]
                i += 1
                j -= 1
        return "".join(ch)