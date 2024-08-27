class Solution:
    # def solve(self, alice_score, bob_score, left, right, turn, piles):
    #     if left > right:
    #         return alice_score > bob_score
        
    #     if turn:
    #         # alice turn
    #         if piles[left] > piles[right]:
    #             return self.solve(alice_score + piles[left], bob_score, left + 1, right, 0, piles)
    #         elif piles[left] < piles[right]:
    #             return self.solve(alice_score + piles[right], bob_score, left, right - 1, 0, piles)
    #         else:
    #             return self.solve(alice_score + piles[left], bob_score, left + 1, right, 0, piles) or self.solve(alice_score + piles[right], bob_score, left, right - 1, 0, piles)
    #     else:
    #         # bob turn
    #         if piles[left] > piles[right]:
    #             return self.solve(alice_score, bob_score + piles[left], left + 1, right, 1, piles)
    #         elif piles[left] < piles[right]:
    #             return self.solve(alice_score, bob_score + piles[right], left, right - 1, 1, piles)
    #         else:
    #             return self.solve(alice_score, bob_score + piles[left], left + 1, right, 1, piles) or self.solve(alice_score, bob_score + piles[right], left, right - 1, 1, piles)

    def solve(self, alice_score, bob_score, left, right, turn, piles, dp):
        if left > right:
            return alice_score > bob_score
        if (left, right, turn) in dp:
            return dp[(left, right, turn)]
        if turn:
            dp[(left, right, turn)] = self.solve(alice_score + piles[left], bob_score, left + 1, right, 0, piles, dp) or self.solve(alice_score + piles[right], bob_score, left, right - 1, 0, piles, dp)
        else:
            # bob turn
            dp[(left, right, turn)] = self.solve(alice_score, bob_score + piles[left], left + 1, right, 1, piles, dp) or self.solve(alice_score, bob_score + piles[right], left, right - 1, 1, piles, dp)
        return dp[(left, right, turn)]

    def stoneGame(self, piles: List[int]) -> bool:
        return self.solve(0, 0, 0, len(piles) - 1, 1, piles, dict())