class Solution:
    data = None
    def solve(self, idx, s, word_set, temp_ans):
        if idx == len(s):
            self.data.append(temp_ans[:-1])
            return
        
        temp_s = ""
        for i in range(idx, len(s)):
            temp_s += s[i]
            if temp_s in word_set:
                self.solve(i + 1, s, word_set, temp_ans + temp_s + " ")

    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        self.data= list()
        word_set = set()
        for word in wordDict:
            word_set.add(word)
        self.solve(0, s, word_set, "")
        return self.data