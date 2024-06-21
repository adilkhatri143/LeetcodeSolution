class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        max_unsatisfied = cur_unsatisfied = 0
        for i in range(minutes):
            cur_unsatisfied += customers[i] * grumpy[i]
        max_unsatisfied = max(max_unsatisfied, cur_unsatisfied)
        i, j = 0, minutes
        while j < len(customers):
            cur_unsatisfied -= customers[i] * grumpy[i]
            cur_unsatisfied += customers[j] * grumpy[j]
            max_unsatisfied = max(max_unsatisfied, cur_unsatisfied)
            i += 1
            j += 1
        satisfied = 0
        for i in range(len(customers)):
            satisfied += customers[i] * (1 - grumpy[i])
        return satisfied + max_unsatisfied