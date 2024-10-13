class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        merged = []
        for idx, num in enumerate(nums):
            for val in num:
                merged.append((val, idx))
        merged.sort()
        k = len(nums)
        min_max = [0, float("inf")]
        contains = dict()
        window_end = 0
        for window_start in range(len(merged)):
            contains[merged[window_start][1]] = contains.get(merged[window_start][1], 0) + 1
            while len(contains) == k:
                cur_min = merged[window_end][0]
                cur_max = merged[window_start][0]
                if cur_max - cur_min < min_max[1] - min_max[0]:
                    min_max[0] = cur_min
                    min_max[1] = cur_max
                contains[merged[window_end][1]] = contains.get(merged[window_end][1]) - 1
                if contains[merged[window_end][1]] <= 0:
                    contains.pop(merged[window_end][1])  
                window_end += 1    
        return min_max


