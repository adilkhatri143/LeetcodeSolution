class Solution:
    def minimumSteps(self, s: str) -> int:
        ch_list = list(s)
        ans = 0
        i = j = len(s) - 1
        while i >= 0 and j >= 0:
            if ch_list[i] == "0":
                j -= 1
                while j >= 0 and ch_list[j] != "1":
                    j -= 1
                ch_list[i], ch_list[j] = ch_list[j], ch_list[i]
                if j < 0:
                    break
                ans += i - j
            else:
                j -= 1
            i -= 1
        return ans
