class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        largest = arrays[0][-1]
        smallest = arrays[0][0]
        max_dis = float("-inf")
        for i in range(1, len(arrays)):
            max_dis = max(max_dis, abs(smallest - arrays[i][-1]), abs(largest - arrays[i][0]))
            largest = max(largest, arrays[i][-1])
            smallest = min(smallest, arrays[i][0])
        return max_dis