class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            cur_sum = 0
            while num:
                cur_sum += num % 10
                num //= 10
            num = cur_sum
        return num