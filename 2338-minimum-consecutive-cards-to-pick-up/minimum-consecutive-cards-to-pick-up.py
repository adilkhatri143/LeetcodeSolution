class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        answer = float('inf')
        seen = dict()
        for i, card in enumerate(cards):
            if card in seen:
                if i - seen[card] + 1 < answer:
                    answer = i - seen[card] + 1
                    seen[card] = i
            seen[card] = i
        return -1 if answer == float('inf') else answer