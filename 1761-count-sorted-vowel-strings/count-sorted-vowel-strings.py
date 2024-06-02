class Solution:
    def countVowelStrings(self, n: int) -> int:
        a, e, i, o, u = 1, 1, 1, 1, 1
        for k in range(1, n):
            a = a + e + i + o + u
            e = e + i + o + u
            i = i + o + u
            o = o + u
        return a + e + i + o + u