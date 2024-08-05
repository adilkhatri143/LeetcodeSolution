class Solution:
    keypad = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
    answer = list()
    def solve(self, idx, digits, temp_ans):
        if idx == len(digits):
            if len(digits) != 0:
                self.answer.append(temp_ans)
            return
        
        letters = self.keypad[int(digits[idx])]
        for letter in letters:
            self.solve(idx + 1, digits, temp_ans + letter)


    def letterCombinations(self, digits: str) -> List[str]:
        self.answer.clear()
        self.solve(0, digits, "")    
        return self.answer  
