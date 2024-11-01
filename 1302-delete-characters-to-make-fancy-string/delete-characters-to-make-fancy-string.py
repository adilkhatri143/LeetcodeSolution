class Solution:
    def makeFancyString(self, s: str) -> str:
        first, second, third = 0, 1, 2
        if len(s) < 3:
            return s
        new_s = ""
        while first < len(s):
            if third < len(s) and s[first] == s[second] == s[third]:
                first += 1
                second += 1
                third += 1
            else:
                new_s += s[first]
                first += 1
                second += 1
                third += 1
        return new_s