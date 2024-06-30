class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        op_ht = {"--X": -1, "X--": -1, "X++": 1, "++X": 1}
        for op in operations:
            x += op_ht[op]
        return x