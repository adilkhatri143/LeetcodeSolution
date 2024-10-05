class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        ht = dict()
        for ch in s1:
            ht[ch] = ht.get(ch, 0) + 1
        ht2 = dict()
        for i in range(len(s1)):
            ht2[s2[i]] = ht2.get(s2[i], 0) + 1
        if ht == ht2:
            return True
        for i in range(len(s1), len(s2)):
            ht2[s2[i]] = ht2.get(s2[i], 0) + 1
            ht2[s2[i - len(s1)]] = ht2.get(s2[i - len(s1)]) - 1
            if ht2[s2[i - len(s1)]] <= 0:
                ht2.pop(s2[i - len(s1)])
            if ht == ht2:
                return True
        return False
