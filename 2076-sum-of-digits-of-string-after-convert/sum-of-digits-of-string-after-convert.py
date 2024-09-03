class Solution:
    def getLucky(self, s: str, k: int) -> int:
        num = ""
        for ch in s:
            num += str(ord(ch) - 97 + 1)
        num = int(num)
        print(num)
        while k and num:
            copy_num = num
            answer = 0
            while copy_num:
                rem = copy_num % 10
                copy_num //= 10
                answer += rem
            num = answer
            k -= 1
        return num

