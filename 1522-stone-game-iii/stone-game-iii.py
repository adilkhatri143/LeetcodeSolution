class Solution:
    def solve(self, idx, turn, stoneValue, dp):
        if idx >= len(stoneValue):
            return 0
        if (idx, turn) in dp:
            return dp[(idx, turn)]
        score = 0
        if turn:
            answer = float("-inf")
            for i in range(idx, min(idx + 3, len(stoneValue))):
                score += stoneValue[i]
                answer = max(answer, score + self.solve(i + 1, 0, stoneValue, dp))
        else:
            answer = float("inf")
            for i in range(idx, min(idx + 3, len(stoneValue))):
                answer = min(answer, self.solve(i + 1, 1, stoneValue, dp))
        dp[(idx, turn)] = answer
        return dp[(idx, turn)]

    def stoneGameIII(self, stoneValue: List[int]) -> str:
        total_score = sum(stoneValue)
        alice_score = self.solve(0, 1, stoneValue, dict())
        if total_score - alice_score == alice_score:
            return "Tie"
        elif total_score - alice_score > alice_score:
            return "Bob"
        return "Alice"