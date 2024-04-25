class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        # here dp represents longestIdealSubsequece at index i 
        # let say i = 1 ie b, represent LIS ending at b
        dp = [0 for i in range(26)]
        answer = 1
        for val in s:
            char_to_int = ord(val) - 97
            left = max(0, char_to_int - k)
            right = min(25, char_to_int + k)
            cur_max = float('-inf')
            for i in range(left, right + 1):
                cur_max = max(cur_max, dp[i] + 1)
            dp[char_to_int] = cur_max
            answer = max(answer, dp[char_to_int])
        return answer