class Solution:
    answer = list()
    def solve(self, open_bracket, close_bracket, temp_ans, n):
        if open_bracket == close_bracket == n:
            self.answer.append("".join(temp_ans))
            return
        if open_bracket > n or close_bracket > open_bracket:
            return
        temp_ans.append("(")
        self.solve(open_bracket + 1, close_bracket, temp_ans, n)
        temp_ans.pop()
        temp_ans.append(")")
        self.solve(open_bracket, close_bracket + 1, temp_ans, n)
        temp_ans.pop()

    def generateParenthesis(self, n: int) -> List[str]:
        self.answer = list()
        self.solve(0, 0, [], n)
        return self.answer