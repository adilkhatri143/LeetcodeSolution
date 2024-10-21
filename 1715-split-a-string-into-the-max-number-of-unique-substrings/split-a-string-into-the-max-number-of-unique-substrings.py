class Solution:
    max_unique_substring = float("-inf")
    def solve(self, idx, s, exist):
        if idx == len(s):
            self.max_unique_substring = max(self.max_unique_substring, len(exist))
            return 

        new_str = []
        for i in range(idx, len(s)):
            new_str.append(s[i])
            temp_join = "".join(new_str)
            if temp_join not in exist:
                exist.add(temp_join)
                self.solve(i + 1, s, exist)
                exist.remove(temp_join)
                
    def maxUniqueSplit(self, s: str) -> int:
        self.max_unique_substring = float("-inf")
        self.solve(0, s, set())
        return self.max_unique_substring