class Solution:
    def reverse(self, x: int) -> int:
        negative_sign = False
        if x < 0:
            negative_sign = True
            x *= -1
        reverse = 0
        while x:
            rem = x % 10
            reverse = (reverse * 10) + rem
            x //= 10
        if reverse > 2 ** 31 - 1:
            return 0
        return reverse * -1 if negative_sign else reverse