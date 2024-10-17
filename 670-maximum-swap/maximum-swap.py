class Solution:
    def maximumSwap(self, num: int) -> int:
        num_str = list(str(num))
        max_idx = [0] * len(num_str)
        max_idx[-1] = len(num_str) - 1
        for i in range(len(num_str) - 2, -1, -1):
            if int(num_str[i]) > int(num_str[max_idx[i + 1]]):
                max_idx[i] = i
            else:
                max_idx[i] = max_idx[i + 1]
        for i in range(len(num_str)):
            if num_str[i] < num_str[max_idx[i]]:
                num_str[i], num_str[max_idx[i]] = num_str[max_idx[i]], num_str[i]
                break
        return int("".join(num_str))