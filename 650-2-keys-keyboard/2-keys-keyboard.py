class Solution:
    def solve(self, n, screen, clipboard, dp):
        if screen == n:
            return 0
        if screen > n:
            return float('inf')
        if (screen, clipboard) in dp:
            return dp[(screen, clipboard)]

        copy_paste = self.solve(n, screen + screen, screen, dp) + 2
        paste = float('inf')
        if clipboard:
            paste = self.solve(n, screen + clipboard, clipboard, dp) + 1
        dp[(screen, clipboard)] = min(copy_paste, paste)
        return dp[(screen, clipboard)]

    def minSteps(self, n: int) -> int:
        dp = dict()
        return self.solve(n, 1, 0, dp)