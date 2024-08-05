class Solution:
    answer = list()
    def solve(self, k, n, start, temp):
        if n < 0 or k < 0:
            return
        if n == 0 and k == 0:
            self.answer.append(temp)
            return

        for j in range(start, 10):
            self.solve(k - 1, n - j, j + 1, temp + [j])


    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        if k > n:
            return []
        self.answer.clear()
        self.solve(k, n, 1, [])
        return self.answer