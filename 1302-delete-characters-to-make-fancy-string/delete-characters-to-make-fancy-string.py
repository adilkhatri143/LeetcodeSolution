class Solution:
    def makeFancyString(self, s: str) -> str:
        if len(s) < 3:
            return s
        new_s = list()
        first, second, third = 0, 1, 2
        while first < len(s):
            if not (third < len(s) and s[first] == s[second] == s[third]):
                new_s.append(s[first])
            first += 1
            second += 1
            third += 1
        return "".join(new_s)