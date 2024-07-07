class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total = numBottles
        while numBottles >= numExchange:
            emptied = numBottles // numExchange
            rem_empty = numBottles % numExchange
            numBottles = emptied + rem_empty
            total += emptied
        return total