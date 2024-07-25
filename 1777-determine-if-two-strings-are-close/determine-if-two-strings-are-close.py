class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        count1 = [0] * 26
        count2 = [0] * 26
        for ch in word1:
            count1[ord(ch) - 97] += 1
        for ch in word2:
            count2[ord(ch) - 97] += 1
        for i in range(26):
            if (count1[i] != 0 and count2[i] == 0) or (count1[i] == 0 and count2[i] != 0):
                return False
        count1.sort()
        count2.sort()
        for i in range(26):
            if count1[i] != count2[i]:
                return False
        return True

            