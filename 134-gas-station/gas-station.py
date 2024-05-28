class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gas = cur_gas = index = 0
        for i in range(len(gas)):
            total_gas += gas[i] - cost[i]
            cur_gas += gas[i] - cost[i]
            if cur_gas < 0:
                cur_gas = 0
                index = i + 1
        return -1 if total_gas < 0 else index