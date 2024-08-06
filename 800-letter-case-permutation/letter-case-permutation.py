class Solution:
    answer = list()
    def solve(self, idx, s, temp):
        if idx == len(s):
            self.answer.append(temp)
            return
        
        if s[idx].isalpha():
            self.solve(idx + 1, s, temp + s[idx].lower())
            self.solve(idx + 1, s, temp + s[idx].upper())
        else:
            self.solve(idx + 1, s, temp + s[idx])

    def letterCasePermutation(self, s: str) -> List[str]:
        self.answer = list()
        self.solve(0, s, "")
        return self.answer