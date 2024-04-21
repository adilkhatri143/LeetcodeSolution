class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        answer = []
        for row in range(1, numRows + 1):
            cur_row_list = [1] * row
            for col in range(1, row - 1):
                cur_row_list[col] = answer[-1][col - 1] + answer[-1][col]
            answer.append(cur_row_list)
        return answer