class Solution:
    max_unique_substring = float("-inf")
    def solve(self, idx, s, exist):
        if idx == len(s):
            self.max_unique_substring = max(self.max_unique_substring, len(exist))
            return 

        new_str = ""
        for i in range(idx, len(s)):
            new_str += s[i]
            if new_str not in exist:
                exist.add(new_str)
                self.solve(i + 1, s, exist)
                exist.remove(new_str)
                
    def maxUniqueSplit(self, s: str) -> int:
        self.max_unique_substring = float("-inf")
        self.solve(0, s, set())
        return self.max_unique_substring